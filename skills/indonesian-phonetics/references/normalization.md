# Normalisasi Angka, Uang, Tanggal, Jam, Satuan, dan Simbol

Sumber: Sneddon dkk. (2010) untuk sistem bilangan; EYD V untuk penulisan angka; korpus & Galeri Tes HDI (2026) untuk perilaku TTS. Skrip `scripts/normalize.py` mengimplementasikan aturan bertanda ⚙.

## Daftar isi
1. Bilangan pokok · 2. Desimal & ribuan · 3. Uang · 4. Persen, kelipatan, rentang · 5. Ordinal & pecahan · 6. Telepon, kode, versi, tahun · 7. Tanggal · 8. Jam · 9. Satuan · 10. Simbol & tanda baca · 11. Teks TTS vs caption

## 1. Bilangan pokok ⚙
0 nol · 1 satu · 2 dua · 3 tiga · 4 empat · 5 lima · 6 enam · 7 tujuh · 8 delapan · 9 sembilan · 10 **se**puluh · 11 **se**belas · 12–19 *N* belas · 20–99 *N* puluh *M* · 100 **se**ratus · 1.000 **se**ribu · 10⁶ juta (1.000.000 = satu juta) · 10⁹ miliar (bukan milyar) · 10¹² triliun.
Contoh: 1.514 → seribu lima ratus empat belas; 1.250.000 → satu juta dua ratus lima puluh ribu.

**[Fakta — HDI]** Panduan produksi HDI (merujuk panduan resmi ElevenLabs) menyarankan angka ditulis sebagai kata di teks TTS, terutama untuk model multibahasa.

## 2. Desimal & ribuan ⚙
- Teks Indonesia: **titik = ribuan**, **koma = desimal**. 8.000 → delapan ribu; 0,7 → nol koma tujuh.
- Digit desimal dibaca satu per satu (konvensi repo): 3,14 → tiga koma satu empat. Varian: tiga koma empat belas.
- Titik yang **tidak** diikuti tepat 3 digit (1.5, 3.12) → bukan ribuan; bisa desimal gaya Inggris, versi, atau jam → **RAGU**.
- Teks Inggris "1,500" = 1500. Periksa bahasa dokumen.

## 3. Uang ⚙
Simbol ditulis **sebelum** angka tetapi dibaca **sesudah** bilangan:

| Tulisan | Ucapan |
|---|---|
| Rp25.000 | dua puluh lima ribu rupiah (Galeri HDI: kata "rupiah" berisiko terlewat bila tidak ditulis) |
| Rp 10.000,- | sepuluh ribu rupiah (",-" tidak dibaca) |
| Rp1,5 jt | satu setengah juta rupiah (Galeri HDI: "jt" salah baca) |
| Rp2-7 juta | dua sampai tujuh juta rupiah |
| Rp2 M | dua miliar rupiah (M = miliar dalam konteks rupiah) |
| $12 | dua belas dolar |
| US$5 | lima dolar Amerika |
| €10 / £10 | sepuluh euro / sepuluh pound sterling |
| USD 5 / 5 USD | lima dolar Amerika |
| ¥100 | **RAGU**: yen (Jepang) atau yuan (Tiongkok) |

*x,5 + besaran* lazim "x setengah": 1,5 juta → satu setengah juta; 0,5 juta → setengah juta.

## 4. Persen, kelipatan, rentang ⚙
- 4,2% → empat koma dua persen; 50 % → lima puluh persen.
- 2x / 10x → dua kali / sepuluh kali; 3 x 4 → tiga kali empat; 1920x1080 → … kali ….
- 10-15 / 10–15 → sepuluh sampai lima belas (formal: hingga).
- **Bukan rentang**: skor (2-1 → dua-satu / dua lawan satu), angka berawalan nol (kode), tanggal ISO → skrip menandai RAGU.
- Singkatan besaran: rb → ribu, jt → juta, M → miliar (Indonesia) / million (Inggris: RAGU), T → triliun, K → ribu (informal; "10K" → RAGU kecuali konteks jelas).

## 5. Ordinal & pecahan ⚙
- ke-2 → kedua; ke-11 → kesebelas; ke-21 → kedua puluh satu; *pertama* untuk urutan pertama (*kesatu* di penomoran formal).
- abad XXI → abad kedua puluh satu.
- 1/2 → setengah; 1/3 → sepertiga; 1/4 → seperempat; 3/4 → tiga perempat; 2/3 → dua pertiga (unsur *per-* serangkai, EYD).
- 1990-an → seribu sembilan ratus sembilan puluhan; 90-an → sembilan puluhan.

