# Contoh: Pelafalan Kata Umum

Keluaran yang mencantumkan id entri berasal dari dataset dan dapat diperiksa dengan:

```bash
python skills/indonesian-phonetics/scripts/lookup.py <kata>
```

## 1. Kualitas vokal *e*

| Kata | IPA | Jenis *e* | Entri |
|---|---|---|---|
| enak | /e.nak/ | taling | `word-0014` |
| besar | /bə.sar/ | pepet | `word-0026` |
| kemeja | /kə.me.dʒa/ | pepet + taling | `word-0034` |
| ember | /em.bər/ | taling + pepet | `word-0033` |

**Pelajaran:** ejaan tidak membedakan /e/ dan /ə/. Agen tidak boleh menebak; kata di luar leksikon diberi IPA hanya bila setiap *e* diketahui.

## 2. Homograf

**Input:** `Pejabat teras kementerian berkumpul di teras gedung.`

**Analisis:**

| Token | Konteks | Bacaan | IPA |
|---|---|---|---|
| teras (1) | "pejabat teras" | têras | /tə.ras/ |
| teras (2) | "di teras gedung" | téras | /te.ras/ |

Untuk TTS, teks biasanya tidak diubah; jika mesin salah baca, pertimbangkan respelling berdiakritik PUEBI (*têras*, *téras*) **setelah** menguji dukungan mesin.

**Input tanpa konteks:** `teras` → keluaran: homograf, dua kemungkinan, tidak ada IPA tunggal (lihat `word-0001`).

## 3. Hentian glotal dan konsonan akhir

| Kata | IPA fonemis | Realisasi | Catatan |
|---|---|---|---|
| saat | /sa.ʔat/ | [sa.ʔat] | vokal sama berurutan (`word-0036`) |
| maaf | /ma.ʔaf/ | [ma.ʔaf] | serapan Arab (`loanwords.json`) |
| anak | /a.nak/ | [a.naʔ] | *k* akhir → [ʔ] (`word-0038`) |
| sebab | /sə.bab/ | [sə.bap] | *b* akhir → [p] (contoh aturan, belum ada di dataset) |

## 4. Gabungan konsonan

| Kata | IPA | Catatan |
|---|---|---|
| bangun | /ba.ŋun/ | *ng* = satu bunyi |
| mangga | /maŋ.ga/ | *ngg* = /ŋ/ + /g/ |
| nyanyi | /ɲa.ɲi/ | *ny* = /ɲ/ |
| syukur | /ʃu.kur/ | *sy* = /ʃ/; varian santai [sukur] |
| khusus | /xu.sus/ | *kh* = /x/; varian [kusus] |

## 5. Bentuk informal

**Input:** `Gimana kalo kita pake cara ini aja?`

**Keluaran skill (target `tts`):** teks **tidak diubah**. *gimana, kalo, pake, aja* adalah pilihan gaya penulis (ragam santai). Leksikon mencatat bentuk bakunya (*bagaimana, kalau, pakai, saja*) sebagai varian formal, dipakai hanya jika pengguna meminta ragam baku.

## 6. Nama diri berejaan lama

| Tulisan | Bacaan | IPA |
|---|---|---|
| Soekarno | sukarno | /su.kar.no/ |
| Gadjah Mada | gajah mada | /ga.dʒah ma.da/ |

Teks tampilan tidak diubah; respelling modern hanya untuk teks TTS bila mesin salah baca.
