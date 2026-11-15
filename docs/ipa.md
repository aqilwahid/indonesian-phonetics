# IPA untuk Bahasa Indonesia

> Konvensi transkripsi International Phonetic Alphabet (IPA) yang dipakai di seluruh repo. Sumber: `ipa-handbook-1999`, `ipa-chart-2020`, `soderberg-olson-2008`, `puebi-2015`.

## 1. Konvensi repo

| Aturan | Contoh |
|---|---|
| Dataset memakai **transkripsi fonemis** diapit `/ /` | `/ma.kan/` |
| Transkripsi fonetis `[ ]` hanya di dokumentasi | `[a.naʔ]` |
| Batas suku kata = titik `.` | `/sə.pu.luh/` |
| Batas kata = spasi tunggal | `/dan la.in la.in/` |
| Tekanan **tidak** ditandai | bukan `/ˈma.kan/` |
| Diftong ditandai `̯` (U+032F) pada unsur kedua | `/pan.dai̯/` |
| *k* akhir ditulis /k/; realisasi [ʔ] di dokumentasi | `/a.nak/` [a.naʔ] |
| /ʔ/ ditulis hanya untuk apostrof dan di antara vokal sama | `/sa.ʔat/`, `/al.qur.ʔan/` |
| Luncuran [j]/[w] antarvokal tidak ditulis | `/di.a/` bukan `/di.ja/` |
| Alofon [ɪ ɛ ɔ ʊ] tidak ditulis di IPA fonemis | `/hi.dup/` bukan `/hi.dʊp/` |
| IPA **null** jika tidak didukung data | kualitas *e* belum pasti → `null` |

## 2. Tabel simbol

### Vokal dan diftong

| IPA | Huruf | Contoh | IPA contoh |
|---|---|---|---|
| /i/ | i | ikan | /i.kan/ |
| /e/ | e (taling) | enak | /e.nak/ |
| /ə/ | e (pepet) | besar | /bə.sar/ |
| /a/ | a | apa | /a.pa/ |
| /o/ | o | toko | /to.ko/ |
| /u/ | u | buku | /bu.ku/ |
| /ai̯/ | ai | pantai | /pan.tai̯/ |
| /au̯/ | au | pulau | /pu.lau̯/ |
| /oi̯/ | oi | koboi | /ko.boi̯/ |
| /ei̯/ | ei | survei | /sur.vei̯/ |

### Konsonan

| IPA | Huruf | Contoh | IPA contoh |
|---|---|---|---|
| /p/ /b/ | p, b | pagi, bagi | /pa.gi/, /ba.gi/ |
| /t/ /d/ | t, d | tari, dari | /ta.ri/, /da.ri/ |
| /k/ /g/ | k, g | kalah, galah | /ka.lah/, /ga.lah/ |
| /ʔ/ | ' atau tanpa huruf | saat | /sa.ʔat/ |
| /tʃ/ | c | cepat | /tʃə.pat/ |
| /dʒ/ | j | jalan | /dʒa.lan/ |
| /f/ /v/ | f, v | fakta, video | /fak.ta/, /vi.de.o/ |
| /s/ /z/ | s, z | sama, zaman | /sa.ma/, /za.man/ |
| /ʃ/ | sy | syukur | /ʃu.kur/ |
| /x/ | kh | khusus | /xu.sus/ |
| /h/ | h | hari | /ha.ri/ |
| /m/ /n/ | m, n | mana, nama | /ma.na/, /na.ma/ |
| /ɲ/ | ny | nyanyi | /ɲa.ɲi/ |
| /ŋ/ | ng | bangun | /ba.ŋun/ |
| /ŋg/ | ngg | mangga | /maŋ.ga/ |
| /r/ /l/ | r, l | rupa, lupa | /ru.pa/, /lu.pa/ |
| /w/ | w | warna | /war.na/ |
| /j/ | y | yang | /jaŋ/ |
| /q/ | q (ragam keagamaan) | Al-Qur'an | /al.qur.ʔan/ |

## 3. Kesalahan umum (ditolak validator)

| Salah | Benar | Alasan |
|---|---|---|
| `/yaŋ/` | `/jaŋ/` | Huruf *y* = IPA /j/ |
| `/ceri/` | `/tʃe.ri/` | Huruf *c* = /tʃ/ |
| `/ñaɲi/` | `/ɲa.ɲi/` | Palatal nasal = ɲ, bukan ñ |
| `/baŋun/` dengan `ng` | `/ba.ŋun/` | Tulis /ŋ/, bukan *ng* |
| `/sa'at/` | `/sa.ʔat/` | Apostrof bukan simbol IPA |
| `[e.nak]` di dataset | `/e.nak/` | Dataset fonemis |

## 4. Menyusun IPA untuk singkatan

Initialism yang dieja dengan nama huruf Indonesia disusun dari nama huruf PUEBI (`puebi-2015`): A /a/, B /be/, C /tʃe/, D /de/, E /e/, F /ef/, G /ge/, H /ha/, I /i/, J /dʒe/, K /ka/, L /el/, M /em/, N /en/, O /o/, P /pe/, Q /ki/, R /er/, S /es/, T /te/, U /u/, V /ve/, W /we/, X /eks/, Y /je/, Z /zet/.

Contoh: *KTP* → /ka te pe/; *MP4* → /em pe əm.pat/.

Bacaan dengan nama huruf **Inggris** (si ti ar) dan kata asing **tidak** diberi IPA di dataset, karena realisasi penutur Indonesia sangat bervariasi; dataset memberi `respelling` sebagai gantinya.

## 5. Kapan IPA dibiarkan null

- Kualitas *e* belum dikonfirmasi sumber (mis. *Februari*, *September*, *teknik*).
- Kata asing/merek yang lafalnya bervariasi.
- Akronim yang dibaca sebagai kata dengan *e* (mis. *Puskesmas*).
- Homograf: IPA ada di masing-masing varian, bukan di entri utama.

Prinsip: **lebih baik kosong daripada salah.**
