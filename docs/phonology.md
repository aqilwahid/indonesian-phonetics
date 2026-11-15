# Fonologi Bahasa Indonesia: Ikhtisar

> Dokumen ini merangkum sistem fonologis dan mengarahkan ke berkas rinci di [knowledge/](../knowledge/). Label: **[Fakta]** · **[Variasi]** · **[Rekomendasi]**.

## 1. Inventaris fonem

**[Fakta]** (`soderberg-olson-2008`, `alwi-tbbi-2017`)

- **Vokal (6):** /i e ə a o u/ → [knowledge/vowels.md](../knowledge/vowels.md)
- **Diftong (4):** /ai̯ au̯ oi̯ ei̯/ → [knowledge/diphthongs.md](../knowledge/diphthongs.md)
- **Konsonan asli (19):** /p b t d k g ʔ tʃ dʒ s h m n ɲ ŋ r l w j/
- **Konsonan serapan:** /f v z ʃ x/ (+ /q/ ragam keagamaan) → [knowledge/consonants.md](../knowledge/consonants.md)

Catatan: status /ʔ/ sebagai fonem tersendiri atau alofon /k/ dibahas berbeda di literatur; lihat konvensi repo di [consonants.md](../knowledge/consonants.md#32-hambat-akhir).

## 2. Struktur suku kata dan fonotaktik

**[Fakta]** Pola dasar kata asli: (K)V(K). Gugus konsonan hanya pada serapan, menghasilkan hingga 11 pola suku kata. Konsonan akhir kata asli terbatas pada /p t k m n ŋ s h r l/. → [knowledge/syllables.md](../knowledge/syllables.md)

## 3. Prosodi

**[Fakta]** Deskripsi tradisional: tekanan penultima, bergeser ke suku akhir bila penultima berisi schwa. Riset eksperimental: tekanan kata lemah, prominensi terutama di tingkat frasa; tidak ada kontras makna oleh tekanan. Intonasi deklaratif turun, tanya ya/tidak naik. → [knowledge/stress-and-intonation.md](../knowledge/stress-and-intonation.md)

## 4. Proses fonologis

**[Fakta]** Asimilasi nasal *meN-/peN-* dengan peluluhan /p t k s/; pelesapan /r/ pada *ber-/ter-*; glotalisasi /k/ akhir; penetralan bersuara /b d/ akhir; penurunan vokal di suku tertutup; penyisipan luncuran dan hentian glotal. **[Variasi]** Monoftongisasi dan pelesapan pada ragam santai. → [knowledge/phonological-processes.md](../knowledge/phonological-processes.md)

## 5. Variasi

**[Variasi]** Pengaruh bahasa daerah, ragam formal/informal, dan konteks (teknologi, kantor, akademik, siaran). Dibedakan antara variasi yang tidak mengubah makna (alofon) dan yang berisiko mengubah makna (e pepet/taling, /f/→[p], /ʃ/→[s], /x/→[k]). → [knowledge/regional-variations.md](../knowledge/regional-variations.md)

## 6. Hubungan dengan ejaan

Fonologi menjelaskan **bunyi**; ejaan (EYD V) mengatur **tulisan**. Keduanya sering sejalan, tetapi tidak identik (mis. pemenggalan ortografis vs suku kata fonologis; satu huruf *e* untuk dua fonem). Aturan pembacaan tulisan → [pronunciation-rules.md](pronunciation-rules.md).

## Ringkasan untuk mesin

| Fitur | Keputusan untuk TTS/IPA |
|---|---|
| e pepet/taling | Wajib leksikon; jangan ditebak |
| /k/ akhir | IPA fonemis /k/, realisasi [ʔ] |
| Tekanan | Tidak ditandai di IPA; prominensi diatur frasa |
| Alofon vokal | Tidak ditulis di IPA fonemis |
| Fonem serapan | Dipertahankan pada ragam baku; realisasi lain jadi varian |
