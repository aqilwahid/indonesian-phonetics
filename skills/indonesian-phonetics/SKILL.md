---
name: indonesian-phonetics
description: Interpretasi pelafalan bahasa Indonesia untuk TTS, voice-over, text normalization, dan transkripsi IPA. Gunakan saat mengubah naskah atau teks berbahasa Indonesia menjadi teks siap-ucap (angka, uang, persen, tanggal, jam, singkatan, akronim, istilah asing/teknologi, nama merek, simbol), saat menjelaskan cara membaca kata, membuat IPA, atau memeriksa ambiguitas lafal seperti homograf e pepet/taling. Use for Indonesian pronunciation, TTS/ElevenLabs script preparation, phonetic respelling, text normalization, and IPA.
license: MIT untuk skrip, CC BY 4.0 untuk data (lihat LICENSE di repositori)
compatibility: Skrip opsional membutuhkan Python 3.9+ (pustaka standar saja). Tanpa Python, baca references/ dan assets/lexicon.json secara langsung.
metadata:
  version: "1.0.0"
  repository: "https://github.com/aqilwahid/indonesian-phonetics"
  language: "id"
---

# Indonesian Phonetics

Skill ini membantu mengubah teks bahasa Indonesia menjadi bentuk ucapan yang benar, konsisten, dan jujur terhadap ketidakpastian — untuk mesin TTS, naskah voice-over, normalisasi teks, dan transkripsi IPA.

## Prinsip (wajib)

1. **Pertahankan makna dan gaya.** Hanya ubah *cara tulis*, bukan isi, urutan, pilihan kata, atau ragam (santai/formal). Jangan mengganti *pake* dengan *pakai* atau *upload* dengan *unggah* kecuali diminta.
2. **Peka konteks.** Bacaan singkatan, simbol, angka, dan homograf ditentukan konteks kalimat dan domain.
3. **Konsisten.** Satu bentuk tulis → satu bacaan sepanjang dokumen. Catat pilihan Anda di glosarium kerja.
4. **Aturan dulu, kamus untuk pengecualian.** Pakai aturan terdokumentasi untuk pola produktif (angka, tanggal, initialism Indonesia); pakai leksikon untuk pengecualian dan istilah.
5. **Jangan mengarang.** Jika tidak ada dasar (leksikon, aturan, atau konteks tegas), biarkan bentuk asli dan masukkan ke daftar **RAGU**. Jangan mengisi IPA dengan tebakan.
6. **Pisahkan teks tampilan dan teks ucapan.** Respelling TTS (*e ay*, *syorts*) tidak boleh masuk caption/teks layar; caption memakai bentuk tulis asli.
7. **Sebut tingkat keyakinan.** Bedakan bacaan baku (`standard`), teramati (`attested`), turunan aturan (`derived`), dan perlu validasi (`needs_validation`).

## Alur kerja

1. **Tentukan target keluaran** dari permintaan pengguna:
   - `tts` — teks untuk mesin TTS (pakai `respelling` bila ada);
   - `spoken` — normalisasi teks dalam ejaan biasa (pakai `spoken_form`);
   - `ipa` — transkripsi fonemis;
   - `explain` — penjelasan cara baca/aturan.
   Tentukan juga ragam (formal/santai), gaya jam (formal `pukul 19.00` → "pukul sembilan belas"; santai → "jam tujuh malam"), dan kamus rumah pengguna jika diberikan.
2. **Pindai teks** untuk menemukan bagian yang perlu interpretasi: angka, uang, persen, tanggal, jam, nomor telepon, satuan, singkatan/akronim, huruf kapital beruntun, campuran angka-huruf, kata asing/merek, simbol (`/ & + % @ # ± ~ -`), kurung, emoji, homograf. Jika bisa menjalankan Python: `python scripts/lookup.py --scan "<teks>"`.
3. **Selesaikan setiap token** dengan urutan prioritas:
   1. Kamus rumah/instruksi pengguna (mengalahkan semua yang lain).
   2. Entri leksikon yang **tidak ambigu** (`assets/lexicon.json`; `python scripts/lookup.py <token>`).
   3. Aturan terdokumentasi di `references/`.
   4. Konteks kalimat untuk entri ambigu (`disambiguation` di leksikon; [references/ambiguity-and-variation.md](references/ambiguity-and-variation.md)).
   5. Jika masih ragu → **jangan ubah**, masukkan ke RAGU dengan alasannya.
4. **Normalisasi angka, uang, tanggal, jam, simbol** sesuai [references/normalization.md](references/normalization.md). Skrip `python scripts/normalize.py "<teks>"` melakukan bagian yang deterministik dan mengeluarkan daftar RAGU; tinjau hasilnya, jangan diterima mentah.
5. **Rapikan untuk TTS** (target `tts`): kurung → koma, hapus emoji/markdown/catatan editor, pecah kalimat > ±25 kata di batas klausa tanpa menambah kata.
6. **IPA** (target `ipa`): pakai IPA leksikon; atau susun dari aturan hanya bila ejaan transparan dan kualitas setiap *e* diketahui. Ikuti [references/ipa-reference.md](references/ipa-reference.md). Jika tidak pasti, tulis "IPA tidak tersedia" — jangan menebak.
7. **Periksa ulang**: makna utuh, konsistensi bacaan, tidak ada respelling di teks tampilan, semua keraguan tercatat.

