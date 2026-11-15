# Dasar Fonetik Bahasa Indonesia

> Label: **[Fakta]** · **[Variasi]** · **[Rekomendasi]** (lihat [introduction.md](introduction.md#tiga-tingkat-klaim)). Kode sumber merujuk [sources.md](sources.md).

## 1. Fonetik dan fonologi

| | Fonetik | Fonologi |
|---|---|---|
| Objek | Bunyi bahasa secara fisik: cara dihasilkan, sifat akustik, cara didengar | Sistem bunyi: bunyi mana yang membedakan makna dalam satu bahasa |
| Satuan | **Fon** (bunyi konkret), ditulis dalam `[ ]` | **Fonem** (satuan pembeda makna), ditulis dalam `/ /` |
| Contoh | [ɛ] dan [e] pada *nenek* adalah dua fon | Keduanya realisasi satu fonem /e/ |

**[Fakta]** Cabang fonetik: artikulatoris (produksi), akustik (gelombang bunyi), dan auditoris (persepsi) (`chaer-2009`). Repo ini terutama memakai fonetik artikulatoris.

## 2. Alat ucap

**[Fakta]** Bunyi bahasa Indonesia dihasilkan dengan arus udara paru-paru yang keluar (pulmonik egresif) (`chaer-2009`). Alat ucap yang relevan:

| Alat ucap | Peran | Contoh bunyi |
|---|---|---|
| Bibir (labium) | Penutup/penyempit | /p b m w/ |
| Gigi atas + bibir bawah | Labiodental | /f/ |
| Gusi (alveolum) | Tempat artikulasi ujung lidah | /t d n s l r/ |
| Langit-langit keras (palatum) | Bagian depan lidah | /ɲ j/; /tʃ dʒ/ di pascaalveolar |
| Langit-langit lunak (velum) | Pangkal lidah; velum turun = nasal | /k g ŋ x/ |
| Pita suara (glotis) | Getar = bersuara; tutup = hentian glotal | /b/ vs /p/; [ʔ] |
| Rongga hidung | Resonansi nasal | /m n ɲ ŋ/ |

## 3. Klasifikasi konsonan

Tiga parameter (lihat tabel lengkap di [knowledge/consonants.md](../knowledge/consonants.md)):

1. **Tempat artikulasi** — bilabial, labiodental, alveolar, pascaalveolar, palatal, velar, glotal.
2. **Cara artikulasi** — hambat (plosif), afrikat, frikatif, nasal, getar, lateral, semivokal.
3. **Bersuara/tak bersuara** — /b d g dʒ/ bersuara; /p t k tʃ/ tak bersuara.

Contoh: /b/ = hambat bilabial bersuara; /s/ = frikatif alveolar tak bersuara; /ŋ/ = nasal velar.

## 4. Klasifikasi vokal

Tiga parameter (lihat [knowledge/vowels.md](../knowledge/vowels.md)):

1. **Tinggi lidah** — tinggi (/i u/), sedang (/e ə o/), rendah (/a/).
2. **Posisi lidah** — depan (/i e/), tengah (/ə a/), belakang (/u o/).
3. **Bentuk bibir** — bundar (/u o/), tidak bundar (lainnya).

## 5. Fonem dan alofon

**[Fakta]** Dua bunyi adalah fonem berbeda bila menggantinya mengubah makna. Buktinya adalah **pasangan minimal**:

| Pasangan | Kontras |
|---|---|
| *pagi* : *bagi* | /p/ : /b/ |
| *tari* : *dari* | /t/ : /d/ |
| *kalah* : *galah* | /k/ : /g/ |
| *rupa* : *lupa* | /r/ : /l/ |
| *dara* : *darah* | ∅ : /h/ |
| *teras* (rumah) : *teras* (inti) | /e/ : /ə/ (homograf) |

**Alofon** adalah variasi fon dari satu fonem yang muncul menurut lingkungan, tanpa mengubah makna: /k/ akhir kata asli direalisasikan [ʔ] (*anak* [anaʔ]); /u/ di suku tertutup direalisasikan [ʊ] (*hidup* [hidʊp]).

## 6. Segmental dan suprasegmental

- **Segmental**: vokal, konsonan, diftong.
- **Suprasegmental**: tekanan, nada/intonasi, durasi, jeda. Lihat [knowledge/stress-and-intonation.md](../knowledge/stress-and-intonation.md).

## 7. Transkripsi fonetik vs fonemis

| | Fonemis `/ /` | Fonetis `[ ]` |
|---|---|---|
| Mencatat | Fonem (abstrak, pembeda makna) | Realisasi bunyi (detail alofon) |
| *anak* | /a.nak/ | [a.naʔ] |
| *hidup* | /hi.dup/ | [hi.dʊp] |
| *nenek* | /ne.nek/ | [nɛ.nɛʔ] |
| *sebab* | /sə.bab/ | [sə.bap] |

**[Konvensi repo]** Dataset hanya memuat transkripsi **fonemis**. Detail fonetis dijelaskan di dokumentasi. Aturan penulisan IPA ada di [ipa.md](ipa.md).

## 8. Bunyi dan huruf tidak selalu sejajar

Ejaan bahasa Indonesia relatif fonemis, tetapi ada ketidaksejajaran yang penting bagi TTS:

- Satu huruf, dua fonem: *e* = /e/ atau /ə/.
- Dua huruf, satu fonem: *ng* /ŋ/, *ny* /ɲ/, *sy* /ʃ/, *kh* /x/.
- Fonem tanpa huruf: /ʔ/ (kecuali apostrof) dan luncuran [j]/[w].
- Huruf dengan realisasi bergantung posisi: *k* akhir → [ʔ], *b/d* akhir → [p/t].

Detail aturan: [pronunciation-rules.md](pronunciation-rules.md).
