# Daftar Sumber

Dokumen ini adalah versi baca-manusia dari [`dictionary/meta/sources.json`](../dictionary/meta/sources.json). Setiap entri dataset merujuk `id` di bawah melalui field `source`.

Kolom **Dibuka saat build** jujur menyatakan apakah sumber dibuka langsung ketika repo dibangun. Sumber bertanda *tidak* dikutip dari literatur yang dikenal dan **wajib dicek reviewer** sebelum entri terkait dinaikkan ke `review_status: reviewed`.

## Referensi ZIP

### `hdi-kamus-2026`

- **Judul:** Kamus Fonetik HDI buat ElevenLabs (Sheet pendamping ebook Voice Over AI pakai ElevenLabs), tab Kamus, 153 entri
- **Penulis/penerbit:** Hidup dari Internet (@hidupdariinternet) (2026)
- **Lisensi/ketentuan:** © 2026 Hidup dari Internet. Untuk pemakaian pribadi; tidak boleh disebar ulang atau dijual. Repo ini hanya mengadopsi fakta pasangan tulisan→bacaan; catatan ditulis ulang, berkas asli tidak disertakan.
- **Dibuka saat build:** ya
- **Catatan:** Sumber internal kolom Sumber pada sheet: 'VO channel HDI' (bacaan yang benar-benar dipakai di VO channel, Okt 2026), 'Kamus skrip VO HDI' (daftar substitusi di program VO), 'Aturan HDI' (aturan rumah). Berlaku untuk suara ElevenLabs 'Pratama', model Multilingual v2; bukan norma bahasa baku.

### `hdi-ebook-2026`

- **Judul:** Voice Over AI pakai ElevenLabs: Dari Naskah sampai Caption Tanpa Ngoding, Edisi Oktober 2026 (Bab 05 'Nulis Teks buat AI', Bab 06 'Galeri Salah Baca')
- **Penulis/penerbit:** Hidup dari Internet (@hidupdariinternet) (2026)
- **Lisensi/ketentuan:** © 2026 Hidup dari Internet. Pemakaian pribadi; tidak disebar ulang. Hanya prinsip dan fakta yang diringkas dengan kata-kata sendiri.
- **Dibuka saat build:** ya
- **Catatan:** Memuat 9 aturan menulis teks fonetik untuk TTS (angka jadi kata, uang lengkap dengan satuan, tanggal/jam seperti diucapkan, singkatan dieja, simbol jadi kata, kurung jadi koma, kalimat pendek, cek salah ketik) dan prinsip 'jangan menebak, masukkan ke daftar ragu'.

### `hdi-galeri-2026`

- **Judul:** Galeri Tes Salah Baca, 18 kalimat, 27 Oktober 2026 (ElevenLabs Multilingual v2, suara Pratama, stability 50, similarity 75; dicek dengan transkripsi Whisper dua kali)
- **Penulis/penerbit:** Hidup dari Internet (@hidupdariinternet) (2026)
- **Lisensi/ketentuan:** © 2026 Hidup dari Internet. Hanya ringkasan hasil (lolos/meragukan/salah baca) yang dirujuk; transkrip dan audio tidak disalin.
- **Dibuka saat build:** ya
- **Catatan:** Bukti observasional satu mesin TTS, satu suara, satu tanggal. Hasil bisa berbeda antar-generate, suara, dan model.

### `hdi-toolkit-2026`

- **Judul:** Toolkit VO (config.py: kamus balik caption CAPTION_BALIK)
- **Penulis/penerbit:** Hidup dari Internet (@hidupdariinternet) (2026)
- **Lisensi/ketentuan:** © 2026 Hidup dari Internet. Kode tidak disertakan; hanya konsep pemetaan balik bentuk fonetik → bentuk tulis untuk caption.
- **Dibuka saat build:** ya
- **Catatan:** Konsep 'reverse map' dipakai di skill: teks TTS tidak boleh bocor ke caption/teks layar.

## Eksternal

### `eyd-v-2022`