## Format keluaran default

Untuk permintaan konversi teks, jawab dengan tiga bagian:

1. **TEKS HASIL** — siap ditempel (paragraf dipisah baris kosong).
2. **TABEL PERUBAHAN** — `| Asli | Jadi | Dasar | Keyakinan |` (Dasar = id entri leksikon atau nama aturan).
3. **RAGU** — token yang dibiarkan + alasan + pertanyaan spesifik untuk pengguna; tulis "kosong" jika tidak ada.

Untuk target `ipa`, tambahkan kolom IPA dan tandai sumbernya (leksikon/aturan). Untuk `explain`, jelaskan aturan dengan label **[Fakta]**, **[Variasi]**, atau **[Rekomendasi]**.

## Peta referensi (baca sesuai kebutuhan)

| Kebutuhan | Berkas |
|---|---|
| Sistem bunyi: vokal, konsonan, alofon, diftong, suku kata, tekanan, intonasi | [references/phonetics.md](references/phonetics.md) |
| Membaca huruf/kombinasi huruf, huruf *e*, singkatan & initialism, kata serapan, ejaan lama | [references/pronunciation-rules.md](references/pronunciation-rules.md) |
| Angka, uang, persen, rentang, tanggal, jam, satuan, simbol, tanda baca | [references/normalization.md](references/normalization.md) |
| Homograf, singkatan ambigu, ragam, variasi daerah, protokol RAGU | [references/ambiguity-and-variation.md](references/ambiguity-and-variation.md) |
| Simbol IPA, konvensi, menyusun IPA singkatan | [references/ipa-reference.md](references/ipa-reference.md) |
| Struktur leksikon, arti field/keyakinan, cara mencari tanpa skrip | [references/dictionary-guide.md](references/dictionary-guide.md) |

## Skrip (opsional)

| Skrip | Fungsi |
|---|---|
| `scripts/lookup.py TOKEN` | Cari entri (peka huruf besar, lalu longgar). `--search` cari substring, `--scan` pindai teks, `--json` keluaran mesin |
| `scripts/normalize.py "TEKS"` | Normalisasi deterministik. `--mode tts|spoken`, `--time-style formal|casual`, `--json` |

Skrip tidak mengganti entri ambigu atau `needs_validation`; keduanya muncul di RAGU. Keputusan akhir tetap pada Anda dan konteks.

## Contoh

**Input (target tts, gaya santai):** `Webinar mulai 19.00 WIB. Biayanya Rp25.000 (sudah termasuk sertifikat).`

**Output:**
1. TEKS HASIL: `Webinar mulai jam tujuh malam, we i be. Biayanya dua puluh lima ribu rupiah, sudah termasuk sertifikat.`
2. TABEL PERUBAHAN:

| Asli | Jadi | Dasar | Keyakinan |
|---|---|---|---|
| 19.00 WIB | jam tujuh malam, we i be | aturan jam santai (dt-0046) + WIB (dt-0038) | attested |
| Rp25.000 | dua puluh lima ribu rupiah | aturan rupiah | attested |
| (sudah termasuk sertifikat) | , sudah termasuk sertifikat | kurung → koma | derived |

3. RAGU: kosong

**Input:** `Buka dashboard, cek CTR & RPM, lalu kirim CV ke HRD.`

**Output (ringkas):** `Buka dashboard, cek si ti ar dan ar pi em, lalu kirim CV ke HRD.` — *RPM* ambigu, tetapi konteks *dashboard* + *CTR* menunjukkan metrik monetisasi YouTube → "ar pi em" (catat di tabel sebagai keputusan konteks). RAGU: **CV** (curriculum vitae → "si vi", atau badan usaha → "se ve"? Konteks "kirim ke HRD" menunjukkan lamaran kerja → sarankan "si vi", minta konfirmasi); **HRD** (`needs_validation`; lazim "ha er de"); **dashboard** (`needs_validation`; respelling "desbor" belum tervalidasi, biarkan jika mesin membacanya benar). *&* di antara kata → "dan".

**Input (target ipa):** `teras`

**Output:** homograf — *téras* /te.ras/ (bagian depan rumah) atau *têras* /tə.ras/ (inti; "pejabat teras"). Tanpa konteks, tidak ada IPA tunggal.

Contoh lebih banyak: folder `examples/` di repositori.

## Jangan

- Jangan menebak kualitas *e*, ekspansi singkatan tak dikenal, atau bacaan merek baru.
- Jangan mengubah istilah, gaya bahasa, atau urutan kalimat.
- Jangan menyebut data ini "tervalidasi linguis": seluruh entri berstatus `unreviewed`.
- Jangan menyamakan satu logat daerah dengan standar nasional.
