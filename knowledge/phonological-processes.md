# Proses Fonologis

> Label: **[Fakta]** · **[Variasi]** · **[Rekomendasi]**. Kode sumber merujuk [docs/sources.md](../docs/sources.md).

## 1. Asimilasi nasal prefiks *meN-* / *peN-*

**[Fakta]** Nasal *N* pada prefiks *meN-* dan *peN-* menyesuaikan tempat artikulasi konsonan awal kata dasar; hambat tak bersuara dan /s/ di awal kata dasar **luluh** (`alwi-tbbi-2017`, `sneddon-2010`):

| Awal kata dasar | Bentuk prefiks | Contoh | Hasil | IPA hasil |
|---|---|---|---|---|
| b | mem- | baca | membaca | /məm.ba.tʃa/ |
| p (luluh) | mem- | pukul | memukul | /mə.mu.kul/ |
| f, v | mem- | fitnah | memfitnah | — |
| d | men- | dengar | mendengar | /mən.də.ŋar/ |
| t (luluh) | men- | tulis | menulis | /mə.nu.lis/ |
| c, j | men- | cari, jual | mencari, menjual | /mən.tʃa.ri/, /mən.dʒu.al/ |
| s (luluh) | meny- | sapu | menyapu | /mə.ɲa.pu/ |
| g, h, vokal | meng- | gali, hitung, ambil | menggali, menghitung, mengambil | /məŋ.ga.li/ … |
| k (luluh) | meng- | kirim | mengirim | /mə.ŋi.rim/ |
| l, r, m, n, ny, ng, w, y | me- | lihat, rasa, nanti | melihat, merasa, menanti | /mə.li.hat/ … |
| kata dasar satu suku | menge- | cat, bom | mengecat, mengebom | /mə.ŋə.tʃat/ … |

**[Fakta]** Pengecualian dan kasus khusus:

- Gugus konsonan serapan tidak luluh: *mengkritik*, *memproduksi*, *mentransfer*.
- *mempunyai* (dari *punya*) mempertahankan /p/ — bentuk leksikal tetap.
- Bentuk baku *memengaruhi* (bukan *mempengaruhi*), *memesona* (bukan *mempesona*), sesuai KBBI (`kbbi-daring`, perlu dicek ulang reviewer).
- Pada serapan berawal *k*, KBBI menetapkan bentuk luluh sebagai baku (*mengoordinasi*), tetapi bentuk tidak luluh (*mengkoordinasi*) sering terdengar. **[Variasi]**

## 2. Prefiks *ber-* dan *ter-*

**[Fakta]** */r/* prefiks hilang bila kata dasar diawali /r/ atau suku pertamanya berakhir *-er*: *ber-* + *renang* → *berenang*; *ber-* + *kerja* → *bekerja*; *ter-* + *rasa* → *terasa*. Bentuk *belajar* (dari *ajar*) adalah bentuk leksikal khusus.

## 3. Proses pada batas suku dan akhir kata

| Proses | Deskripsi | Contoh |
|---|---|---|
| Glotalisasi /k/ | /k/ akhir kata asli → [ʔ] | *anak* [anaʔ] |
| Penetralan bersuara | /b d/ akhir → [p t] | *sebab* [səbap], *abad* [abat] |
| Penurunan vokal | /i u e o/ di suku tertutup → [ɪ ʊ ɛ ɔ] | *hidup* [hidʊp] |
| Penyisipan luncuran | [j] setelah /i/, [w] setelah /u/ di depan vokal | *dia* [dija], *buah* [buwah] |
| Penyisipan glotal | [ʔ] di antara vokal sama, termasuk batas sufiks | *saat* [saʔat], *kebersamaan* [kəbərsamaʔan] |
| Glotalisasi sebelum sufiks | /k/ akhir kata dasar sering tetap [ʔ] sebelum sufiks vokal **[perlu validasi contoh]** | *duduki* [duduʔi] (`cohn-1989`) |

## 4. Proses ragam santai

**[Variasi]** Lazim dalam percakapan, terutama ragam Jakarta (`sneddon-2006`). Tidak salah, tetapi berbeda ragam:

| Proses | Contoh baku → santai |
|---|---|
| Monoftongisasi | *pakai* → *pake*, *kalau* → *kalo* |
| Pelesapan /h/ antarvokal | *tahu* → *tau*, *lihat* → *liat* |
| Pelesapan suku/fonem awal | *sudah* → *udah*, *saja* → *aja*, *bagaimana* → *gimana* |
| Pelesapan schwa | *seratus* → [sratus] pada tuturan cepat |
| Sufiks *-in* untuk *-kan/-i* | *bikinkan* → *bikinin* (morfologis, bukan fonologis murni) |

## 5. Penyesuaian fonem serapan

**[Variasi]** Lihat tabel risiko makna di [consonants.md](consonants.md#36-konsonan-serapan): /f/→[p], /v/→[f], /z/→[dʒ]/[s], /ʃ/→[s], /x/→[k]/[h], dan penyisipan schwa pada gugus.

## 6. Proses pada singkatan dan kata asing

**[Fakta — ZIP]** Korpus VO HDI menunjukkan prefiks Indonesia menempel pada singkatan Inggris tanpa perubahan bunyi singkatan: *di-DM* → "di di em" (`hdi-kamus-2026`). Bentuk *nge-* informal juga lazim (*nge-share*, *ngedit*) **[Variasi]**.

## Implikasi untuk TTS dan agen AI

- Jangan "membetulkan" kata turunan yang sudah luluh (*memukul*) menjadi bentuk tak luluh.
- Bentuk santai di naskah adalah pilihan gaya; pertahankan kecuali pengguna meminta ragam baku.
- Untuk IPA kata turunan, hitung prefiks dengan /ə/ dan terapkan asimilasi nasal.
