# Contoh: Singkatan, Akronim, dan Initialism

Keluaran normalisasi dihasilkan dengan `python skills/indonesian-phonetics/scripts/normalize.py "<teks>"` (mode `tts`, default).

## 1. Initialism Indonesia (nama huruf Indonesia)

**Input:** `Urus KTP dan NPWP dulu.`
**Teks hasil:** `Urus ka te pe dan en pe we pe dulu.`

| Asli | Jadi | Dasar | Keyakinan |
|---|---|---|---|
| KTP | ka te pe | `acr-0011` | attested |
| NPWP | en pe we pe | `acr-0036` (nama huruf PUEBI) | derived |

## 2. Initialism Inggris di domain kreator

**Input:** `Bulan ini CTR kanal kita 4,2%.`
**Teks hasil:** `Bulan ini si ti ar kanal kita empat koma dua persen.`

Bacaan *si ti ar* teramati di korpus VO HDI dan lolos Galeri Tes 27 Okt 2026 (`tech-0005`).

## 3. Campuran sistem huruf

| Tulisan | Bacaan | Sistem | Catatan |
|---|---|---|---|
| FAQ | ef a kyu | campuran | A dibaca Indonesia, Q dibaca Inggris (HDI) |
| ER | i er | campuran | engagement rate |
| API | a pe i | Indonesia | varian Inggris: ei pi ai |
| CPM | si pi em | Inggris | HDI juga memakai *se pe em* (C = "se") |
| AC | a se | campuran | *needs_validation*; warisan nama huruf Belanda |

**Prinsip:** pilih satu bacaan per singkatan dan konsisten sepanjang dokumen.

## 4. Akronim dibaca sebagai kata

| Tulisan | Bacaan | Teknik TTS |
|---|---|---|
| NIK | nik | tulis huruf kecil di teks TTS agar tidak dieja (HDI) |
| SIM | sim | idem |
| QRIS | kris | bacaan yang dikampanyekan Bank Indonesia |
| Polri | polri | — |

## 5. Singkatan bertitik

**Input:** `Siapkan tripod, lampu, dll. Lalu rekam.`
**Teks hasil:** `Siapkan tripod, lampu, dan lain-lain. Lalu rekam.`

Titik singkatan sekaligus akhir kalimat dipertahankan. Galeri Tes HDI mencatat *dll.* terbaca seperti kata "dil" bila tidak diekspansi.

**Input:** `Lihat No. 5 di daftar.` → `Lihat nomor lima di daftar.` (aturan konteks: *No.* + angka)

## 6. Singkatan ambigu → RAGU

**Input:** `Cek notifikasi lewat HP kamu, terus pindahkan foto ke SD card.`
**Teks hasil:** `Cek notifikasi lewat HP kamu, terus pindahkan foto ke SD card.` (tidak diubah oleh skrip)

**RAGU dari skrip:**
- `HP` — telepon / merek / horsepower / health points.
- `SD` — sekolah dasar ("es de") / kartu memori ("es di").

**Keputusan agen dengan konteks:** "notifikasi lewat HP kamu" → telepon → *ha pe* (atau *hape*); "SD card" → kartu memori → *es di card*. Catat keduanya di tabel perubahan sebagai keputusan konteks.

## 7. Singkatan tidak dikenal

**Input:** `Kami pakai XYZQ untuk deploy.`
**Teks hasil:** `Kami pakai XYZQ untuk diploi.`
**RAGU:** `XYZQ` — tidak dikenal leksikon: dieja atau dibaca sebagai kata? Konfirmasi ke pengguna. Agen **tidak** menebak.

## 8. Gelar akademik

| Tulisan | Pengumuman lisan | Upacara resmi |
|---|---|---|
| S.Kom. | es kom | sarjana komputer |
| M.T. | em te | magister teknik |
| Dr. | doktor | doktor |
| dr. | dokter | dokter |

Konvensi gelar berstatus *needs_validation* di dataset; skrip tidak mengubahnya otomatis.
