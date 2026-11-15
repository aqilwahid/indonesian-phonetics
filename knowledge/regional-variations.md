# Variasi Regional dan Ragam

> Label: **[Fakta]** · **[Variasi]** · **[Rekomendasi]**. Kode sumber merujuk [docs/sources.md](../docs/sources.md).

## Prinsip

1. **Tidak ada satu logat daerah yang menjadi standar seluruh penutur.** Bahasa Indonesia dipelajari banyak penutur sebagai bahasa kedua setelah bahasa daerah; pelafalannya wajar membawa ciri bahasa pertama.
2. Ciri di bawah adalah **kecenderungan yang sering dilaporkan**, bukan ciri pasti setiap penutur dari daerah itu. Hindari stereotip.
3. Sebagian besar ciri di bawah belum diverifikasi ke studi fonetik terukur di repo ini → status **needs_validation**. Kontribusi rujukan penelitian sangat diharapkan (lihat [CONTRIBUTING.md](../CONTRIBUTING.md)).
4. Bedakan **variasi pelafalan** (bunyi berbeda, kata sama) dari **variasi leksikal/dialek** (kata berbeda: *sudah* vs *su* di Melayu Papua/Ambon). Repo ini fokus pada yang pertama.

## 1. Perbedaan yang tidak mengubah makna vs yang berisiko mengubah makna

| Jenis | Contoh | Mengubah makna? |
|---|---|---|
| Alofon vokal ([e]/[ɛ], [o]/[ɔ], [i]/[ɪ]) | *nenek* [nenek] vs [nɛnɛʔ] | Tidak |
| Realisasi /r/ (getar, tap, uvular) | *rumah* | Tidak |
| /k/ akhir [k] vs [ʔ] | *anak* [anak]/[anaʔ] | Tidak |
| Tekanan dan nada logat | — | Tidak (memengaruhi kesan, bukan makna) |
| /v/ → [f] | *video* [fideo] | Tidak (praktis diterima) |
| **e pepet ↔ e taling** | *apel* /a.pel/ ↔ /a.pəl/ | **Bisa** (homograf) |
| **/f/ → [p]** | *fakta* → [pakta] | **Bisa** (*fakta* vs *pakta*) |
| **/ʃ/ → [s]** | *syarat* → [sarat] | **Bisa** (*syarat* vs *sarat*) |
| **/x/ → [k]** | *khas* → [kas] | **Bisa** (*khas* vs *kas*) |
| Pelesapan /h/ akhir | *darah* → [dara] | **Bisa** (*darah* vs *dara*) |

**[Rekomendasi]** Untuk TTS/voice-over umum, pakai realisasi baku pada kategori "Bisa". Variasi kategori "Tidak" boleh mengikuti karakter suara/persona.

## 2. Kecenderungan yang sering dilaporkan (needs_validation)

| Latar bahasa pertama | Kecenderungan pelafalan dalam bahasa Indonesia | Catatan |
|---|---|---|
| Jawa | Prenasalisasi hambat bersuara di awal sebagian nama tempat ([mbandʊŋ] untuk *Bandung*); hambat bersuara terdengar "berat"; penurunan vokal di suku tertutup lebih kuat | Sering disebut *medhok*; tingkatnya sangat bervariasi |
| Sunda | /f/ dan /v/ → [p] (*fitnah* → [pitnah]); /z/ → [dʒ] | Juga muncul pada penutur dari latar lain |
| Batak (Toba dan sekitarnya) | e pepet cenderung direalisasikan [e]/[ɛ]; tekanan dan intonasi lebih kuat | Berpotensi mengaburkan homograf e |
| Bali | /t/ dan /d/ terdengar retrofleks/apikal [ʈ ɖ] | — |
| Bugis/Makassar | Nasal akhir cenderung [ŋ] (*makan* → [makaŋ]); geminasi konsonan | — |
| Minangkabau | Pola intonasi khas; sebagian vokal akhir berubah dalam alih kode | Lebih banyak bersifat leksikal/dialektal |
| Maluku/Papua/NTT | Banyak ciri bersifat dialek Melayu lokal (leksikon & morfologi), mis. pemendekan *sudah* → *su*, *tidak* → *tra/tar* | Bukan sekadar pelafalan |
| Jakarta (ragam santai) | Monoftongisasi (*pake*, *kalo*), pelesapan /h/ dan suku awal (*udah, aja*), sufiks *-in* | Ragam informal yang menyebar lewat media (`sneddon-2006`) |

## 3. Ragam formal dan informal

| Aspek | Formal/baku | Informal |
|---|---|---|
| Diftong akhir | *pakai, sampai, kalau* | *pake, sampe, kalo* |
| Bentuk ingkar | *tidak* | *nggak, enggak, gak* |
| Pronomina | *saya, Anda* | *aku, gue/gua, lu/lo* |
| Fonem serapan | /f x ʃ z/ dipertahankan | sering diganti fonem asli |
| Singkatan dalam narasi | diekspansi atau dieja baku | dieja santai, kadang nama huruf Inggris |
| Jam | *pukul 19.00* (24 jam) | *jam tujuh malam* |

**[Rekomendasi]** Pilih ragam berdasarkan naskah dan audiens, lalu **konsisten** sepanjang dokumen. Skill tidak boleh mengubah ragam naskah tanpa diminta.

## 4. Variasi berdasarkan konteks penggunaan

- **Teknologi/kreator**: initialism asal Inggris lebih sering dieja dengan nama huruf Inggris (*CTR* = si ti ar), tetapi banyak yang tetap dieja Indonesia (*PDF* = pe de ef, *API* = a pe i) (`hdi-kamus-2026`).
- **Kantor/pemerintahan**: initialism Indonesia selalu dieja nama huruf Indonesia (*KTP, NPWP, BPJS*); beberapa singkatan Inggris pun dieja Indonesia (*HRD* = ha er de).
- **Akademik**: gelar sering dieja singkat dalam pengumuman (*S.Kom.* = es kom), diekspansi dalam upacara resmi (*sarjana komputer*).
- **Siaran/berita**: kecenderungan memakai bentuk baku dan *pukul* + 24 jam.

## 5. Variasi yang diterima di dataset

Dataset mencatat variasi di field `variants` dengan `register`, `region`, `context`, dan `meaning_changing`. Prinsipnya:

- Satu `spoken_form` default per entri (bacaan paling netral/lazim di konteks yang dicatat).
- Varian yang **mengubah makna** ditandai `meaning_changing: true` dan entri ditandai `ambiguous: true`.
- Varian regional tanpa bukti penelitian diberi sumber `maintainer-interpretation` dan confidence `needs_validation`.
