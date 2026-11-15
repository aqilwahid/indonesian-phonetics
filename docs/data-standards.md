# Standar Data

Dataset ada di [`dictionary/`](../dictionary/) (JSON, UTF-8). Skema: [`schemas/pronunciation.schema.json`](../schemas/pronunciation.schema.json) (JSON Schema 2020-12). Kosakata terkendali: [`dictionary/meta/taxonomy.json`](../dictionary/meta/taxonomy.json). Registri sumber: [`dictionary/meta/sources.json`](../dictionary/meta/sources.json).

## 1. Berkas

| Berkas | Prefix id | Kategori | Isi |
|---|---|---|---|
| `abbreviations.json` | `abbr` | alphabet, abbreviation | 26 nama huruf, singkatan bertitik, gelar, alamat, singkatan obrolan |
| `acronyms.json` | `acr` | acronym | initialism, akronim, alfanumerik (umum/kelembagaan/profesional/akademik) |
| `technology.json` | `tech` | technology | AI/ML, data, pemrograman, web, keamanan, format berkas, kreator, merek |
| `loanwords.json` | `loan` | loanword | kata Inggris, serapan berejaan Indonesia, serapan Arab/Belanda/daerah |
| `numbers.json` | `num` | number, currency, unit | leksem bilangan, pola normalisasi, mata uang, satuan |
| `symbols.json` | `sym` | symbol | simbol dan tanda baca |
| `dates-and-times.json` | `dt` | date-time | bulan, hari, zona waktu, format tanggal/jam |
| `pronunciation-dictionary.json` | `word` | general | homograf, kualitas *e*, glotal, digraf, bentuk informal, istilah akademik, nama diri |

Setiap berkas: `{ "$schema", "dataset", "version", "description", "entries": [...] }`.

## 2. Field entri

| Field | Wajib | Tipe | Keterangan |
|---|---|---|---|
| `id` | ya | string | `prefix-NNNN`, unik global, berurutan dalam berkas |
| `text` | ya | string | Bentuk tulis asli (seperti di layar/caption). Untuk `entry_type: pattern`, berisi label pola |
| `normalized_text` | ya | string | Kunci cari: NFC + huruf kecil + spasi tunggal (`normalize_key()`) |
| `spoken_form` | ya | string | Bacaan default dalam ejaan biasa = keluaran *text normalization*. Bentuk dalam kurung, mis. `(jeda)`, adalah instruksi, bukan teks ucapan |
| `respelling` | ya (nullable) | string/null | Ejaan bantu untuk mesin TTS jika berbeda dari `spoken_form` |
| `ipa` | ya (nullable) | string/null | IPA fonemis `/.../`; **null jika tidak didukung data** |
| `ipa_note` | tidak | string | Alasan IPA kosong atau catatan transkripsi |
| `language` | ya | string | Bahasa asal bentuk tulis (kode di taxonomy) |
| `category`, `subcategory` | ya | string | Lihat taxonomy |
| `entry_type` | ya | enum | `lexical`, `pattern`, `example` |
| `reading_type` | tidak | enum | `letter-by-letter`, `word`, `mixed`, `expansion`, `context-dependent` |
| `letter_system` | tidak | enum | `id`, `en`, `mixed`, `na` |
| `register` | ya | enum | `formal`, `neutral`, `informal`, `technical` |
| `context` | tidak | string | Kapan bacaan default berlaku |
| `variants` | ya | array | Bacaan alternatif (lihat §3) |
| `ambiguous` + `disambiguation` | tidak (berpasangan) | bool + string | Wajib untuk entri yang maknanya/bacaannya bergantung konteks |
| `pattern` + `examples` | wajib untuk `pattern` | regex + array | Regex sintaks Python/JS; setiap contoh wajib cocok |
| `source` | ya | array | Id dari `sources.json` |
| `provenance` | ya | enum | Diturunkan dari jenis sumber entri + varian (divalidasi) |
| `confidence` | ya | enum | Lihat §4 |
| `review_status` | ya | enum | `unreviewed` / `reviewed` |
| `tts_notes` | tidak | string | Observasi spesifik mesin TTS (sebut mesin, suara, tanggal) |
| `notes` | ya | string | Catatan bebas (boleh kosong) |
| `related`, `tags` | tidak | array | Rujukan id lain; label bebas kebab-case |

### Contoh entri

```json
{
  "id": "tech-0001",
  "text": "AI",
  "normalized_text": "ai",
  "spoken_form": "ei ai",
  "respelling": "e ay",
  "ipa": null,
  "language": "en",
  "category": "technology",
  "subcategory": "ai-ml",
  "entry_type": "lexical",
  "reading_type": "letter-by-letter",
  "letter_system": "en",
  "register": "technical",
  "variants": [
    {"spoken_form": "a i", "ipa": "/a i/", "register": "formal", "letter_system": "id",
     "context": "Nama huruf Indonesia; ragam formal/baku", "source": ["hdi-kamus-2026", "hdi-galeri-2026", "hdi-toolkit-2026"]}
  ],
  "source": ["hdi-kamus-2026", "hdi-galeri-2026", "hdi-toolkit-2026"],
  "provenance": "zip-reference",
  "confidence": "attested",
  "review_status": "unreviewed",
  "tts_notes": "Galeri Tes HDI 27 Okt 2026: …",
  "notes": "Artificial intelligence …"
}
```

## 3. Varian

