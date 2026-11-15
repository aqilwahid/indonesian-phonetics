# Aturan Pelafalan

> Aturan membaca tulisan bahasa Indonesia, termasuk singkatan, kata serapan, dan pengecualian. Label: **[Fakta]** · **[Variasi]** · **[Rekomendasi]**. Kode sumber merujuk [sources.md](sources.md).

## 1. Hubungan grafem–fonem

**[Fakta]** Tabel dasar (`eyd-v-2022`, `puebi-2015`, `soderberg-olson-2008`). Kolom *Catatan* memuat pengecualian.

| Grafem | Fonem | Contoh | Catatan |
|---|---|---|---|
| a | /a/ | *apa* | — |
| b | /b/ | *baru* | akhir kata → [p]: *sebab* |
| c | /tʃ/ | *cari* | tidak pernah /k/ atau /s/ dalam kata Indonesia |
| d | /d/ | *dua* | akhir kata → [t]: *abad* |
| e | /e/ **atau** /ə/ | *enak* /e/, *besar* /ə/ | leksikal; lihat §2 |
| f | /f/ | *fakta* | [p] pada sebagian penutur |
| g | /g/ | *gula* | — |
| h | /h/ | *hari* | sering lesap antarvokal berbeda pada ragam santai |
| i | /i/ | *ini* | [ɪ] di suku akhir tertutup |
| j | /dʒ/ | *jalan* | — |
| k | /k/ | *kaki* | akhir suku kata asli → [ʔ] |
| kh | /x/ | *khusus* | [k]/[h] pada sebagian penutur |
| l, m, n, r, s, t, w | /l m n r s t w/ | — | — |
| ng | /ŋ/ | *bangun* | satu bunyi |
| ngg | /ŋg/ | *mangga* | dua bunyi lintas suku |
| ny | /ɲ/ | *nyanyi* | tidak di akhir kata |
| o | /o/ | *obat* | [ɔ] di suku tertutup |
| p | /p/ | *pagi* | tak beraspirasi |
| q | /k/ (/q/ ragam keagamaan) | *Al-Qur'an* | — |
| sy | /ʃ/ | *syarat* | [s] pada sebagian penutur |
| u | /u/ | *ular* | [ʊ] di suku akhir tertutup |
| v | /v/ ~ [f] | *video* | realisasi [f] sangat umum |
| x | /ks/; awal kata [s] | *sinar-X* | jarang di kata umum |
| y | /j/ | *yang* | — |
| z | /z/ | *zaman* | [dʒ]/[s] pada sebagian penutur |
| ai, au, oi, ei | diftong | *pantai, pulau, koboi, survei* | bisa juga hiatus (*main*) |
| eu | monoftong [ɘ] | *seudati* | serapan daerah (EYD V) |
| ' | /ʔ/ | *Al-Qur'an* | — |

## 2. Huruf *e*

**[Fakta]** Tidak ada aturan ejaan yang menentukan /e/ vs /ə/. Kecenderungan:

1. Prefiks *ber-, ter-, me(N)-, pe(N)-, ke-, se-* → /ə/.
2. Suku akhir terbuka kata asli → /e/ (*sate, tempe, sore*).
3. Serapan Eropa cenderung /e/ (*sistem, efektif*), kecuali suku akhir *-el/-er* serapan Belanda yang sering /ə/ (*wortel, dokter*).
4. Homograf harus diselesaikan dari konteks (lihat [pronunciation-dictionary.json](../dictionary/pronunciation-dictionary.json)).

**[Rekomendasi]** Untuk TTS: cek leksikon; untuk homograf, beri konteks kalimat atau gunakan diakritik PUEBI (é/è/ê) hanya bila mesin mendukung.

## 3. Ejaan lama dalam nama diri

**[Fakta]** Nama diri boleh mempertahankan ejaan lama; bacaannya mengikuti bunyi modern:

| Ejaan lama | Bunyi | Contoh |
|---|---|---|
| oe | /u/ | *Soekarno* /su.kar.no/ |
| dj | /dʒ/ | *Gadjah Mada* /ga.dʒah ma.da/ |
| tj | /tʃ/ | *Tjahaja* → cahaya |
| j (lama) | /j/ | *Soerabaja* → Surabaya (huruf *j* modern = /dʒ/) |
| nj | /ɲ/ | *Njonja* → nyonya |
| sj | /ʃ/ | *Sjahrir* |
| ch | /x/ | *Chairil* |

