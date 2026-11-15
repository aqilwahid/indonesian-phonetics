# Contoh: Angka, Uang, Tanggal, Jam, dan Satuan

Semua baris di bawah adalah keluaran nyata `skills/indonesian-phonetics/scripts/normalize.py` (gaya jam `formal` kecuali disebut) dan sebagian besar diuji di `tests/pronunciation-tests.json`.

## Bilangan

| Input | Output |
|---|---|
| Sebanyak 12 peserta | Sebanyak dua belas peserta |
| Total 1.514 kata | Total seribu lima ratus empat belas kata |
| Nilainya 0,7 | Nilainya nol koma tujuh |
| 2x lebih cepat | dua kali lebih cepat |
| 3 x 4 | tiga kali empat |
| 10-15 menit | sepuluh sampai lima belas menit |
| -5 | minus lima |
| ±10 menit | kurang lebih sepuluh menit |
| 50rb | lima puluh ribu |

## Uang

| Input | Output | Catatan |
|---|---|---|
| Rp25.000 | dua puluh lima ribu rupiah | Galeri HDI: "rupiah" berisiko terlewat jika tidak ditulis |
| Rp 10.000,- | sepuluh ribu rupiah | ",-" tidak dibaca |
| Rp1,5 jt | satu setengah juta rupiah | Galeri HDI: "jt" salah baca |
| Rp2-7 juta | dua sampai tujuh juta rupiah | |
| Rp2 M | dua miliar rupiah | M = miliar dalam rupiah |
| $12 | dua belas dolar | |
| US$5 | lima dolar Amerika | |
| €10 | sepuluh euro | |
| USD 5 | lima dolar Amerika | |
| ¥100 | ¥100 → **RAGU** | yen atau yuan |

## Persen, ordinal, pecahan

| Input | Output |
|---|---|
| 4,2% | empat koma dua persen |
| ke-2 | kedua |
| ke-21 | kedua puluh satu |
| abad XXI | abad kedua puluh satu |
| 1/2 | setengah |
| 3/4 | tiga perempat |
| 1990-an | seribu sembilan ratus sembilan puluhan |

## Telepon, versi

| Input | Output |
|---|---|
| 0812-3456-7890 | nol delapan satu dua, tiga empat lima enam, tujuh delapan sembilan nol |
| +62 812 3456 7890 | plus enam dua, delapan satu dua, tiga empat lima enam, tujuh delapan sembilan nol |
| v2.5 | versi dua titik lima |
| Python 3.12 | **RAGU** (versi, desimal, atau jam?) |
| ISO/IEC 27001:2022 | **RAGU** (nomor standar: per digit atau bilangan?) |
| Q3 2026 | **RAGU** untuk Q3 (kuartal tiga / kyu tiga); 2026 → dua ribu dua puluh enam |

## Tanggal

| Input | Output |
|---|---|
| 1/2/2027 | satu Februari dua ribu dua puluh tujuh (asumsi hari/bulan/tahun dicatat) |
| 2026-11-15 | lima belas November dua ribu dua puluh enam |
| 1 Feb 2027 | satu Februari dua ribu dua puluh tujuh |
| 02/13/2027 | **RAGU** — bulan > 12, kemungkinan format AS; tidak diubah |
| 1/2/27 | **RAGU** — tahun dua digit |

## Jam

| Input | Formal | Santai (`--time-style casual`) |
|---|---|---|
| 19.00 WIB | pukul sembilan belas we i be | jam tujuh malam, we i be |
| pukul 07.30 | pukul tujuh lewat tiga puluh menit | jam setengah delapan pagi |
| jam 13.05 WITA | jam tiga belas lewat lima menit wita | jam satu lewat lima siang, wita |
| 09.00–11.30 WIB | pukul sembilan sampai pukul sebelas lewat tiga puluh menit we i be | jam sembilan pagi sampai jam setengah dua belas siang, we i be |
| 19.00 (tanpa *pukul*/zona) | **RAGU** | **RAGU** |

## Satuan

| Input | Output |
|---|---|
| 60 km/jam | enam puluh kilometer per jam |
| 25 °C | dua puluh lima derajat Celsius |
| 2 GB | dua gigabita (bacaan umum: gigabait) |
| 30 fps | tiga puluh ef pe es |
| 5 m | **RAGU** — meter, menit, atau juta? |

## Kasus yang sengaja tidak diubah

| Input | Alasan |
|---|---|
| Skor 2-1 | angka kedua lebih kecil → bukan rentang (skor?) |
| Kode 0812-3456 | diawali nol → kode/nomor |
| 1.5 juta | titik + 1 digit bukan pemisah ribuan Indonesia |
| 10K | gabungan angka-huruf tak dikenal |

Token RAGU **dilindungi utuh** — tidak ada konversi sebagian seperti "dua-1".