| Field | Keterangan |
|---|---|
| `spoken_form` (wajib) | Bacaan alternatif |
| `context` (wajib) | Kapan varian dipakai |
| `source` (wajib) | Sumber varian (bisa berbeda dari entri utama) |
| `respelling`, `ipa`, `register`, `letter_system`, `region` | Opsional |
| `meaning_changing` | `true` bila varian menandai makna lain (homograf/rujukan berbeda) |

## 4. Tingkat keyakinan (`confidence`)

| Nilai | Arti | Syarat sumber |
|---|---|---|
| `standard` | Didokumentasikan di sumber normatif (EYD/PUEBI, KBBI, lembaga resmi) | minimal satu sumber `external` |
| `attested` | Terbukti dipakai dalam praktik nyata yang tercatat (mis. korpus VO HDI) | sumber ZIP atau eksternal |
| `derived` | Diturunkan sistematis dari aturan terdokumentasi (nama huruf, sistem bilangan, ejaan baku) | bebas |
| `needs_validation` | Belum pasti, sumber lemah, atau interpretasi | bebas |

**Penting:** `confidence` ≠ validasi linguistik. Semua entri saat ini `review_status: unreviewed`. Sumber yang tidak dibuka saat build ditandai `accessed_in_build: false` di `sources.json`.

## 5. Provenance

| Nilai | Arti |
|---|---|
| `zip-reference` | Semua sumber (entri + varian) dari materi ZIP HDI |
| `external-source` | Semua sumber dari literatur/lembaga eksternal |
| `interpretation` | Hanya interpretasi maintainer |
| `mixed` | Gabungan |

Validator menghitung ulang provenance dari sumber dan menolak nilai yang tidak cocok.

## 6. Konvensi teks

- **IPA**: fonemis, titik suku kata, tanpa tekanan, `/k/` akhir, lihat [ipa.md](ipa.md).
- **Respelling**: ejaan Indonesia sebagai alat bantu mesin TTS: `c` = /tʃ/, `j` = /dʒ/, `y` = /j/, `sy` = /ʃ/, `ny` = /ɲ/, `ng` = /ŋ/, `ai/au/ei` = diftong. Keterbatasan: huruf `e` tetap ambigu (/e/ atau /ə/); diakritik PUEBI (é/ê) hanya dipakai pada varian homograf. Respelling yang berasal dari HDI dipertahankan apa adanya karena teruji pada mesin tertentu.
- **Nama huruf Inggris (kanonik repo)**: A ei, B bi, C si, D di, E i, F ef, G ji, H eic, I ai, J jei, K kei, L el, M em, N en, O o, P pi, Q kyu, R ar, S es, T ti, U yu, V vi, W dabelyu, X eks, Y wai, Z zet.
- **Kapitalisasi**: `text` peka huruf besar (*HP* ≠ *hp*, *Dr.* ≠ *dr.*). Pencocokan longgar memakai `normalized_text`.

## 7. Aturan integritas (divalidasi otomatis)

1. JSON valid dan sesuai skema (`scripts/validate-data.py`).
2. Id unik, prefix sesuai berkas, berurutan (`scripts/validate-dictionary.py`).
3. Kategori/subkategori/bahasa sesuai taxonomy.
4. `normalized_text` = `normalize_key(text)`.
5. Tidak ada duplikat `text` dalam satu berkas, tidak ada duplikat `text + category` lintas berkas, tidak ada duplikat isi (`normalized_text + category + spoken_form`).
6. Semua sumber terdaftar; provenance konsisten; syarat sumber per `confidence` terpenuhi.
7. IPA memakai simbol yang diizinkan, diapit `/ /`, tanpa alofon/huruf ortografis.
8. Homograf: `ambiguous: true` dan ≥ 2 varian `meaning_changing`.
9. Regex pola valid dan semua contoh cocok.
10. `skills/indonesian-phonetics/assets/lexicon.json` sinkron dengan `dictionary/` (`scripts/build-skill-assets.py --check`).

## 8. Memakai dataset

### Python

```python
import json, pathlib
entries = []
for f in sorted(pathlib.Path("dictionary").glob("*.json")):
    entries += json.loads(f.read_text(encoding="utf-8"))["entries"]

by_text = {}
for e in entries:
    by_text.setdefault(e["text"], []).append(e)

hp = by_text["HP"][0]
print(hp["spoken_form"], hp.get("ambiguous"), hp["disambiguation"])
```

### JavaScript (Node.js)

```js
import { readFileSync, readdirSync } from "node:fs";
const entries = readdirSync("dictionary")
  .filter((f) => f.endsWith(".json"))
  .flatMap((f) => JSON.parse(readFileSync(`dictionary/${f}`, "utf8")).entries);

const tts = (text) => {
  const e = entries.find((x) => x.text === text && !x.ambiguous);
  return e ? (e.respelling ?? e.spoken_form) : null; // null = tangani dengan aturan atau tandai ragu
};
console.log(tts("Shorts")); // "syorts"
```

Pola (`entry_type: "pattern"`) memakai sintaks regex yang kompatibel Python `re` dan JavaScript (tanpa grup bernama Python-only). Lookbehind dipakai di beberapa pola; didukung Node.js ≥ 10.

## 9. Versi

Setiap berkas memiliki `version` (SemVer). Naikkan *minor* saat menambah entri, *major* saat mengubah skema atau makna field. Catat di [CHANGELOG.md](../CHANGELOG.md).
