# Contoh: Istilah Teknologi, AI, dan Nama Merek

## 1. Istilah teruji di korpus VO (confidence `attested`)

**Input:** `Video Shorts pertama kami cuma dapat 900 views.`
**Teks hasil (tts):** `Video syorts pertama kami cuma dapat sembilan ratus views.`

| Asli | Jadi | Dasar |
|---|---|---|
| Shorts | syorts | `tech-0032` (HDI; Galeri Tes lolos) |
| 900 | sembilan ratus | aturan bilangan |

*views* tidak diubah: kata Inggris yang lazim bagi audiens dan dibaca benar oleh mesin.

**Input:** `Saya pakai AI untuk menulis naskah, lalu menyimpannya sebagai MP4.`

| Mode | Teks hasil |
|---|---|
| `tts` | Saya pakai **e ay** untuk menulis naskah, lalu menyimpannya sebagai **em pe empat**. |
| `spoken` | Saya pakai **ei ai** untuk menulis naskah, lalu menyimpannya sebagai **em pe empat**. |

*e ay* adalah respelling TTS dari korpus HDI (dipakai setelah satu suara ElevenLabs terdengar janggal membaca "AI"). Untuk ragam baku, varian *a i* (nama huruf Indonesia) tersedia. Caption tetap menulis **AI**.

## 2. Istilah belum tervalidasi (confidence `needs_validation`)

**Input:** `Model LLM kami di-fine-tune pakai PyTorch di GPU, lalu deploy ke server Docker.`

**Default (aman):**
`Model LLM kami di-fine-tune pakai PyTorch di GPU, lalu diploi ke server Docker.`
RAGU: `LLM` (usulan *el el em*), `GPU` (usulan *ji pi yu*) — ada di leksikon tetapi belum tervalidasi.

**Dengan izin pengguna (`--include-unvalidated`):**
`Model el el em kami di-fine-tune pakai pai torc di ji pi yu, lalu diploi ke server doker.`

**Pelajaran:** respelling `needs_validation` hanya dipakai bila pengguna mengizinkan atau mesin terbukti salah baca bentuk aslinya. *di-fine-tune* dibiarkan (kata Inggris berprefiks; tidak ada data).

## 3. Merek yang bertabrakan dengan kata Indonesia

| Tulisan | Konteks | Bacaan | Catatan |
|---|---|---|---|
| Keras | `import keras`, "model Keras" | [kɛras] (pustaka) | kata Indonesia *keras* = /kə.ras/ |
| CUDA | "GPU dengan CUDA" | kuda / ku-da | sama bunyi dengan *kuda* (hewan) |
| DANA | "bayar pakai DANA" | /da.na/ | dompet digital vs *dana* (anggaran) |
| Java | "belajar Java" | jawa / java | bahasa pemrograman vs pulau *Jawa* |
| Make | "otomasi dengan Make" | meik | platform vs kata kerja Inggris |
| X | "posting di X" | eks | platform vs huruf/variabel/tanda kali |

Semua ditandai `ambiguous: true`; skrip memasukkannya ke RAGU dan agen memutuskan dari konteks.

## 4. Format berkas dan alfanumerik

**Input:** `Kirim dokumennya dalam format PDF atau DOCX, lalu upload ke Drive.`
**Teks hasil:** `Kirim dokumennya dalam format pe de ef atau dok eks, lalu upload ke Drive.`
**RAGU:** `Drive` — Google Drive (*draiv*) atau penyimpanan umum. Dengan konteks "upload ke Drive" → Google Drive → *draiv*.

| Tulisan | Bacaan | Catatan |
|---|---|---|
| MP4 | em pe empat | angka dibaca Indonesia |
| 720p | tujuh ratus dua puluh pe | HDI menulis lengkap |
| 30 fps | tiga puluh ef pe es | satuan |
| 2FA | (RAGU) | Galeri Tes HDI: meragukan; padanan aman *autentikasi dua faktor* |
| n8n | en eit en | *needs_validation* |
| C++ / C# | si plas plas / si syarp | *needs_validation*; + dan # tidak dibaca "tambah"/"tagar" |

## 5. Domain dan surel

| Tulisan | Bacaan |
|---|---|
| konten.com | konten dot com (formal: konten titik com) |
| nama@gmail.com | nama et ji meil dot com |
| @hidupdariinternet (handle di narasi) | hidup dari internet |
