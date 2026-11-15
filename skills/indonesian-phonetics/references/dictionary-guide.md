# Panduan Leksikon

`assets/lexicon.json` adalah gabungan 8 berkas dataset repositori (dibangkitkan otomatis; jangan diedit). Struktur: `{about, version, generated_from, entry_count, sources, entries[]}`. Setiap entri punya field tambahan `dataset`.

## Dataset dan isinya
| dataset | Isi | Contoh |
|---|---|---|
| abbreviations | nama huruf, singkatan bertitik, gelar, alamat, obrolan | dll., S.Kom., Jl., yg |
| acronyms | initialism, akronim, alfanumerik | KTP, Polri, QRIS, A4 |
| technology | AI/ML, data, kode, web, keamanan, format berkas, kreator, merek | AI, CTR, Shorts, JSON |
| loanwords | kata Inggris, serapan, Arab/Belanda/daerah | prewed, kualitas, khusus |
| numbers | bilangan, pola, mata uang, satuan | Rp, %, km, 720p |
| symbols | simbol & tanda baca | &, /, ±, @ |
| dates-and-times | bulan, hari, zona, format | Februari, WIB, 24/7 |
| pronunciation-dictionary | homograf, kualitas e, glotal, informal, nama diri | teras, saat, nggak |

## Field yang dipakai agen
| Field | Pakai untuk |
|---|---|
| `text` | Pencocokan **peka huruf besar** (HP ≠ hp; Dr. ≠ dr.) |
| `normalized_text` | Pencocokan longgar (huruf kecil) bila pencocokan persis gagal |
| `spoken_form` | Keluaran mode *spoken*; bentuk dalam kurung, mis. `(jeda)`, adalah instruksi |
| `respelling` | Keluaran mode *tts* bila tidak null |
| `ipa` | IPA fonemis; null = jangan ditebak |
| `variants[]` | Alternatif; `meaning_changing: true` = makna berbeda |
| `ambiguous` + `disambiguation` | Wajib cek konteks |
| `entry_type: pattern` + `pattern` + `examples` | Pola produktif (regex) dengan contoh keluaran |
| `confidence` | `standard` / `attested` / `derived`: boleh dipakai langsung. `needs_validation`: usulkan, tandai |
| `tts_notes` | Bukti perilaku mesin TTS tertentu (bukan aturan bahasa) |
| `source` | Id sumber; `hdi-*` = korpus VO HDI 2026 (praktik ElevenLabs), `puebi-2015`/`eyd-v-2022`/`kbbi-daring` = normatif, `maintainer-interpretation` = interpretasi |
| `review_status` | Saat ini semua `unreviewed` |

## Mencari tanpa skrip
- Cari string `"text":"HP"` di `assets/lexicon.json` (berkas JSON satu baris; gunakan pencarian teks biasa).
- Untuk kata Indonesia, cari `"normalized_text":"kata"`.
- Pola: cari `"entry_type":"pattern"` lalu baca `examples`.

## Dengan skrip
```bash
python scripts/lookup.py HP
python scripts/lookup.py --search kecap
python scripts/lookup.py --scan "Saya pakai AI untuk bikin Shorts, CTR naik 4,2%."
python scripts/normalize.py --time-style casual "Live 19.00 WIB, harga Rp25.000."
```

## Kamus rumah pengguna
Jika pengguna memberi daftar `tulisan = bacaan`, daftar itu **mengalahkan** leksikon. Contoh: pengguna ingin "AI" selalu dibaca "a i" → pakai "a i" walau leksikon menyarankan "ei ai"/"e ay". Catat di tabel perubahan dengan dasar "kamus pengguna".

## Menambah pengetahuan
Bacaan baru yang ditemukan saat bekerja **jangan** ditulis ke `assets/lexicon.json`. Sarankan pengguna menambahkannya ke `dictionary/*.json` di repositori sesuai CONTRIBUTING.md (dengan sumber dan confidence), lalu menjalankan `scripts/build-skill-assets.py`.
