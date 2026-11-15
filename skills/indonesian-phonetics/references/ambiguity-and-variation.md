# Ambiguitas, Ragam, dan Variasi

## Daftar isi
1. Protokol RAGU · 2. Homograf e pepet/taling · 3. Singkatan & token ambigu · 4. Isyarat konteks · 5. Memilih ragam · 6. Variasi daerah · 7. Konsistensi

## 1. Protokol RAGU
Masukkan token ke RAGU (dan **jangan ubah** di teks hasil) bila:
- tidak ada di leksikon dan tidak tercakup aturan;
- ada di leksikon tetapi `ambiguous: true` dan konteks tidak menentukan;
- ada di leksikon dengan `confidence: needs_validation` dan pengguna belum mengizinkan;
- format angka/tanggal bisa dibaca lebih dari satu cara (1.5, 3.12, 02/01/2027, 10K, ¥).

Format: `token — alasan — pertanyaan konkret` (mis. "CV — lamaran kerja atau badan usaha? — 'si vi' atau 'se ve'?").
Jika pengguna meminta keputusan cepat, boleh pakai bacaan paling mungkin **asal** ditandai sebagai asumsi di tabel perubahan.

## 2. Homograf e pepet/taling
| Kata | /e/ (taling) | /ə/ (pepet) | Isyarat |
|---|---|---|---|
| teras | /te.ras/ bagian rumah | /tə.ras/ inti; "pejabat teras" | bangunan vs jabatan |
| kecap | /ke.tʃap/ saus | /kə.tʃap/ mengecap | makanan vs verba |
| seri | /se.ri/ rangkaian | /sə.ri/ imbang | film/nomor vs pertandingan |
| seret | /se.ret/ menarik | /sə.rət/ tersendat | gerakan vs keadaan |
| apel | /a.pel/ buah | /a.pəl/ upacara | makanan vs "apel pagi/siaga" |
| mental | /men.tal/ kejiwaan | /mən.tal/ terpelanting | psikologi vs benda memantul |
| per | /per/ pegas | /pər/ tiap | mekanis vs "per hari" |
| memerah | /mə.me.rah/ jadi merah | /mə.mə.rah/ memeras | warna vs susu |
| semi | /se.mi/ setengah | /sə.mi/ tunas/musim | prefiks serapan vs musim |
| sedan | /se.dan/ mobil | /sə.dan/ isak | kendaraan vs tangis |
| Serang | /se.raŋ/ kota | /sə.raŋ/ menyerang | nama tempat vs aksi |
| beruang | /bə.ru.aŋ/ hewan | /bər.u.aŋ/ punya uang (beda pemenggalan) | hewan vs keuangan |

Untuk TTS, homograf biasanya tidak perlu diubah tulisannya; tandai hanya bila mesin terbukti salah, lalu pertimbangkan diakritik PUEBI (é/ê) bila mesin mendukung.

## 3. Singkatan & token ambigu (contoh dari leksikon)
| Token | Bacaan | Isyarat |
|---|---|---|
| HP | ha pe (telepon) · tenaga kuda (mesin) · eic pi (gim) | "dari HP", "layar HP" → telepon |
| CV | si vi (lamaran) · se ve/ce ve (badan usaha) | "kirim CV", "lamar" vs "CV Maju Jaya" |
| RPM | ar pi em (monetisasi YouTube) · putaran per menit (mesin) | CTR/AdSense vs mesin/motor |
| SD | es de (sekolah) · es di (kartu memori) | "murid SD" vs "SD card" |
| ID | ai di (identitas/identifier) · i de (kode negara) | "user ID" vs domain/negara |
| AIR | eir (kata Inggris) · air /a.ir/ (kata Indonesia) · singkatan | wajib konteks |
| UI | u i (Universitas Indonesia) · yu ai (user interface) | kampus vs desain |
| KKN, PT | bacaan sama, makna beda | tidak perlu diubah untuk TTS |
| Dr. / dr. | doktor / dokter | huruf kecil = dokter; awal kalimat → RAGU |
| H. | haji · inisial "ha" | ada Hj./konteks keagamaan? |
| No. | nomor (+ angka) · "no" Inggris | diikuti angka → nomor ⚙ |
| Hal. | perihal (surat) · halaman | + angka → halaman ⚙ |
| cc | tembusan/si si (surel) · sentimeter kubik (mesin) | surel vs kendaraan |
| M (besaran) | miliar (rupiah) · million (USD) | mata uang |
| m (satuan) | meter · menit · juta | konteks |
| Make, Drive, DANA, CUDA, Keras, Java, Python, token, X | merek vs kata biasa | kapitalisasi & domain |
| ¥ | yen · yuan | negara |
| & | dan · en (Q&A) | spasi di kiri-kanan → dan |
| / | per · atau · tanggal · pecahan · URL | lihat normalization.md |

## 4. Isyarat konteks
Urutan kekuatan: (1) instruksi/kamus pengguna; (2) kolokasi langsung ("murid SD", "SD card"); (3) domain dokumen (teknologi, keuangan, pemerintahan); (4) kapitalisasi dan tanda titik; (5) frekuensi umum. Jangan memutuskan dari frekuensi saja bila makna berubah.

## 5. Memilih ragam
| Situasi | Pilihan |
|---|---|
| Naskah santai (YouTube, media sosial) | pertahankan *gue/lu/nggak/pake*; jam santai; singkatan teknologi dieja lazim |
| Narasi formal (korporat, pemerintahan, e-learning) | bentuk baku; *pukul* + 24 jam; ekspansi singkatan bila diminta |
| Siaran/berita | baku; zona waktu dieja atau lengkap |
Jangan mengubah ragam naskah tanpa diminta; ragam hanya memengaruhi pilihan bacaan simbol/angka/singkatan.

## 6. Variasi daerah
- Tidak ada logat daerah yang menjadi standar nasional; jangan menstereotipkan penutur.
- Variasi yang **tidak** mengubah makna (alofon vokal, realisasi /r/, [k]/[ʔ] akhir, /v/→[f]) boleh mengikuti persona suara.
- Variasi yang **berisiko** mengubah makna — e pepet/taling, /f/→[p] (*fakta/pakta*), /ʃ/→[s] (*syarat/sarat*), /x/→[k] (*khas/kas*), pelesapan /h/ akhir (*darah/dara*) — hindari pada narasi formal.
- Kecenderungan yang sering dilaporkan (Jawa: prenasalisasi pada sebagian nama tempat; Sunda: f/v → p; Batak: ə → e; Bali: t/d apikal; Bugis-Makassar: nasal akhir → ŋ) berstatus **needs_validation**; jangan dipakai sebagai aturan.

## 7. Konsistensi
Buat glosarium kerja per dokumen: `bentuk tulis → bacaan dipilih → alasan`. Jika satu singkatan punya dua bacaan sah (HP: ha pe / hape; CPM: si pi em / se pe em), pilih satu dan pakai di seluruh dokumen. Laporkan pilihan ini di tabel perubahan.