- **Judul:** [Ejaan Bahasa Indonesia yang Disempurnakan (EYD) Edisi V](https://ejaan.kemdikbud.go.id/)
- **Penulis/penerbit:** Badan Pengembangan dan Pembinaan Bahasa, Kemendikbudristek (2022)
- **Lisensi/ketentuan:** Dokumen pemerintah; dikutip untuk rujukan.
- **Dibuka saat build:** ya
- **Catatan:** Diakses lewat ringkasan sekunder (tirto.id) untuk diftong ai/au/ei/oi, gabungan konsonan kh/ng/ny/sy, monoftong eu, dan diakritik ê. Teks lengkap wajib dicek di situs resmi.

### `puebi-2015`

- **Judul:** [Pedoman Umum Ejaan Bahasa Indonesia (PUEBI), Lampiran Permendikbud No. 50 Tahun 2015](https://lmsspada.kemdikbud.go.id/pluginfile.php/45217/mod_page/content/2/BAB%20II.pdf)
- **Penulis/penerbit:** Badan Pengembangan dan Pembinaan Bahasa, Kemendikbud (2015)
- **Lisensi/ketentuan:** Dokumen pemerintah; dikutip untuk rujukan.
- **Dibuka saat build:** ya
- **Catatan:** Sumber tabel nama huruf beserta pengucapan (B 'bé', F 'èf', Q 'ki', V 'vé', X 'èks', Z 'zèt'), diakritik é/è/ê (contoh téras, kécap, sèri/sêri, kêcap), dan aturan pemenggalan kata. Telah digantikan EYD V (2022); bagian yang dirujuk perlu dicocokkan ulang dengan EYD V.

### `kbbi-daring`

- **Judul:** [Kamus Besar Bahasa Indonesia (KBBI) Daring, Edisi VI](https://kbbi.kemdikbud.go.id/)
- **Penulis/penerbit:** Badan Pengembangan dan Pembinaan Bahasa (2023)
- **Lisensi/ketentuan:** Rujukan; isi kamus tidak disalin.
- **Dibuka saat build:** tidak — perlu dicek
- **Catatan:** Dirujuk untuk penanda lafal homograf (é/ê) dan bentuk baku kata serapan. Tidak dibuka langsung saat build (akses dibatasi); setiap entri yang merujuk sumber ini WAJIB dicek reviewer.

### `pupi-2007`

- **Judul:** Pedoman Umum Pembentukan Istilah, Edisi Ketiga
- **Penulis/penerbit:** Pusat Bahasa, Departemen Pendidikan Nasional (2007)
- **Lisensi/ketentuan:** Dokumen pemerintah; dikutip untuk rujukan.
- **Dibuka saat build:** tidak — perlu dicek
- **Catatan:** Kaidah penyesuaian ejaan unsur serapan (c→k/s, ph→f, th→t, -tion→-si, -ty→-tas, dsb.).

### `soderberg-olson-2008`

- **Judul:** [Indonesian (Illustrations of the IPA). Journal of the International Phonetic Association 38(2): 209–213](https://www.cambridge.org/core/journals/journal-of-the-international-phonetic-association/article/indonesian/AE405481B94A4E0B7234A8BBE9C6F5FD)
- **Penulis/penerbit:** Craig D. Soderberg; Kenneth S. Olson (2008)
- **Lisensi/ketentuan:** Rujukan akademik.
- **Dibuka saat build:** ya
- **Catatan:** Metadata dikonfirmasi via PHOIBLE (inventaris PH 1144: diftong ai̯ au̯ oi̯). Rujukan utama inventaris vokal/konsonan dan alofon.

### `alwi-tbbi-2017`

- **Judul:** Tata Bahasa Baku Bahasa Indonesia, Edisi Keempat
- **Penulis/penerbit:** Hasan Alwi; Soenjono Dardjowidjojo; Hans Lapoliwa; Anton M. Moeliono (2017)
- **Lisensi/ketentuan:** Rujukan akademik.
- **Dibuka saat build:** tidak — perlu dicek
- **Catatan:** Rujukan fonem, pola suku kata (V, VK, KV, KVK, KKV, KKVK, KVKK, KKKV, KKKVK, KKVKK, KVKKK), dan proses morfofonemik meN-/peN-.

### `chaer-2009`

- **Judul:** Fonologi Bahasa Indonesia
- **Penulis/penerbit:** Abdul Chaer (2009)
- **Lisensi/ketentuan:** Rujukan akademik.
- **Dibuka saat build:** tidak — perlu dicek
- **Catatan:** Rujukan konsep fonetik artikulatoris, fonem/alofon, dan variasi bunyi.

### `muslich-2008`

- **Judul:** Fonologi Bahasa Indonesia: Tinjauan Deskriptif Sistem Bunyi Bahasa Indonesia
- **Penulis/penerbit:** Masnur Muslich (2008)
- **Lisensi/ketentuan:** Rujukan akademik.
- **Dibuka saat build:** tidak — perlu dicek
- **Catatan:** Rujukan distribusi alofon dan fonotaktik.

### `sneddon-2010`

- **Judul:** Indonesian: A Comprehensive Grammar, 2nd edition
- **Penulis/penerbit:** James Neil Sneddon; Alexander Adelaar; Dwi Noverini Djenar; Michael C. Ewing (2010)
- **Lisensi/ketentuan:** Rujukan akademik.
- **Dibuka saat build:** tidak — perlu dicek
- **Catatan:** Rujukan fonologi, ragam formal vs informal, dan bilangan.

### `sneddon-2006`

- **Judul:** Colloquial Jakartan Indonesian (Pacific Linguistics 581)
- **Penulis/penerbit:** James Neil Sneddon (2006)
- **Lisensi/ketentuan:** Rujukan akademik.
- **Dibuka saat build:** tidak — perlu dicek
- **Catatan:** Rujukan bentuk informal Jakarta (pakai→pake, sampai→sampe, -kan→-in).

### `cohn-1989`

- **Judul:** Stress in Indonesian and bracketing paradoxes. Natural Language & Linguistic Theory 7: 167–216
- **Penulis/penerbit:** Abigail C. Cohn (1989)
- **Lisensi/ketentuan:** Rujukan akademik.
- **Dibuka saat build:** tidak — perlu dicek
- **Catatan:** Analisis tekanan penultima dengan pergeseran bila penultima berisi schwa.

### `goedemans-vanzanten-2007`

- **Judul:** [Stress and accent in Indonesian. In V. J. van Heuven & E. van Zanten (eds.), Prosody in Indonesian Languages (LOT Occasional Series 9), 35–62](https://hdl.handle.net/11245/1.275780)
- **Penulis/penerbit:** Rob Goedemans; Ellen van Zanten (2007)
- **Lisensi/ketentuan:** Rujukan akademik.
- **Dibuka saat build:** ya
- **Catatan:** Metadata dikonfirmasi (UvA DARE). Rujukan untuk temuan bahwa tekanan kata dalam bahasa Indonesia lemah/diperdebatkan dan prominensi lebih banyak ditentukan di tingkat frasa.

### `ipa-handbook-1999`

- **Judul:** Handbook of the International Phonetic Association
- **Penulis/penerbit:** International Phonetic Association (1999)
- **Lisensi/ketentuan:** Rujukan akademik.
- **Dibuka saat build:** tidak — perlu dicek
- **Catatan:** Konvensi notasi IPA: /.../ fonemis, [...] fonetis, titik sebagai batas suku kata.

### `ipa-chart-2020`

- **Judul:** [The International Phonetic Alphabet (revised to 2020)](https://www.internationalphoneticassociation.org/content/ipa-chart)
- **Penulis/penerbit:** International Phonetic Association (2020)
- **Lisensi/ketentuan:** CC BY-SA 3.0 (bagan tidak disertakan di repo).
- **Dibuka saat build:** tidak — perlu dicek
- **Catatan:** Set simbol IPA yang diizinkan validator.

### `iso-4217`

- **Judul:** [ISO 4217 Currency codes](https://www.iso.org/iso-4217-currency-codes.html)
- **Penulis/penerbit:** International Organization for Standardization (2015)
- **Lisensi/ketentuan:** Rujukan standar.
- **Dibuka saat build:** tidak — perlu dicek
- **Catatan:** Kode mata uang IDR, USD, EUR, JPY, GBP, SGD, MYR.

### `bi-qris`

- **Judul:** [QRIS (Quick Response Code Indonesian Standard), materi publik Bank Indonesia](https://www.bi.go.id/id/fungsi-utama/sistem-pembayaran/ritel/kanal-layanan/qris/default.aspx)
- **Penulis/penerbit:** Bank Indonesia (2019)
- **Lisensi/ketentuan:** Rujukan.
- **Dibuka saat build:** tidak — perlu dicek
- **Catatan:** Materi kampanye BI menyebut QRIS dibaca 'KRIS'. Perlu dicek ulang.

### `agentskills-spec`

- **Judul:** [Agent Skills Specification](https://agentskills.io/specification)
- **Penulis/penerbit:** agentskills.io (2026)
- **Lisensi/ketentuan:** Rujukan.
- **Dibuka saat build:** ya
- **Catatan:** Aturan frontmatter SKILL.md (name, description, license, compatibility, metadata), struktur scripts/references/assets, progressive disclosure (< 500 baris).

## Interpretasi

### `maintainer-interpretation`

- **Judul:** Interpretasi dan rekomendasi maintainer repo indonesian-phonetics
- **Penulis/penerbit:** Kontributor indonesian-phonetics (2026)
- **Lisensi/ketentuan:** CC BY 4.0 (mengikuti lisensi data repo).
- **Dibuka saat build:** ya
- **Catatan:** Dipakai untuk rekomendasi praktis, konsolidasi variasi, dan bacaan yang diturunkan dari aturan. Selalu disertai confidence yang sesuai; bukan klaim norma baku.