**[Rekomendasi]** Jangan mengubah ejaan nama diri di teks tampilan. Untuk TTS, beri respelling modern bila mesin salah baca.

## 4. Singkatan, akronim, dan initialism

### 4.1 Jenis

| Jenis | Cara baca | Contoh |
|---|---|---|
| **Initialism** | dieja per huruf | *KTP* → ka te pe |
| **Akronim** | dibaca sebagai kata | *Polri* → polri, *NIK* → nik |
| **Campuran/alfanumerik** | sebagian dieja, sebagian dibaca | *MP4* → em pe empat, *B2B* → bi tu bi |
| **Singkatan bertitik** | diekspansi | *dll.* → dan lain-lain, *a.n.* → atas nama |

### 4.2 Sistem nama huruf

**[Fakta]** Nama huruf baku: tabel PUEBI (lihat [ipa.md](ipa.md#4-menyusun-ipa-untuk-singkatan)). Q = **ki**, V = **ve** (sering direalisasikan **fe**), X = **eks**, Y = **ye**, Z = **zet**.

**[Fakta — ZIP, observasi]** Korpus VO HDI (`hdi-kamus-2026`) menunjukkan pola nyata yang tidak seragam:

- Initialism asal Indonesia **selalu** dieja nama huruf Indonesia (*KTP, UMKM, THR*).
- Initialism asal Inggris **bervariasi**: sebagian nama huruf Inggris (*CTR* = si ti ar, *CEO* = si i o, *DM* = di em), sebagian nama huruf Indonesia (*PDF* = pe de ef, *API* = a pe i, *SMS* = es em es, *ATM* = a te em), sebagian campuran (*FAQ* = ef a kyu, *ER* = i er).
- Huruf C kadang dibaca **se** (warisan nama huruf Belanda): *CPM* = se pe em; bandingkan *AC* = a se.

**[Rekomendasi]** Aturan keputusan untuk agen/TTS:

1. Jika ada di leksikon → pakai `spoken_form` (atau `respelling` untuk teks TTS).
2. Initialism asal Indonesia → nama huruf Indonesia (keyakinan tinggi, `derived`).
3. Initialism asal Inggris tanpa data → ikuti kebiasaan domain jika diketahui; jika tidak, nama huruf Indonesia untuk ragam formal, dan **tandai** sebagai ragu.
4. Singkatan yang mungkin dibaca sebagai kata (≤ 4 huruf, pola KVK/KVKV) → jangan menebak; tandai.
5. Pilih satu bacaan per singkatan dan konsisten sepanjang dokumen.

### 4.3 Teknik TTS dari korpus ZIP

**[Fakta — ZIP]** Akronim yang harus dibaca sebagai kata ditulis huruf kecil di teks TTS agar mesin tidak mengeja (*nik, sim, zip*) (`hdi-kamus-2026`).

## 5. Kata serapan

### 5.1 Penyesuaian ejaan (bacaan mengikuti ejaan Indonesia)

**[Fakta]** Kaidah penyesuaian unsur serapan (`pupi-2007`); setelah disesuaikan, kata dibaca menurut ejaan Indonesia:

| Asing | Indonesia | Contoh |
|---|---|---|
| c (di depan a, u, o, konsonan) | k | *computer* → *komputer* |
| c (di depan e, i) | s | *central* → *sentral* |
| ph | f | *photo* → *foto* |
| th | t | *theory* → *teori* |
| ck | k | *check* → *cek* |
| -tion | -si | *information* → *informasi* |
| -ty | -tas | *quality* → *kualitas* |
| -ive | -if | *effective* → *efektif* |
| -ic, -ical | -ik, -is | *electronic* → *elektronik*; *practical* → *praktis* |
| x | ks | *taxi* → *taksi* |
| q | k | *aquarium* → *akuarium* |

Bentuk baku lain yang sering keliru: *analisis* (bukan analisa), *praktik* (bukan praktek), *risiko* (bukan resiko), *sistem*, *standar*, *objek*, *survei*, *karier*, *apotek*, *kuitansi* (lihat `loanwords.json`).

**[Variasi]** Gugus *ku-/kua-/kui-* lazim dilafalkan dengan luncuran [w]: *kualitas* [kwalitas], *kuitansi* [kwitansi]. Ejaan baku tetap *ku-*.

### 5.2 Kata asing yang tidak diserap ejaannya

**[Fakta — ZIP, observasi]** Kata Inggris yang dipakai apa adanya dibaca dengan pelafalan Inggris yang diadaptasi penutur Indonesia, dan mesin TTS sering salah karena membaca menurut ejaan Indonesia atau terlalu "kebarat-baratan" (`hdi-kamus-2026`, `hdi-galeri-2026`). Contoh respelling teruji: *Shorts* → syorts, *AdSense* → ed sens, *Reels* → rils, *deploy* → diploi.

**[Rekomendasi]**
- Kata Inggris yang sudah lazim di audiens (*upload, views, thumbnail*) boleh dibiarkan bila mesin membacanya benar.
- Ganti dengan respelling hanya bila terbukti salah baca atau tercatat di leksikon.
- Padanan Indonesia (*unggah, tagar, daring*) adalah pilihan **penulis naskah**; skill tidak boleh mengganti kata tanpa diminta.

### 5.3 Serapan Arab dan Belanda

**[Fakta]** Serapan Arab membawa /x ʃ z f q ʔ/: *khusus, syukur, zakat, fajar, Al-Qur'an, maaf* /ma.ʔaf/. Serapan Belanda membawa gugus dan suku *-el/-er* dengan schwa: *wortel* /wor.təl/, *knalpot*. Lihat `loanwords.json` subkategori `arabic` dan `dutch`.

## 6. Pengaruh bahasa asing terhadap pelafalan

| Pengaruh | Wujud | Contoh |
|---|---|---|
| Inggris | Nama huruf Inggris pada initialism; kata Inggris tanpa penyesuaian; angka Inggris dalam singkatan | *CTR* = si ti ar; *2FA* = tu ef a |
| Belanda | Nama huruf C = se; suku *-er/-el* schwa; gugus konsonan | *AC* = a se; *dokter* |
| Arab | Fonem /x ʃ z q ʔ/, apostrof | *khusus*, *Jumat* [dʒumʔat] |
| Bahasa daerah | Lihat [regional-variations.md](../knowledge/regional-variations.md) | — |

## 7. Variasi yang diterima

**[Rekomendasi]** Variasi berikut diterima dan dicatat sebagai varian, bukan kesalahan: /v/→[f]; bacaan initialism Indonesia vs Inggris yang sama-sama lazim (*HTML*); bentuk informal di ragam santai (*nggak, pake*); bacaan *meme* [meme] atau [mim]; *Wi-Fi* [wifi] atau [waifai]. Variasi yang **berisiko mengubah makna** (lihat [regional-variations.md](../knowledge/regional-variations.md#1-perbedaan-yang-tidak-mengubah-makna-vs-yang-berisiko-mengubah-makna)) tidak dipakai untuk narasi formal.

## 8. Pengecualian penting

| Kasus | Aturan umum | Pengecualian |
|---|---|---|
| *&* | dibaca *dan* | dalam singkatan Inggris: *Q&A* = kyu en ei |
| */* | *per* | alternatif: *A/B* = A atau B; tanggal; pecahan |
| *-* antara angka | *sampai* | skor *2-1*, nomor telepon, tanggal ISO |
| *x* setelah angka | *kali* | resolusi *1920x1080* = kali; huruf X tunggal = platform/huruf |
| *e* | lihat §2 | homograf |
| *meN-* + /p/ | /p/ luluh | *mempunyai*; gugus serapan (*memproduksi*) |
| Gelar | diekspansi | dalam pengumuman lisan lazim dieja (*S.Kom.* = es kom) |
| *dr.* vs *Dr.* | — | huruf kecil = dokter; kapital = doktor (gelar akademik) |

Normalisasi angka, mata uang, tanggal, jam, dan simbol dijelaskan di [skills/indonesian-phonetics/references/normalization.md](../skills/indonesian-phonetics/references/normalization.md).
