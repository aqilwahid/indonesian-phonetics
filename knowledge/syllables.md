# Suku Kata, Pemenggalan, dan Fonotaktik

> Label: **[Fakta]** · **[Variasi]** · **[Rekomendasi]**. Kode sumber merujuk [docs/sources.md](../docs/sources.md).

## 1. Pola suku kata

**[Fakta]** Pola suku kata bahasa Indonesia (K = konsonan, V = vokal) menurut tata bahasa baku (`alwi-tbbi-2017`). Pola dengan gugus konsonan hanya muncul pada kata serapan.

| Pola | Contoh (suku bercetak tebal) | Asal |
|---|---|---|
| V | **a**-nak | asli |
| VK | **an**-tar | asli |
| KV | **ra**-kit | asli |
| KVK | **pin**-tu, ma-**kan** | asli |
| KKV | **pra**-ja, **dra**-ma | serapan |
| KKVK | **blok**, kon-**trak** | serapan |
| KVKK | **teks**, **pers** | serapan |
| KKKV | **stra**-tegi | serapan |
| KKKVK | **struk** | serapan |
| KKVKK | kom-**pleks** | serapan |
| KVKKK | **korps** | serapan |

## 2. Pemenggalan ortografis (EYD/PUEBI)

**[Fakta]** Aturan pemenggalan kata dasar (`puebi-2015`):

1. Dua vokal berurutan dipenggal di antaranya: *bu-ah*, *ma-in*. **Diftong tidak dipenggal**: *pan-dai*, *sur-vei*.
2. Satu konsonan di antara dua vokal ikut suku berikutnya: *ba-pak*, *de-ngan* (gabungan *ng* = satu konsonan).
3. Dua konsonan berurutan dipenggal di antaranya: *Ap-ril*, *cap-lok*.
4. Tiga konsonan atau lebih dipenggal setelah konsonan pertama: *ul-tra*, *in-stru-men*.
5. Gabungan huruf yang melambangkan satu bunyi (*kh, ng, ny, sy*) tidak dipisah: *bang-sa*, *ikh-las*.
6. Kata turunan dipenggal sedapat mungkin di batas morfem: *ber-jalan*, *mem-bantu*.

**[Fakta]** Pemenggalan ini adalah **aturan ejaan untuk pergantian baris**. Pembagian suku kata fonologis bisa berbeda, terutama pada gugus serapan dan batas morfem.

## 3. Batas morfem dan suku kata

Batas morfem dapat menghasilkan homograf yang berbeda pemenggalan:

| Kata | Analisis | IPA |
|---|---|---|
| *beruang* (hewan) | be.ru.ang | /bə.ru.aŋ/ |
| *beruang* (ber- + uang) | ber.u.ang | /bər.u.aŋ/ |

Lihat entri `word-0013` di `pronunciation-dictionary.json`.

## 4. Fonotaktik

**[Fakta]** Batasan distribusi bunyi (`muslich-2008`, `sneddon-2010`):

- **Akhir kata asli** dapat berupa vokal atau konsonan /p t k m n ŋ s h r l/. /ɲ/, /tʃ/, /dʒ/, /j/, /w/ tidak muncul sebagai konsonan akhir (kecuali sebagai bagian diftong atau serapan). EYD mencatat *ny* tidak muncul di akhir kata.
- **/ə/** tidak muncul di suku akhir terbuka kata asli.
- **Gugus nasal + hambat homorgan** lintas suku sangat umum: *tampak* /tam.pak/, *tinggal* /tiŋ.gal/, *candi* /tʃan.di/.
- **Gugus awal** hanya pada serapan, umumnya hambat + likuida (*pr, tr, kr, bl, pl, kl, gr*) dan *s* + hambat (*sp, st, sk, str*).
- **Gugus akhir** hanya pada serapan: *-ks, -ns, -rs, -ps* (*teks, ons, pers*).

**[Variasi]** Gugus serapan sering disederhanakan atau disisipi schwa dalam ujaran santai/regional (*knalpot* → [kənalpot]).

## Implikasi untuk TTS dan agen AI

- Pemisah suku kata dalam IPA dataset memakai titik (`/pan.dai̯/`), mengikuti pemenggalan fonologis yang konsisten dengan aturan di atas.
- Saat membuat respelling, jangan memecah gabungan *ng/ny/sy/kh*.
