# Konsonan Bahasa Indonesia

> Label: **[Fakta]** · **[Variasi]** · **[Rekomendasi]** — lihat [vowels.md](vowels.md). Kode sumber merujuk [docs/sources.md](../docs/sources.md).

## 1. Inventaris

**[Fakta]** Fonem konsonan asli dan serapan (`soderberg-olson-2008`, `alwi-tbbi-2017`, `sneddon-2010`). Fonem dalam kurung adalah fonem serapan yang realisasinya bervariasi antarpenutur.

| Cara \ Tempat | Bilabial | Labiodental | Alveolar/dental | Pascaalveolar | Palatal | Velar | Glotal |
|---|---|---|---|---|---|---|---|
| Hambat (plosif) | p b | | t d | | | k g | ʔ |
| Afrikat | | | | tʃ dʒ | | | |
| Frikatif | | (f) (v) | s (z) | (ʃ) | | (x) | h |
| Nasal | m | | n | | ɲ | ŋ | |
| Getar/tap | | | r | | | | |
| Lateral | | | l | | | | |
| Semivokal | w | | | | j | | |

Catatan: /q/ muncul pada ragam keagamaan untuk huruf *q* serapan Arab (*Al-Qur'an*), umumnya direalisasikan [k] dalam ragam umum.

## 2. Pemetaan huruf → fonem

| Huruf/gabungan | Fonem | Contoh | IPA |
|---|---|---|---|
| p, b, t, d, k, g | /p b t d k g/ | *pagi, bagi, tari, dari, kalah, galah* | /pa.gi/, /ba.gi/ … |
| c | /tʃ/ | *cepat* | /tʃə.pat/ |
| j | /dʒ/ | *jalan* | /dʒa.lan/ |
| y | /j/ | *yang* | /jaŋ/ |
| ny | /ɲ/ | *nyanyi* | /ɲa.ɲi/ |
| ng | /ŋ/ | *bangun* | /ba.ŋun/ |
| ngg | /ŋg/ | *mangga* | /maŋ.ga/ |
| sy | /ʃ/ | *syarat* | /ʃa.rat/ |
| kh | /x/ | *khusus* | /xu.sus/ |
| f | /f/ | *fakta* | /fak.ta/ |
| v | /v/ → umumnya [f] | *video* | /vi.de.o/ [fideo] |
| z | /z/ | *zaman* | /za.man/ |
| q | /k/ (ragam keagamaan /q/) | *Al-Qur'an* | /al.qur.ʔan/ |
| x | /ks/ (huruf *x* jarang; ejaan serapan umumnya menjadi *ks*); di awal kata umumnya [s] | *xenon*, *sinar-X* (nama huruf /eks/) | — |
| ' (apostrof) | /ʔ/ | *Al-Qur'an* | /al.qur.ʔan/ |

**[Fakta]** Pasangan minimal membuktikan kontras fonemis: *pagi/bagi* (/p/:/b/), *tari/dari* (/t/:/d/), *kalah/galah* (/k/:/g/), *rupa/lupa* (/r/:/l/), *fakta/pakta* (/f/:/p/ — kontras serapan).

## 3. Realisasi penting

### 3.1 Hambat tak beraspirasi
**[Fakta]** /p t k/ tidak beraspirasi ([p], bukan [pʰ]) (`soderberg-olson-2008`). **[Rekomendasi]** Suara TTS yang dilatih dominan bahasa Inggris cenderung mengaspirasi; ini terdengar "asing" bagi penutur Indonesia.

### 3.2 Hambat akhir
**[Fakta]** Di akhir suku kata, hambat cenderung tidak dilepas ([p̚ t̚]).
- **/k/ akhir pada kata asli → [ʔ]**: *anak* [anaʔ], *tidak* [tidaʔ], *bapak* [bapaʔ], *rakyat* [raʔjat].
- **/b/ dan /d/ akhir → [p] dan [t]** (penetralan bersuara): *sebab* [səbap], *abad* [abat].

**[Konvensi repo — interpretasi]** IPA fonemis di dataset menulis huruf *k* akhir sebagai /k/ (mis. *anak* /a.nak/), lalu realisasi [ʔ] dijelaskan di dokumentasi. Literatur berbeda pendapat apakah [ʔ] di sini alofon /k/ atau fonem /ʔ/ tersendiri; konvensi ini dipilih agar IPA fonemis tetap dekat dengan ejaan dan konsisten. Simbol /ʔ/ ditulis hanya bila ada apostrof atau di antara dua vokal sama (*saat* /sa.ʔat/, *maaf* /ma.ʔaf/).

### 3.3 Hentian glotal
**[Fakta]** [ʔ] muncul (a) untuk *k* akhir kata asli, (b) di antara dua vokal sama (*saat, taat, maaf*), (c) menandai apostrof serapan Arab, dan (d) secara opsional sebelum vokal awal kata dalam ujaran tegas.

### 3.4 /r/
**[Fakta]** /r/ direalisasikan getar [r] atau tap [ɾ]. **[Variasi]** Realisasi uvular atau aproksiman muncul pada sebagian penutur dan tidak mengubah makna.

### 3.5 /h/
**[Fakta]** /h/ di antara dua vokal berbeda sering melemah atau hilang dalam ragam santai (*tahu* → [tau], *lihat* → [liat]). Di akhir kata /h/ dipertahankan dan membedakan kata: *dara/darah* /da.ra/ vs /da.rah/.

### 3.6 Konsonan serapan
**[Variasi]** Banyak penutur mengganti fonem serapan dengan fonem asli terdekat. Penggantian ini kadang **mengubah makna** karena menggabungkan dua kata:

| Fonem | Pengganti umum | Contoh | Risiko makna |
|---|---|---|---|
| /f/ | [p] | *fajar* → [padʒar] | *fakta* ≈ *pakta* |
| /v/ | [f] (sangat umum, cenderung diterima) | *video* → [fideo] | rendah |
| /z/ | [dʒ] atau [s] | *zaman* → [dʒaman] | rendah |
| /ʃ/ | [s] | *syarat* → [sarat] | *syarat* ≈ *sarat* (penuh) |
| /x/ | [k] atau [h] | *khusus* → [kusus]; *akhir* → [ahir] | *khas* ≈ *kas* |

**[Rekomendasi]** Untuk narasi formal/TTS, pertahankan fonem serapan baku; catat realisasi lain sebagai varian, bukan kesalahan mutlak.

## 4. Gugus konsonan

**[Fakta]** Kata asli tidak memiliki gugus dalam satu suku kata. Gugus awal dan akhir muncul pada serapan: *praktik, struktur, kompleks, teks*. **[Variasi]** Sebagian penutur menyisipkan schwa untuk memecah gugus (*knalpot* → [kənalpot], *setrika*/*seterika*).

## Implikasi untuk TTS dan agen AI

- Jangan meng-IPA-kan *ng* sebagai /n g/, *ny* sebagai /n j/, atau *c* sebagai /k/.
- Untuk IPA, pakai /j/ (bukan *y*), /tʃ/ (bukan *c*), /dʒ/ (bukan *j*), /ɲ/ (bukan *ñ*). Validator repo menolak kesalahan ini.
- Nasal dalam prefiks berubah mengikuti konsonan awal kata dasar — lihat [phonological-processes.md](phonological-processes.md).
