#!/usr/bin/env python3
"""Normalisasi teks bahasa Indonesia untuk TTS / voice-over / text normalization.

Mengubah angka, uang, persen, kelipatan, rentang, tanggal, jam, nomor telepon, satuan, dan
entri leksikon yang tidak ambigu menjadi bentuk ucapan. Hal yang tidak pasti TIDAK diubah,
melainkan dicatat di daftar RAGU.

Pemakaian:
  python scripts/normalize.py "Live mulai 19.00 WIB, harganya Rp25.000 aja."
  python scripts/normalize.py --mode spoken --time-style casual "..."
  python scripts/normalize.py --json < naskah.txt

Mode:
  tts     (default) pakai `respelling` leksikon bila ada (ejaan bantu untuk mesin TTS), kurung → koma, emoji dihapus.
  spoken  pakai `spoken_form` (ejaan biasa) — untuk normalisasi teks/caption suara.
Hanya pustaka standar Python 3.9+.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lookup import load_lexicon  # noqa: E402

UNITS = ["nol", "satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan", "sembilan"]
MONTHS = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
MONTH_ABBR = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "mei": 5, "jun": 6, "jul": 7, "agu": 8, "agt": 8, "ags": 8, "aug": 8,
              "sep": 9, "okt": 10, "oct": 10, "nov": 11, "des": 12, "dec": 12}
ZONES = {"WIB": "we i be", "WITA": "wita", "WIT": "we i te"}
MAGNITUDE = {"ribu": "ribu", "rb": "ribu", "juta": "juta", "jt": "juta", "miliar": "miliar", "M": "miliar", "triliun": "triliun", "T": "triliun"}
END_ABBR = {"dll.", "dsb.", "dst.", "dkk.", "etc."}  # singkatan yang lazim menutup kalimat/daftar
CURRENCY_WORDS = {"rupiah", "dolar", "euro", "persen", "ringgit", "yen"}
CONTEXT_RULES = [
    (r"\bNo\.\s?(?=\d)", "nomor ", "konteks: No. + angka → nomor (abbr No.)"),
    (r"\bHal\.\s?(?=\d)", "halaman ", "konteks: Hal. + angka → halaman (abbr Hal.)"),
]
PER_WORDS = {"peserta", "pax", "kamar", "paket", "sesi", "hari", "jam", "bulan", "minggu", "pekan", "tahun", "detik", "menit", "orang", "kg", "km", "unit", "pcs", "item", "video",
             "malam", "sesi", "porsi", "lembar", "halaman", "kata", "karakter", "liter", "meter"}
EMOJI = re.compile("[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F2FF️‍]+")
NUM = r"\d{1,3}(?:\.\d{3})+(?:,\d+)?|\d+(?:,\d+)?"  # Indonesian number: 1.250.000,50 | 1,5 | 25


# ---------------------------------------------------------------- number words
def int_words(n: int) -> str:
    if n < 0:
        return "minus " + int_words(-n)
    if n < 10:
        return UNITS[n]
    if n == 10:
        return "sepuluh"
    if n == 11:
        return "sebelas"
    if n < 20:
        return UNITS[n - 10] + " belas"
    if n < 100:
        return _join(UNITS[n // 10] + " puluh", n % 10)
    if n < 200:
        return _join("seratus", n - 100)
    if n < 1000:
        return _join(UNITS[n // 100] + " ratus", n % 100)
    if n < 2000:
        return _join("seribu", n - 1000)
    for size, word in ((10**12, "triliun"), (10**9, "miliar"), (10**6, "juta"), (10**3, "ribu")):
        if n >= size:
            if n >= size * 1000 and word == "triliun":
                break
            return _join(int_words(n // size) + " " + word, n % size)
    raise ValueError(f"Bilangan terlalu besar: {n}")


def _join(head: str, rest: int) -> str:
    return head if rest == 0 else f"{head} {int_words(rest)}"


def digits_words(s: str) -> str:
    return " ".join(UNITS[int(d)] for d in s if d.isdigit())


def parse_id_number(s: str) -> tuple[int, str]:
    """'1.250.000,50' -> (1250000, '50'); '1,5' -> (1, '5')."""
    if "," in s:
        ip, frac = s.split(",", 1)
    else:
        ip, frac = s, ""
    return int(ip.replace(".", "")), frac


def number_words(s: str) -> str:
    ip, frac = parse_id_number(s)
    out = int_words(ip)
    frac = frac.rstrip("-")
    if frac and set(frac) != {"0"}:
        out += " koma " + digits_words(frac)
    return out


def with_magnitude(s: str, mag: str) -> str:
    ip, frac = parse_id_number(s)
    if frac == "5":
        return f"setengah {mag}" if ip == 0 else f"{int_words(ip)} setengah {mag}"
    return f"{number_words(s)} {mag}"


# ---------------------------------------------------------------- normalizer
class Normalizer:
    def __init__(self, lexicon: dict, mode: str = "tts", time_style: str = "formal", include_unvalidated: bool = False):
        self.mode, self.time_style = mode, time_style
        self.changes: list[dict] = []
        self.ragu: list[dict] = []
        self.notes: list[dict] = []
        self._protected: list[str] = []
        entries = lexicon["entries"]
        self.by_text = {}
        for e in entries:
            self.by_text.setdefault(e["text"], e)
        self.units = sorted([e for e in entries if e["category"] == "unit" and e["entry_type"] == "lexical"], key=lambda e: -len(e["text"]))
        self.currency_codes = {e["text"]: e for e in entries if e["category"] == "currency" and e["subcategory"] == "code"}
        self.subst, self.ambiguous, self.homographs = [], [], []
        for e in entries:
            if e["entry_type"] != "lexical":
                continue
            if e["subcategory"] == "homograph":
                self.homographs.append(e)
                continue
            if e.get("ambiguous"):
                if e["category"] not in ("general", "symbol"):
                    self.ambiguous.append(e)  # simbol ditangani aturan di tahap C
                continue
            if not self._eligible(e, include_unvalidated):
                continue
            self.subst.append(e)
        self.subst.sort(key=lambda e: -len(e["text"]))
        self.ambiguous.sort(key=lambda e: -len(e["text"]))

    @staticmethod
    def _eligible(e: dict, include_unvalidated: bool) -> bool:
        if e["spoken_form"].startswith("("):
            return False
        if e["confidence"] == "needs_validation" and not include_unvalidated:
            return False
        cat, sub = e["category"], e["subcategory"]
        if cat in ("general", "symbol", "number", "alphabet"):
            return False
        if cat == "currency" and sub != "code":
            return False
        if cat == "unit" and len(e["text"]) <= 2:
            return False  # satuan pendek hanya diubah bila didahului angka
        if cat == "date-time" and sub not in ("time-zone", "time-format"):
            return False
        if cat == "loanword" and e.get("respelling") is None and e["spoken_form"] == e["text"]:
            return False  # kata serapan yang dibaca sesuai ejaan tidak perlu diubah
        return True

    # -- helpers
    def _log(self, original: str, output: str, rule: str, entry: str | None = None):
        if original != output:
            item = {"asli": original, "jadi": output, "aturan": rule}
            if entry:
                item["entri"] = entry
            self.changes.append(item)

    def _flag(self, token: str, reason: str):
        if not any(r["token"] == token and r["alasan"] == reason for r in self.ragu):
            self.ragu.append({"token": token, "alasan": reason})

    def _protect(self, token: str) -> str:
        """Sembunyikan token ragu dari aturan berikutnya agar tidak diubah sebagian."""
        self._protected.append(token)
        return "\ue000" + chr(0xE100 + len(self._protected) - 1) + "\ue001"  # tanpa digit

    def _restore(self, t: str) -> str:
        return re.sub("\ue000(.)\ue001", lambda m: self._protected[ord(m.group(1)) - 0xE100], t)

    def _sub(self, pattern: str, func, text: str, rule: str, flags=0) -> str:
        def repl(m):
            out = func(m)
            if out is None:
                return m.group(0)
            if isinstance(out, tuple):  # ("protect", alasan): tandai RAGU dan lindungi token utuh
                self._flag(m.group(0), out[1])
                return self._protect(m.group(0))
            self._log(m.group(0), out, rule)
            return out
        return re.sub(pattern, repl, text, flags=flags)

    def _reading(self, e: dict) -> str:
        if self.mode == "tts" and e.get("respelling"):
            return e["respelling"]
        return e["spoken_form"]

    # -- stage A: numeric patterns tied to letters/symbols
    def stage_a(self, t: str) -> str:
        B = r"(?<![\w.,])"
        E = r"(?![\w])"
        # versi
        t = self._sub(B + r"[vV](\d+(?:\.\d+){1,3})" + E, lambda m: "versi " + " titik ".join(int_words(int(p)) for p in m.group(1).split(".")), t, "nomor versi")
        # tanggal ISO
        def iso(m):
            y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
            if not (1 <= mo <= 12 and 1 <= d <= 31):
                return None
            return f"{int_words(d)} {MONTHS[mo-1]} {int_words(y)}"
        t = self._sub(B + r"(\d{4})-(\d{2})-(\d{2})" + E, iso, t, "tanggal ISO")
        # tanggal d/m/y
        def dmy(m):
            d, mo, y = int(m.group(1)), int(m.group(2)), m.group(3)
            if len(y) != 4:
                return ("protect", "Tahun dua digit: abad tidak pasti. Tidak diubah.")
            if mo > 12 or mo == 0 or d == 0 or d > 31:
                return ("protect", "Bulan > 12 atau tanggal tidak valid: kemungkinan format bulan/hari (AS). Tidak diubah.")
            if d <= 12 and d != mo:
                self.notes.append({"token": m.group(0), "catatan": "Diasumsikan hari/bulan/tahun (konvensi Indonesia)."})
            return f"{int_words(d)} {MONTHS[mo-1]} {int_words(int(y))}"
        t = self._sub(B + r"(\d{1,2})/(\d{1,2})/(\d{2,4})" + E, dmy, t, "tanggal hari/bulan/tahun")
        # pecahan a/b (setelah tanggal)
        def frac(m):
            if m.group(1).startswith("0") or m.group(2).startswith("0"):
                return ("protect", "Diawali nol: kode/tanggal, bukan pecahan. Tidak diubah.")
            a, b = int(m.group(1)), int(m.group(2))
            if b == 0 or b > 100:
                return None
            if a == 1:
                return "setengah" if b == 2 else "seper" + int_words(b)
            return f"{int_words(a)} per{int_words(b)}"
        t = self._sub(r"(?<![\w.,/])(\d{1,2})/(\d{1,3})(?![\w/])", frac, t, "pecahan")
        # tanggal '1 Feb 2027'
        def dmony(m):
            mo = MONTH_ABBR.get(m.group(2).lower()[:3])
            if not mo:
                return None
            return f"{int_words(int(m.group(1)))} {MONTHS[mo-1]} {int_words(int(m.group(3)))}"
        t = self._sub(B + r"(\d{1,2})\s([A-Za-z]{3,9})\.?\s(\d{4})" + E, dmony, t, "tanggal dengan nama bulan")
        # rentang jam: 09.00–11.30 WIB
        def time_range(m):
            prefix, zone = m.group(1), m.group(6)
            a = self._time_core(prefix or "pukul", int(m.group(2)), int(m.group(3)), None)
            b = self._time_core(prefix or "pukul", int(m.group(4)), int(m.group(5)), zone)
            return f"{a} sampai {b}"
        t = self._sub(r"(?:\b(pukul|jam)\s)?" + B + r"([01]?\d|2[0-3])[.:]([0-5]\d)\s?[-–]\s?([01]?\d|2[0-3])[.:]([0-5]\d)(?!\d)(?:\s?(WIB|WITA|WIT)\b)?",
                      lambda m: time_range(m) if (m.group(1) or m.group(6)) else ("protect", "Rentang angka bertitik tanpa 'pukul'/zona: jam atau bilangan? Tidak diubah."), t, "rentang jam")
        # nomor standar/model: ISO 27001:2022, SNI 7612, RFC 9110
        t = self._sub(r"\b([A-Z]{2,}(?:/[A-Z]{2,})?)\s(\d{3,}(?:[-:]\d{1,4})*)\b",
                      lambda m: ("protect", f"Nomor standar/model setelah '{m.group(1)}': baca per digit (mis. '{digits_words(m.group(2).split(':')[0])}') atau sebagai bilangan? Tahun setelah ':' dibaca penuh. Konfirmasi.")
                      if not re.fullmatch(r"(?:19|20)\d{2}", m.group(2)) else None, t, "nomor standar")
        # kuartal Q1–Q4
        t = self._sub(r"\bQ([1-4])\b", lambda m: ("protect", f"Kuartal: 'kuartal {int_words(int(m.group(1)))}' (formal) atau 'kyu {int_words(int(m.group(1)))}'? Konfirmasi."), t, "kuartal")
        # jam
        t = self._sub(r"(?:\b(pukul|jam)\s)?" + B + r"([01]?\d|2[0-3])[.:]([0-5]\d)(?!\d)(?:\s?(WIB|WITA|WIT)\b)?", self._time, t, "jam")
        # telepon
        def phone(m):
            groups = re.split(r"[- ]", m.group(0).strip())
            words = []
            for g in groups:
                words.append("plus " + digits_words(g) if g.startswith("+") else digits_words(g))
            return ", ".join(words)
        t = self._sub(r"(?:\+62[- ]?|(?<![\w\d])0)\d{2,3}[- ]\d{3,4}[- ]\d{3,5}(?!\d)", phone, t, "nomor telepon (per digit)")
        # rupiah rentang: Rp2-7 juta
        def rp_range(m):
            mag = MAGNITUDE.get(m.group(3) or "", "")
            a, b = number_words(m.group(1)), number_words(m.group(2))
            return f"{a} sampai {b}{' ' + mag if mag else ''} rupiah"
        t = self._sub(r"Rp\.?\s?(" + NUM + r")\s?[-–]\s?(" + NUM + r")(?:\s?(juta|jt|ribu|rb|miliar|M|triliun|T)\b)?", rp_range, t, "rentang rupiah")
        # rupiah
        def rp(m):
            amt, mag = m.group(1), m.group(2)
            if mag:
                return f"{with_magnitude(amt, MAGNITUDE[mag])} rupiah"
            return f"{number_words(amt)} rupiah"
        t = self._sub(r"Rp\.?\s?(" + NUM + r")(?:,-)?(?:\s?(juta|jt|ribu|rb|miliar|M|triliun|T)\b)?", rp, t, "mata uang rupiah")
        # dolar / euro / pound
        def foreign(m):
            sym, amt, mag = m.group(1), m.group(2), m.group(3)
            name = {"US$": "dolar Amerika", "$": "dolar", "€": "euro", "£": "pound sterling"}[sym]
            if re.fullmatch(r"\d{1,3}(?:,\d{3})+(?:\.\d+)?", amt):
                self._flag(m.group(0), "Format angka gaya Inggris (koma ribuan). Dibaca sebagai ribuan.")
                amt = amt.replace(",", "").replace(".", ",")
            words = with_magnitude(amt, MAGNITUDE[mag]) if mag else number_words(amt)
            return f"{words} {name}"
        t = self._sub(r"(US\$|\$|€|£)\s?(\d[\d.,]*\d|\d)(?:\s?(juta|jt|ribu|rb|miliar|M|triliun|T)\b)?", foreign, t, "mata uang asing")
        # kode mata uang + angka (USD 5, 5 USD)
        codes = "|".join(map(re.escape, self.currency_codes))
        if codes:
            t = self._sub(r"\b(" + codes + r")\s?(" + NUM + r")" + E,
                          lambda m: f"{number_words(m.group(2))} {self.currency_codes[m.group(1)]['spoken_form']}", t, "kode mata uang")
            t = self._sub(B + r"(" + NUM + r")\s?(" + codes + r")\b",
                          lambda m: f"{number_words(m.group(1))} {self.currency_codes[m.group(2)]['spoken_form']}", t, "kode mata uang")
        # yen/yuan ambigu
        t = self._sub(r"¥\s?\d[\d.,]*", lambda m: ("protect", "¥ dipakai untuk yen (Jepang) dan yuan (Tiongkok). Tidak diubah."), t, "¥")
        # abad + angka Romawi
        t = self._sub(r"\babad\s+([IVXLC]+)\b", lambda m: f"abad ke{int_words(roman_to_int(m.group(1)))}" if roman_to_int(m.group(1)) else None, t, "abad (Romawi)")
        # persen
        t = self._sub(B + r"(" + NUM + r")\s?%", lambda m: number_words(m.group(1)) + " persen", t, "persen")
        # kelipatan & perkalian
        t = self._sub(B + r"(" + NUM + r")\s?[x×]\s?(" + NUM + r")" + E, lambda m: f"{number_words(m.group(1))} kali {number_words(m.group(2))}", t, "perkalian")
        t = self._sub(B + r"(" + NUM + r")[xX×]" + E, lambda m: number_words(m.group(1)) + " kali", t, "kelipatan")
        # besaran singkat tanpa mata uang
        t = self._sub(B + r"(" + NUM + r")\s?(jt|rb|juta|ribu|miliar|triliun)\b", lambda m: with_magnitude(m.group(1), MAGNITUDE[m.group(2)]), t, "besaran")
        # satuan setelah angka
        for u in self.units:
            ut = re.escape(u["text"])
            if u.get("ambiguous"):
                for mm in re.finditer(B + r"(" + NUM + r")\s?" + ut + E, t):
                    self._flag(mm.group(0), f"Satuan ambigu ({u['id']}): {u['disambiguation']}")
                continue
            t = self._sub(B + r"(" + NUM + r")\s?" + ut + r"(?![\w²³/])" if "/" not in u["text"] else B + r"(" + NUM + r")\s?" + ut + E,
                          lambda m, u=u: f"{number_words(m.group(1))} {u['spoken_form']}", t, f"satuan ({u['id']})")
        # ordinal ke-N
        t = self._sub(r"\bke-(\d+)\b", lambda m: "ke" + int_words(int(m.group(1))), t, "ordinal ke-")
        # dasawarsa -an
        t = self._sub(B + r"(\d{2,4})-an\b", lambda m: int_words(int(m.group(1))) + "an", t, "dasawarsa -an")
        # rentang angka
        def rng(m):
            a, b = m.group(1), m.group(2)
            if (a.startswith("0") and len(a) > 1) or (b.startswith("0") and len(b) > 1):
                return ("protect", "Diawali nol: kemungkinan kode/nomor, bukan rentang. Tidak diubah.")
            if parse_id_number(b)[0] <= parse_id_number(a)[0]:
                return ("protect", "Angka kedua tidak lebih besar: mungkin skor (dua-satu) atau kode, bukan rentang. Tidak diubah.")
            return f"{number_words(a)} sampai {number_words(b)}"
        t = self._sub(B + r"(" + NUM + r")\s?[-–]\s?(" + NUM + r")" + E, rng, t, "rentang")
        # ± ~
        t = self._sub(r"±\s?(?=\d)", lambda m: "kurang lebih ", t, "simbol ±")
        t = self._sub(r"(?<![\w/])~\s?(?=\d)", lambda m: "sekitar ", t, "simbol ~")
        # negatif
        t = self._sub(r"(?:(?<=\s)|^)-(\d+(?:,\d+)?)" + E, lambda m: "minus " + number_words(m.group(1)), t, "bilangan negatif")
        return t

    def _time(self, m):
        prefix, h, mi, zone = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)
        if not prefix and not zone:
            return ("protect", "Bisa jam, desimal gaya Inggris, atau versi. Tambahkan 'pukul'/'jam' atau zona waktu. Tidak diubah.")
        return self._time_core(prefix, h, mi, zone)

    def _time_core(self, prefix, h, mi, zone):
        z = ""
        if zone:
            z = ZONES[zone] if self.mode == "tts" else zone_spoken(zone)
        if self.time_style == "casual":
            period = day_period(h)
            h12 = h % 12 or 12
            nxt = (h + 1) % 12 or 12
            if mi == 0:
                core = f"jam {int_words(h12)} {period}"
            elif mi == 30:
                core = f"jam setengah {int_words(nxt)} {period}"
            elif mi == 15:
                core = f"jam {int_words(h12)} lewat seperempat {period}"
            elif mi == 45:
                core = f"jam {int_words(nxt)} kurang seperempat {period}"
            else:
                core = f"jam {int_words(h12)} lewat {int_words(mi)} {period}"
            return core + (f", {z}" if z else "")
        word = "pukul" if prefix in (None, "pukul") else prefix
        core = f"{word} {int_words(h)}" + ("" if mi == 0 else f" lewat {int_words(mi)} menit")
        return core + (f" {z}" if z else "")

    # -- stage 0: alphanumeric lexicon entries (24/7, MP4, 720p) before numeric rules touch them
    def stage_0(self, t: str) -> str:
        # URL dan surel: lindungi utuh, beri usulan bacaan di RAGU
        def url(m):
            u = m.group(0)
            if "@" in u:
                local, dom = u.split("@", 1)
                sug = f"{local} et {dom.replace('.', ' dot ')}"
            else:
                sug = re.sub(r"^https?://(www\.)?", "", u).rstrip("/").replace(".", " dot ").replace("/", " garis miring ")
            return ("protect", f"Alamat surel/URL; usulan bacaan '{sug}' (sesuaikan bacaan nama domain/merek).")
        t = self._sub(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+|(?:https?://|www\.)[^\s,;()]*[^\s,;().]", url, t, "URL/surel")
        for e in [x for x in self.subst if any(ch.isdigit() for ch in x["text"])]:
            reading = self._reading(e)

            def repl(m, e=e, reading=reading):
                self._log(m.group(0), reading, f"leksikon ({e['confidence']})", e["id"])
                return reading
            t = re.sub(r"(?<![\w])" + re.escape(e["text"]) + r"(?![\w])", repl, t)
        # aturan konteks untuk entri ambigu yang konteksnya tegas
        for rx, out, rule in CONTEXT_RULES:
            t = self._sub(rx, lambda m, out=out: out, t, rule)
        return t

    # -- stage B: lexicon
    def stage_b(self, t: str) -> str:
        for e in self.ambiguous:
            if e["category"] == "unit" and len(e["text"]) <= 2:
                continue  # sudah ditangani di tahap A (hanya bila didahului angka)
            for m in re.finditer(r"(?<![\w])" + re.escape(e["text"]) + r"(?![\w])", t):
                self._flag(m.group(0), f"Ambigu ({e['id']}): {e['disambiguation']}")
        for e in [x for x in self.subst if not any(ch.isdigit() for ch in x["text"])]:
            rx = r"(?<![\w])" + re.escape(e["text"]) + (r"(?![\w])" if e["text"][-1].isalnum() else r"(?![\w])")
            reading = self._reading(e)

            def repl(m, e=e, reading=reading):
                out = reading
                if e["text"] in END_ABBR and re.match(r"\s+[A-Z]|\s*$", m.string[m.end():]):
                    out = reading + "."  # titik singkatan sekaligus akhir kalimat
                self._log(m.group(0), out, f"leksikon ({e['confidence']})", e["id"])
                return out
            t = re.sub(rx, repl, t)
        for e in self.homographs:
            if re.search(r"(?<![\w])" + re.escape(e["text"]) + r"(?![\w])", t, flags=re.IGNORECASE):
                self.notes.append({"token": e["text"], "catatan": f"Homograf ({e['id']}): {e['disambiguation']}"})
        return t

    # -- stage C: remaining numbers & symbols
    def stage_c(self, t: str) -> str:
        B = r"(?<![\w.,])"
        E = r"(?![\w])"
        def plain(m):
            s = m.group(0)
            if any(r["token"] == s for r in self.ragu):
                return None
            if re.fullmatch(r"\d+\.\d{1,2}|\d+\.\d{4,}", s):
                return ("protect", "Titik bukan pemisah ribuan (bukan 3 digit): desimal gaya Inggris, versi, atau jam? Tidak diubah.")
            return number_words(s)
        t = self._sub(B + r"\d+(?:\.\d+)*(?:,\d+)?" + E, plain, t, "bilangan")
        # garis miring
        def slash(m):
            a, b = m.group(1), m.group(2)
            if b.lower() in PER_WORDS or a.lower() in CURRENCY_WORDS:
                return f"{a} per {b}"
            if len(a) == 1 and len(b) == 1 and a.isupper() and b.isupper():
                return f"{a} atau {b}"
            if a[0].isupper() and b[0].isupper() and not a.isupper() and not b.isupper():
                return f"{a} atau {b}"  # Bapak/Ibu, Senin/Selasa
            if (a.lower(), b.lower()) == ("dan", "atau"):
                return "dan atau"
            self._flag(m.group(0), "Garis miring: 'per', 'atau', atau bagian alamat/URL? Tidak diubah.")
            return None
        t = self._sub(r"(?<![\w/:.])([A-Za-z]+)/([A-Za-z]+)(?![\w/])", slash, t, "garis miring")
        t = self._sub(r"(?<=\s)&(?=\s)", lambda m: "dan", t, "simbol &")
        t = self._sub(r"(?<=\s)[=](?=\s)", lambda m: "sama dengan", t, "simbol =")
        t = self._sub(r"(?<=\s)[+](?=\s)", lambda m: "tambah", t, "simbol +")
        for m in re.finditer(r"(?<![\w])(?:\d+[A-Za-z]+\w*|[A-Z]{2,}[0-9]*|[A-Z]+\d+[A-Za-z]*)(?![\w])", t):
            tok = m.group(0)
            if any(tok == r["token"] for r in self.ragu):
                continue
            e = self.by_text.get(tok)
            if e and e["confidence"] == "needs_validation":
                sug = e.get("respelling") or e["spoken_form"]
                self._flag(tok, f"Ada di leksikon ({e['id']}) tetapi needs_validation; usulan '{sug}'. Konfirmasi sebelum dipakai.")
            elif not e:
                self._flag(tok, "Tidak dikenal leksikon: singkatan (dieja?), akronim (dibaca kata?), atau gabungan angka-huruf. Konfirmasi.")
        return t

    def run(self, text: str) -> str:
        t = text
        if self.mode == "tts":
            t2 = EMOJI.sub("", t)
            if t2 != t:
                self._log("(emoji)", "(dihapus)", "hapus emoji")
            t = t2
            t = self._sub(r"\s?\(([^()]{1,200})\)", lambda m: f", {m.group(1)},", t, "kurung → koma")
            t = re.sub(r",\s*([.,!?])", r"\1", t)
            t = re.sub(r"\s+—\s+|\s+–\s+(?=[A-Za-z])", ", ", t)
        t = self.stage_0(t)
        t = self.stage_a(t)
        t = self.stage_b(t)
        t = self.stage_c(t)
        t = self._restore(t)
        t = re.sub(r"[ \t]{2,}", " ", t)
        t = re.sub(r" ,", ",", t)
        return t


def roman_to_int(s: str) -> int | None:
    vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}
    total, prev = 0, 0
    for ch in reversed(s):
        v = vals[ch]
        total = total - v if v < prev else total + v
        prev = max(prev, v)
    return total if 0 < total < 200 else None


def day_period(h: int) -> str:
    if h == 0 or h >= 18:
        return "malam"
    if h <= 3:
        return "dini hari"
    if h <= 10:
        return "pagi"
    if h <= 14:
        return "siang"
    return "sore"


def zone_spoken(z: str) -> str:
    return {"WIB": "we i be", "WITA": "wita", "WIT": "we i te"}[z]


def normalize(text: str, mode: str = "tts", time_style: str = "formal", include_unvalidated: bool = False, lexicon: dict | None = None) -> dict:
    n = Normalizer(lexicon or load_lexicon(), mode=mode, time_style=time_style, include_unvalidated=include_unvalidated)
    out = n.run(text)
    return {"input": text, "output": out, "changes": n.changes, "ragu": n.ragu, "notes": n.notes,
            "settings": {"mode": mode, "time_style": time_style, "include_unvalidated": include_unvalidated}}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("text", nargs="?", help="teks (jika kosong, dibaca dari stdin)")
    ap.add_argument("--mode", choices=["tts", "spoken"], default="tts")
    ap.add_argument("--time-style", choices=["formal", "casual"], default="formal")
    ap.add_argument("--include-unvalidated", action="store_true", help="ikut substitusi entri needs_validation")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    text = args.text if args.text is not None else sys.stdin.read()
    res = normalize(text, args.mode, args.time_style, args.include_unvalidated)
    if args.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0
    print("1. TEKS HASIL\n" + res["output"].strip() + "\n")
    print("2. TABEL PERUBAHAN\n| Asli | Jadi | Aturan |\n|---|---|---|")
    for c in res["changes"]:
        print(f"| {c['asli']} | {c['jadi']} | {c['aturan']}{' ' + c['entri'] if 'entri' in c else ''} |")
    print("\n3. RAGU")
    if not res["ragu"]:
        print("kosong")
    for r in res["ragu"]:
        print(f"- {r['token']}: {r['alasan']}")
    if res["notes"]:
        print("\nCatatan:")
        for n in res["notes"]:
            print(f"- {n['token']}: {n['catatan']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
