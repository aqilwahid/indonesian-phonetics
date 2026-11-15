# Tekanan dan Intonasi

> Label: **[Fakta]** · **[Variasi]** · **[Rekomendasi]**. Kode sumber merujuk [docs/sources.md](../docs/sources.md).

## 1. Tekanan kata: deskripsi tradisional dan temuan riset

**[Fakta — deskripsi tradisional]** Tata bahasa dan analisis fonologis klasik menyebut tekanan bahasa Indonesia jatuh pada **suku kedua dari belakang (penultima)**, dan bergeser ke **suku terakhir bila penultima berisi schwa** (`cohn-1989`, `alwi-tbbi-2017`):

| Kata | Suku bertekanan (deskripsi tradisional) |
|---|---|
| *makanan* | penultima: ma.**ka**.nan |
| *rumah* | penultima: **ru**.mah |
| *besar* (penultima /bə/ berisi schwa) | bergeser ke suku akhir: bə.**sar** |
| *telur* | bergeser ke suku akhir: tə.**lur** |

**[Fakta — temuan riset]** Studi fonetik eksperimental menemukan bahwa tekanan kata dalam bahasa Indonesia lemah dan tidak konsisten, dan bahwa prominensi lebih banyak ditentukan di tingkat **frasa** (akhir frasa) daripada kata (`goedemans-vanzanten-2007`). Realisasinya juga sangat dipengaruhi bahasa daerah penutur.

**[Fakta]** Bahasa Indonesia tidak memiliki pasangan minimal yang dibedakan oleh letak tekanan (berbeda dengan bahasa Inggris *REcord* vs *reCORD*).

**[Konvensi repo]** Karena status tekanan kata masih diperdebatkan, IPA di dataset **tidak menandai tekanan** (tanpa ˈ).

## 2. Intonasi

**[Fakta]** Pola intonasi dasar (`sneddon-2010`, `alwi-tbbi-2017`):

| Jenis tuturan | Kontur umum | Contoh |
|---|---|---|
| Deklaratif | naik di tengah, **turun** di akhir | *Dia sudah pulang.* ↘ |
| Tanya ya/tidak tanpa partikel | **naik** di akhir | *Dia sudah pulang?* ↗ |
| Tanya dengan kata tanya | puncak pada kata tanya, akhir turun | ***Kapan*** *dia pulang?* ↘ |
| Tanya dengan *-kah/apakah* | akhir cenderung turun/datar | *Apakah dia sudah pulang?* |
| Perintah | tinggi di awal, turun | *Duduk!* |
| Rincian (daftar) | naik pada butir tidak terakhir, turun pada butir terakhir | *apel ↗, jeruk ↗, dan pisang ↘* |

**[Fakta]** Penekanan informasi sering diungkapkan dengan partikel (*-lah, -kah, kok, sih, dong, kan*) dan urutan kata, tidak hanya dengan nada.

## 3. Jeda dan pemenggalan frasa

**[Fakta — ZIP]** Praktik produksi VO HDI (`hdi-ebook-2026`, `hdi-galeri-2026`):

- Kalimat pendek (rata-rata 7–10 kata, satu kalimat satu poin) lebih stabil dibaca mesin.
- Kurung tidak membuat salah baca tetapi menghilangkan jeda; koma memberi jeda yang lebih jelas.
- Titik tiga (…) dapat menambah jeda tetapi sering membuat suara terdengar ragu.

**[Rekomendasi]**
- Gunakan tanda baca untuk mengatur frasa intonasi: koma = jeda pendek, titik = jeda panjang dengan nada turun.
- Pecah kalimat lebih dari ±25 kata di batas klausa yang wajar tanpa menambah kata baru.
- Jangan memberi tekanan leksikal kuat ala bahasa Inggris pada kata Indonesia saat menyusun SSML/prompt prosodi.

## Implikasi untuk TTS dan agen AI

- Kesalahan prosodi yang paling terasa pada TTS Indonesia biasanya **tekanan gaya Inggris** pada kata asli dan **kontur tanya** yang tidak naik.
- Untuk kalimat tanya ya/tidak tanpa partikel, pastikan tanda tanya ada di teks TTS.
