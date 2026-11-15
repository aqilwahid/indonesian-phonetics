# Analisis Materi Referensi ZIP

Dokumen ini mencatat isi berkas ZIP yang dipakai sebagai *seed/reference material*, keputusan normalisasi, dan batasan pemakaiannya. Tujuannya menjaga **provenance**: setiap data yang diadopsi dari ZIP bisa ditelusuri, dan setiap perubahan atas data itu terdokumentasi.

## 1. Inventaris

| Berkas | Isi | Dipakai di repo? |
|---|---|---|
| `Ebook - Voice Over AI pakai ElevenLabs.pdf` | Panduan VO 12 bab (Edisi Okt 2026). Relevan: Bab 05 (9 aturan menulis teks fonetik, kamus ringkas 40 entri, prompt P1) dan Bab 06 (Galeri Salah Baca). | Prinsip diringkas dengan kata-kata sendiri. Teks tidak disalin. |
| `Kamus Fonetik HDI - ….xlsx` | Tab *Mulai* (petunjuk + asal data), *Kamus* (153 entri), *Galeri Tes* (18 tes), *Kamus Saya* (kosong). | Pasangan tulisan→bacaan diadopsi sebagai fakta. Catatan ditulis ulang. |
| `Kalkulator Kredit VO - ….xlsx` | Kalkulator kredit/durasi ElevenLabs, paket harga, log generate. | **Tidak relevan** untuk fonetik; tidak diadopsi. Hanya angka 6,3 karakter/kata dan ±150 kata/menit dicatat di sini sebagai konteks produksi. |
| `Toolkit VO - ….zip` (berisi `vo_toolkit/`) | 4 skrip Python (generate, gabung, SRT, loudnorm), `config.py`, contoh naskah dan hasil tes. | Hanya konsep **kamus balik caption** (`CAPTION_BALIK`): bentuk fonetik tidak boleh bocor ke caption. Kode tidak disertakan. |

**Lisensi.** Ebook menyatakan: "© 2026 Hidup dari Internet. Ebook, Sheet, dan toolkit ini buat dipakai sendiri. Tolong jangan disebar ulang atau dijual lagi." Karena itu repo ini (disetujui pemilik repo):

- mengadopsi **fakta** pasangan tulisan→bacaan dan hasil tes (lolos/meragukan/salah baca);
- **tidak** menyalin catatan secara verbatim, jumlah pemakaian ("Dipakai"), transkrip Galeri Tes, teks prompt P1, maupun berkas PDF/XLSX/MP3/kode;
- mencantumkan sumber di setiap entri (`hdi-kamus-2026`, `hdi-galeri-2026`, `hdi-ebook-2026`, `hdi-toolkit-2026`; lihat [sources.md](sources.md)).

## 2. Struktur Kamus HDI

Kolom: No, Tulisan (di layar), Dibaca (teks fonetik), Kategori, Sumber, Dipakai, Catatan.

| Kategori HDI | Jumlah | Dipetakan ke |
|---|---|---|
| Singkatan huruf | 70 | `acronyms.json`, `technology.json` (initialism teknologi/kreator), `numbers.json` (dB, fps, LUFS, 720p, USD), `dates-and-times.json` (WIB/WIT/WITA/UTC), `abbreviations.json` (huruf B) |
| Istilah YouTube | 24 | `technology.json` (content-creator), `loanwords.json` (Viewer, Owner, Manager, Commenter, Geography) |
| Nama tool & merek | 22 | `technology.json`, `symbols.json` (@handle) |
| Kata Inggris | 13 | `loanwords.json`, `technology.json` (CONFIG, CHANGELOG, innerHTML, textContent), `acronyms.json` (di-DM) |
| Angka & uang | 10 | `numbers.json` (contoh di entri pola) |
| Simbol & tanda baca | 10 | `symbols.json`, `abbreviations.json` (dll., dsb., No., e.g., i.e., vs) |
| Tanggal & jam | 4 | `dates-and-times.json` |

Sumber internal HDI: *VO channel HDI* (125 entri, bacaan yang benar-benar dipakai), *Aturan HDI* (11), *Tes Pratama 27 Okt 2026* (10), *Kamus skrip VO HDI* (7).

Cakupan: **153/153 entri** terwakili. Dua entri dipecah/dinormalisasi: `( ... )` menjadi entri simbol `( )`, dan `e.g. / i.e.` menjadi dua entri terpisah. Pemeriksaan cakupan dilakukan dengan skrip sekali-jalan terhadap berkas asli (tidak disertakan karena berkas asli tidak boleh didistribusikan). Total **171 entri** repo merujuk sumber HDI (termasuk varian pada entri lain, mis. huruf V dengan varian "fe").

## 3. Galeri Tes (18 kalimat, 27 Okt 2026)

Metode HDI: setiap kalimat di-generate dua versi (tulisan biasa vs teks fonetik) dengan ElevenLabs Multilingual v2, suara "Pratama", lalu ditranskripsi Whisper dua kali; label SALAH BACA hanya bila kedua transkrip meleset.