## 6. Telepon, kode, versi, tahun ⚙
- Telepon/NIK/rekening/kode: per digit, kelompok dipisah koma (jeda). 0812-3456-7890 → nol delapan satu dua, tiga empat lima enam, tujuh delapan sembilan nol. +62 → plus enam dua. Ragam santai: 0 → kosong.
- Versi: v2.5 → versi dua titik lima; "Python 3.12" tanpa "v" → RAGU (versi/desimal/jam).
- Nomor standar/model setelah singkatan (ISO 27001, SNI 7612, ISO/IEC 27001:2022): lazim per digit (dua tujuh nol nol satu) tetapi bervariasi → RAGU ⚙; tahun setelah ":" dibaca penuh.
- Kuartal Q1–Q4: "kuartal tiga" (formal) atau "kyu tiga" → RAGU ⚙.
- Tahun: bilangan penuh (2026 → dua ribu dua puluh enam; 1998 → seribu sembilan ratus sembilan puluh delapan). Santai: "tahun 98" → sembilan delapan.

## 7. Tanggal ⚙
- Urutan Indonesia **hari/bulan/tahun**; bulan diucapkan namanya: 1/2/2027 → satu Februari dua ribu dua puluh tujuh (Galeri HDI: bentuk garis miring salah baca).
- 2026-11-15 (ISO) → lima belas November dua ribu dua puluh enam.
- 1 Feb 2027 → satu Februari dua ribu dua puluh tujuh.
- Bulan > 12 (02/13/2027) → kemungkinan format AS → RAGU, jangan ubah. Tahun dua digit → RAGU.
- Angka tanggal = bilangan pokok: "tanggal 21" → tanggal dua puluh satu.
- Nama hari/bulan berhuruf kapital; *Minggu* (hari) vs *minggu* (pekan).

## 8. Jam ⚙
EYD memakai titik: 19.00. Skrip hanya mengubah jam bila didahului *pukul/jam* atau diikuti zona waktu; selain itu RAGU.

| Gaya | 19.00 WIB | 07.30 | 13.05 WITA |
|---|---|---|---|
| Formal (24 jam) | pukul sembilan belas we i be | pukul tujuh lewat tiga puluh menit | pukul tiga belas lewat lima menit wita |
| Santai (12 jam) | jam tujuh malam, we i be | jam setengah delapan pagi | jam satu lewat lima siang, wita |

- *setengah delapan* = 07.30 (bukan 08.30). *jam delapan kurang seperempat* = 07.45. *lewat seperempat* = :15.
- Penanda bagian hari (konvensi, bervariasi): dini hari 01–03, pagi 04–10, siang 11–14, sore 15–17, malam 18–24.
- Zona: WIB → we i be, WIT → we i te, WITA → wita (dibaca kata); formal: Waktu Indonesia Barat/Timur/Tengah. UTC → yu ti si.
- Rentang: 09.00–11.30 WIB → pukul sembilan sampai pukul sebelas lewat tiga puluh menit we i be ⚙.
- 24/7 → dua puluh empat jam sehari (aturan HDI).

## 9. Satuan ⚙
Angka + satuan → bilangan + nama satuan: 60 km/jam → enam puluh kilometer per jam; 5 kg → lima kilogram (santai: kilo); 30 fps → tiga puluh ef pe es; 25 °C → dua puluh lima derajat Celsius; 2 GB → dua gigabita (lazim: gigabait / ji bi).
**Ambigu**: "m" (meter/menit/juta), "ha" (hektare/interjeksi) → RAGU bila konteks tidak jelas.

## 10. Simbol & tanda baca
| Simbol | Default | Pengecualian |
|---|---|---|
| & | dan ⚙ | dalam singkatan Inggris: Q&A → kyu en ei |
| / | per (satuan: views/hari; rupiah/peserta) ⚙ | alternatif A/B, Bapak/Ibu → atau ⚙; dan/atau → dan atau; ISO/IEC, URL → RAGU (Galeri HDI: garis miring tidak dibaca mesin) |
| - | rentang: sampai ⚙; negatif: minus ⚙ | reduplikasi tidak dibaca; skor; kode |
| + | tambah ⚙ (di antara spasi) | plus: kode telepon, nama produk (C++ → si plas plas) |
| = | sama dengan ⚙ | — |
| ± | kurang lebih ⚙ (teks umum) | plus minus (galat ilmiah) |
| ~ | sekitar ⚙ (depan angka) | tilde (jalur file) |
| % | persen ⚙ | — |
| @ | et (surel) | handle di narasi: baca nama saja; harga satuan "@Rp5.000" → masing-masing |
| # | tagar (#kata) | #1 → nomor satu; C# → si syarp |
| ( ) | ganti koma ⚙ (mode tts) | isi kurung tetap utuh; jangan ubah kata |
| … | biarkan; jeda | dapat membuat suara ragu (HDI) |
| — – | koma/jeda ⚙ | – di antara angka = sampai |
| emoji, markdown, [VISUAL] | hapus dari teks TTS ⚙ (emoji) | — |
| ® ™ © | hapus/abaikan dalam narasi | © → hak cipta bila dibacakan |

## 11. Teks TTS vs caption
Simpan dua versi: **teks tampilan** (caption/layar, bentuk asli: "AI", "Shorts", "Rp25.000") dan **teks TTS** (bentuk ucapan: "e ay", "syorts", "dua puluh lima ribu rupiah"). Jika caption dihasilkan otomatis dari audio, petakan balik bentuk fonetik ke bentuk tulis (kamus balik) sebelum dipublikasikan.
