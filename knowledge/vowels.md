# Vokal Bahasa Indonesia

> Label: **[Fakta]** = didukung sumber yang dirujuk · **[Variasi]** = realisasi yang berbeda antarpenutur/konteks · **[Rekomendasi]** = saran praktis repo (interpretasi). Kode sumber merujuk [docs/sources.md](../docs/sources.md).

## 1. Inventaris fonem vokal

**[Fakta]** Bahasa Indonesia baku memiliki enam fonem vokal (`soderberg-olson-2008`, `alwi-tbbi-2017`):

| | Depan | Tengah | Belakang |
|---|---|---|---|
| **Tinggi (close)** | /i/ | | /u/ |
| **Sedang (mid)** | /e/ | /ə/ | /o/ |
| **Rendah (open)** | | /a/ | |

/u/ dan /o/ bundar; vokal lain tidak bundar.

| Fonem | Huruf | Contoh | IPA fonemis |
|---|---|---|---|
| /i/ | i | *ibu*, *kita* | /i.bu/, /ki.ta/ |
| /e/ | e | *enak*, *sate* | /e.nak/, /sa.te/ |
| /ə/ | e | *besar*, *telur* | /bə.sar/, /tə.lur/ |
| /a/ | a | *apa*, *makan* | /a.pa/, /ma.kan/ |
| /o/ | o | *ekor*, *toko* | /e.kor/, /to.ko/ |
| /u/ | u | *ular*, *buku* | /u.lar/, /bu.ku/ |

## 2. Masalah utama: satu huruf *e*, dua fonem

**[Fakta]** Huruf *e* melambangkan /e/ (e taling) **dan** /ə/ (e pepet). Ejaan biasa tidak membedakannya. EYD/PUEBI menyediakan diakritik opsional bila perlu menghindari salah lafal (`puebi-2015`, `eyd-v-2022`):

| Diakritik | Bunyi | Contoh PUEBI |
|---|---|---|
| é | [e] | téras (bagian rumah), kécap (saus) |
| è | [ɛ] | sèri (film seri), militèr |
| ê | [ə] | sêri (hasil imbang), kêcap (mengecap) |

Akibatnya, pasangan **homograf** berikut berbeda makna hanya karena kualitas *e* (lihat `pronunciation-dictionary.json`, subkategori `homograph`):

| Ejaan | /e/ | /ə/ |
|---|---|---|
| teras | /te.ras/ bagian rumah | /tə.ras/ inti, "pejabat teras" |
| kecap | /ke.tʃap/ saus kedelai | /kə.tʃap/ mengecap |
| seri | /se.ri/ rangkaian | /sə.ri/ imbang |
| apel | /a.pel/ buah | /a.pəl/ upacara |
| per | /per/ pegas | /pər/ tiap |
| memerah | /mə.me.rah/ menjadi merah | /mə.mə.rah/ memeras susu |

**[Fakta]** Kecenderungan distribusi yang membantu (bukan aturan mutlak):

- Prefiks *ber-, ter-, me-, pe-, ke-, se-* selalu /ə/: *berjalan* /bər.dʒa.lan/, *sepuluh* /sə.pu.luh/.
- /ə/ tidak muncul di suku akhir terbuka kata asli: suku akhir terbuka bereja *e* hampir selalu /e/ (*sate, tempe, sore*).
- Kata serapan Eropa cenderung /e/ (*sistem* /sis.tem/, *efektif* /e.fek.tif/, *objek* /ob.dʒek/), tetapi suku akhir *-el/-er* pada serapan Belanda sering /ə/ (*wortel* /wor.təl/, *dokter* /dok.tər/).

**[Rekomendasi]** Mesin TTS dan agen AI **tidak boleh** menebak kualitas *e* dari ejaan. Gunakan leksikon; jika kata tidak ada di leksikon, jangan isi IPA dan beri tanda ragu.

## 3. Alofon

**[Fakta]** Vokal sedang dan tinggi cenderung lebih rendah/kendur di suku tertutup (`soderberg-olson-2008`, `muslich-2008`). Distribusi persisnya dibahas berbeda-beda di literatur, jadi diperlakukan sebagai kecenderungan:

| Fonem | Alofon umum | Lingkungan khas | Contoh |
|---|---|---|---|
| /i/ | [i] ~ [ɪ] | [ɪ] di suku akhir tertutup | *kecil* [kə.tʃɪl] |
| /u/ | [u] ~ [ʊ] | [ʊ] di suku akhir tertutup | *hidup* [hi.dʊp] |
| /e/ | [e] ~ [ɛ] | [ɛ] di suku tertutup atau bila suku berikut berisi [ɛ] | *nenek* [nɛ.nɛʔ] |
| /o/ | [o] ~ [ɔ] | [ɔ] di suku tertutup | *pohon* [pɔ.hɔn] |

**[Variasi]** Tingkat penurunan ini dipengaruhi bahasa daerah penutur (lihat [regional-variations.md](regional-variations.md)). Perbedaan alofonis **tidak mengubah makna**.

Repo ini menulis IPA **fonemis** (/e/, /o/, /i/, /u/) di dataset; alofon hanya dipakai di dokumentasi dengan kurung siku.

## 4. Vokal *eu* (EYD V)

**[Fakta]** EYD V (2022) menambahkan gabungan huruf vokal *eu* untuk monoftong [ɘ], terutama pada kata serapan dari bahasa daerah seperti Aceh dan Sunda (contoh: *seudati*) (`eyd-v-2022`). Ini bukan fonem asli bahasa Indonesia baku; pelafalannya mengikuti bahasa asal.

## 5. Deret vokal

Dua vokal berurutan umumnya berada di suku kata berbeda (*bu.ah, ma.in, di.a*). Lihat [diphthongs.md](diphthongs.md) untuk diftong dan penyisipan luncuran/hentian glotal.

## Implikasi untuk TTS dan agen AI

- Kesalahan *e* paling sering terjadi pada homograf, kata serapan, singkatan yang dibaca sebagai kata (*Puskesmas*), dan nama diri.
- Untuk pustaka asing yang namanya bertabrakan dengan kata Indonesia (mis. **Keras** vs *keras* /kə.ras/), beri konteks atau tandai.
- Penanda diakritik (é/ê) boleh dipakai dalam respelling bila mesin TTS terbukti mendukungnya; uji dulu.