| Hasil | Jumlah | Kasus |
|---|---|---|
| SALAH BACA | 5 | `Rp1,5 jt` (jt), `1/2/2027`, `19.00 WIB`, `Views/hari`, `dll.` |
| MERAGUKAN | 2 | `Rp25.000` (kata "rupiah" mungkin terlewat), `2FA` |
| LOLOS | 10 | CTR + 4,2%, YPP + 4.000, Shorts + 3, HP, 10x, MP4, AdSense, 720p, vs, kurung |
| KASUS ASLI | 1 | AI (pernah terdengar janggal di naskah panjang) |

Hasil ini disimpan di field `tts_notes` entri terkait dan menjadi dasar kasus uji di `tests/pronunciation-tests.json`. **Batasan:** satu mesin, satu suara, satu tanggal, transkripsi otomatis. Ini bukti observasional TTS, bukan aturan bahasa.

## 4. Inkonsistensi yang ditemukan dan resolusinya

| Temuan | Contoh | Resolusi di repo |
|---|---|---|
| Sistem nama huruf bercampur (Indonesia vs Inggris) tanpa aturan eksplisit | `KTP` = ka te pe, `CTR` = si ti ar, `API` = a pe i, `FAQ` = ef a kyu | Field `letter_system` (`id`/`en`/`mixed`). Bacaan HDI tetap jadi `spoken_form`; sistem lain dicatat sebagai varian. Aturan umum dirumuskan di [pronunciation-rules.md](pronunciation-rules.md#4-singkatan-akronim-dan-initialism). |
| Ejaan huruf A versi Inggris tidak seragam | `AI` = "e ay", `CTA` = "si ti e", `Q&A` = "kyu en ei", `QA` = "kyu ey" | Kanonik repo: **ei**. Bentuk HDI dipertahankan di `respelling` (karena itu yang teruji di TTS). |
| Satu kata, dua cara tulis | HP = ha pe / hape; CPM = se pe em / si pi em; HTML = ha te em el / eich ti em el; YPP = wai pi pi / ye pe pe | Satu bentuk utama + varian bersumber HDI. Prinsip HDI "pilih satu dan konsisten" diadopsi sebagai prinsip skill. |
| Nama huruf C versi Belanda | CPM = **se** pe em, CER = **se** e er | Didokumentasikan sebagai varian `mixed` (warisan nama huruf Belanda; bandingkan "AC" = a se). |
| Huruf V dibaca [f] | HVS = ha **fe** es | PUEBI menulis pengucapan V "vé"; repo mencatat "fe" sebagai varian realisasi umum. |
| Ortografi respelling tidak konsisten | `Checks` = "cheks" (ch) vs `Super Chat` = "super cet" (c) | Konvensi repo: `c` = /tʃ/. Bentuk HDI dipertahankan apa adanya di `respelling` dengan catatan. |
| Duplikat beda kapitalisasi | `Konten.com` / `konten.com` | Digabung menjadi satu entri `konten.com`. |
| Entri tanpa keterangan makna | `AIR` = eir, `CER` = se e er, `SAL` = es a el | `confidence: needs_validation`; `AIR` ditandai ambigu (bisa kata Indonesia *air*). |
| Contoh yang mengubah kata | Kurung: "Pakai median (bukan rata-rata) ya." → HDI: "Pakai median, **jangan** rata-rata, ya." | Bertentangan dengan aturan HDI sendiri ("jangan ubah isi"). Repo hanya mengubah tanda baca: "Pakai median, bukan rata-rata, ya." |
| Kebiasaan rumah dianggap aturan | `AI` = "e ay" karena satu suara tertentu terdengar janggal | Dicatat sebagai `respelling` + `tts_notes` khusus mesin; bacaan baku Indonesia "a i" dicatat sebagai varian formal. |

## 5. Prinsip ZIP yang diadopsi (diringkas)

Dari Bab 05 ebook (sumber `hdi-ebook-2026`), dirumuskan ulang sebagai prinsip skill:

1. Pisahkan **teks tampilan** (caption/layar) dari **teks ucapan** (TTS). Teks ucapan tidak boleh bocor ke caption (konsep kamus balik di toolkit).
2. Angka, uang (dengan satuan), tanggal, dan jam ditulis seperti diucapkan.
3. Singkatan yang dieja ditulis bunyi hurufnya; kata asing yang sering meleset ditulis bunyinya.
4. Simbol (/, &, vs, dll.) diganti kata; kurung diganti koma.
5. Kalimat pendek; salah ketik ikut terbaca.
6. **Jangan menebak**: kata yang ragu dibiarkan dan dimasukkan ke daftar RAGU.
7. Laporan perubahan berbentuk tabel Asli | Jadi | Aturan.

Yang **tidak** diadopsi sebagai norma: pilihan respelling khusus satu suara, paket harga/kredit, pengaturan stability/similarity, dan klaim tentang perilaku normalisasi otomatis ElevenLabs (tidak diverifikasi ke dokumentasi resmi dalam build ini).
