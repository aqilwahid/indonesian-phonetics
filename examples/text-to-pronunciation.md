# Contoh End-to-End: Naskah → Teks Ucapan

Contoh ini menunjukkan alur kerja lengkap skill: skrip mengerjakan bagian deterministik, agen menyelesaikan ambiguitas dengan konteks, dan keraguan dilaporkan.

## Input (naskah YouTube santai)

```text
Halo, gue mau bahas cara bikin Shorts pakai AI. Live-nya mulai 19.00 WIB tanggal 1/2/2027.
Target CTR minimal 4,2%, RPM sekitar Rp15.000 (tergantung niche). Siapkan HP, tripod, lampu, dll.
Info lengkap di konten.com atau DM gue.
```

Permintaan: teks untuk TTS (ElevenLabs), gaya jam santai.

## Langkah 1 — Skrip

```bash
python skills/indonesian-phonetics/scripts/normalize.py --time-style casual "<naskah>"
```

Keluaran skrip:

```text
Halo, gue mau bahas cara bikin syorts pakai e ay. Live-nya mulai jam tujuh malam, we i be tanggal satu Februari dua ribu dua puluh tujuh. Target si ti ar minimal empat koma dua persen, RPM sekitar lima belas ribu rupiah, tergantung niche. Siapkan HP, tripod, lampu, dan lain-lain. Info lengkap di konten dot com atau di em gue.
```

RAGU dari skrip: `RPM` (monetisasi atau mesin?), `HP` (telepon, merek, horsepower, gim?). Catatan: `1/2/2027` diasumsikan hari/bulan/tahun.

## Langkah 2 — Agen menyelesaikan dengan konteks

| Token | Konteks | Keputusan |
|---|---|---|
| RPM | berdampingan dengan CTR, topik YouTube | metrik monetisasi → *ar pi em* |
| HP | daftar peralatan rekaman ("HP, tripod, lampu") | telepon → *ha pe* |
| we i be tanggal | jeda kurang jelas | tambahkan koma setelah zona waktu (tanda baca, bukan kata) |

## Langkah 3 — Jawaban akhir (format skill)

**1. TEKS HASIL**

```text
Halo, gue mau bahas cara bikin syorts pakai e ay. Live-nya mulai jam tujuh malam, we i be, tanggal satu Februari dua ribu dua puluh tujuh. Target si ti ar minimal empat koma dua persen, ar pi em sekitar lima belas ribu rupiah, tergantung niche. Siapkan ha pe, tripod, lampu, dan lain-lain. Info lengkap di konten dot com atau di em gue.
```

**2. TABEL PERUBAHAN**

| Asli | Jadi | Dasar | Keyakinan |
|---|---|---|---|
| Shorts | syorts | tech-0032 | attested |
| AI | e ay | tech-0001 (respelling TTS) | attested |
| 19.00 WIB | jam tujuh malam, we i be, | aturan jam santai + dt-0038 | attested |
| 1/2/2027 | satu Februari dua ribu dua puluh tujuh | aturan tanggal (asumsi h/b/t) | attested |
| CTR | si ti ar | tech-0005 | attested |
| 4,2% | empat koma dua persen | aturan persen | attested |
| RPM | ar pi em | tech-0006 + konteks YouTube | attested (keputusan konteks) |
| Rp15.000 | lima belas ribu rupiah | aturan rupiah | attested |
| (tergantung niche) | , tergantung niche | kurung → koma | derived |
| HP | ha pe | acr-0001 + konteks peralatan | attested (keputusan konteks) |
| dll. | dan lain-lain | abbr-0027 | standard |
| konten.com | konten dot com | tech-0069 | attested |
| DM | di em | tech-0002 | attested |

**3. RAGU**

- *niche* — kata Inggris tanpa entri leksikon; dibiarkan. Jika mesin salah baca, pertimbangkan respelling (mis. "nis" atau "nich") setelah dikonfirmasi pengguna.
- *Live-nya* — dibiarkan; bacaan Inggris "laiv" lazim, tidak ada data leksikon.

## Variasi permintaan

**Target `spoken` (normalisasi untuk caption suara/ASR):** sama, kecuali *AI* → **ei ai** (spoken_form), bukan *e ay*.

**Teks tampilan/caption:** **tidak diubah** — tetap "Shorts", "AI", "19.00 WIB", "Rp15.000". Jika caption dibuat otomatis dari audio, petakan balik bentuk fonetik (*syorts* → Shorts, *e ay* → AI, *si ti ar* → CTR).

**Target `ipa` untuk "siapin HP":** *siapin* (bentuk informal bersufiks *-in*) tidak ada di leksikon, tetapi IPA dapat disusun karena ejaannya transparan dan tanpa *e*: /si.a.pin/; *HP* (telepon, nama huruf Indonesia) → /ha pe/. Kata dengan *e* yang tidak ada di leksikon → "IPA tidak tersedia".

**Pengguna memberi kamus rumah** `AI = a i`: kamus rumah menang → *a i* di seluruh teks; dasar di tabel = "kamus pengguna".
