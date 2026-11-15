# Aturan Pelafalan untuk Agen

Prosedur keputusan membaca tulisan. Sumber: EYD V (2022), PUEBI (2015), Pedoman Umum Pembentukan Istilah (2007), korpus VO HDI (2026, observasi praktik TTS). Label: **[Fakta]**, **[Variasi]**, **[Rekomendasi]**.

## Daftar isi
1. Grafem → fonem · 2. Huruf *e* · 3. Singkatan, akronim, initialism · 4. Kata asing dan serapan · 5. Ejaan lama nama diri · 6. Nama merek dan URL · 7. Pembentukan kata dengan singkatan

## 1. Grafem → fonem
**[Fakta]** a /a/ · b /b/ (akhir [p]) · c /tʃ/ · d /d/ (akhir [t]) · e /e/ atau /ə/ · f /f/ · g /g/ · h /h/ · i /i/ · j /dʒ/ · k /k/ (akhir kata asli [ʔ]) · kh /x/ · l /l/ · m /m/ · n /n/ · ng /ŋ/ · ngg /ŋg/ · ny /ɲ/ · o /o/ · p /p/ · q /k/ · r /r/ · s /s/ · sy /ʃ/ · t /t/ · u /u/ · v /v/≈[f] · w /w/ · x /ks/ · y /j/ · z /z/ · ai au oi ei = diftong (bisa hiatus) · eu = [ɘ] · ' = /ʔ/.

## 2. Huruf *e*
**[Fakta]** Tidak ada aturan ejaan untuk /e/ vs /ə/.
**[Rekomendasi]** Prosedur:
1. Cari di leksikon (`pronunciation-dictionary.json` / `lexicon.json`).
2. Prefiks *ber-, ter-, me(N)-, pe(N)-, ke-, se-* → /ə/ pada prefiksnya.
3. Homograf (subkategori `homograph`): putuskan dari konteks; tanpa konteks → RAGU.
4. Selain itu: jangan isi IPA; untuk TTS biarkan ejaan biasa.

## 3. Singkatan, akronim, initialism

| Jenis | Bacaan | Contoh |
|---|---|---|
| Initialism | dieja | KTP → ka te pe |
| Akronim | dibaca kata | Polri → polri; NIK → nik; QRIS → kris (resmi BI) |
| Alfanumerik | campuran | MP4 → em pe empat; A4 → a empat; S1 → es satu |
| Singkatan bertitik | ekspansi | dll. → dan lain-lain; s.d. → sampai dengan; a.n. → atas nama |

**Nama huruf Indonesia (PUEBI):** a be ce de e ef ge ha i je ka el em en o pe **ki** er es te u **ve** (umum: fe) we **eks** **ye** **zet**.
**Nama huruf Inggris (kanonik repo):** ei bi si di i ef ji eic ai jei kei el em en o pi kyu ar es ti yu vi dabelyu eks wai zet.

**[Fakta — observasi korpus HDI]** Initialism Indonesia selalu nama huruf Indonesia. Initialism Inggris bervariasi: CTR = si ti ar, CEO = si i o, DM = di em (Inggris); PDF = pe de ef, API = a pe i, SMS = es em es, ATM = a te em (Indonesia); FAQ = ef a kyu, ER = i er (campuran). C kadang "se" (warisan Belanda): CPM = se pe em, AC = a se.

**Pohon keputusan [Rekomendasi]:**
1. Kamus rumah pengguna? → pakai.
2. Ada di leksikon & tidak ambigu & bukan `needs_validation`? → pakai `respelling` (tts) / `spoken_form` (spoken).
3. Ada di leksikon tetapi ambigu? → pakai `disambiguation` + konteks; jika tetap ragu → RAGU.
4. Initialism asal Indonesia (lembaga, dokumen, pendidikan)? → nama huruf Indonesia.
5. Initialism Inggris domain teknologi/kreator? → nama huruf Inggris lazim, **tetapi tandai** jika tidak ada data.
6. Bisa dibaca sebagai kata (pola KVK/KVKV, ≤ 5 huruf, mis. "SINTA", "PIN")? → jangan menebak; RAGU.
7. Teknik TTS teramati: akronim yang harus dibaca sebagai kata ditulis huruf kecil di teks TTS (nik, sim, zip).

**Gelar:** dalam pengumuman lisan lazim dieja (S.Kom. → es kom, M.T. → em te); ekspansi (sarjana komputer) untuk upacara resmi. **dr.** = dokter; **Dr.** = doktor (gelar akademik) — awas di awal kalimat.

## 4. Kata asing dan serapan
- **Serapan berejaan Indonesia** dibaca sesuai ejaan: *komputer, sistem, kualitas* (lazim [kwalitas]), *survei*. Bentuk baku: analisis, praktik, risiko, standar, objek, karier, apotek, kuitansi.
- **Kata Inggris apa adanya**: biarkan bila mesin membacanya benar dan audiens terbiasa (*upload, views*). Ganti dengan respelling hanya bila tercatat di leksikon atau terbukti salah baca. Contoh respelling teruji HDI: Shorts → syorts, AdSense → ed sens, Reels → rils, deploy → diploi, WhatsApp → wotsap, Google → gugel.
- **Konvensi respelling**: ejaan Indonesia; c = /tʃ/, j = /dʒ/, y = /j/, sy = /ʃ/; huruf e tetap ambigu.
- **Padanan Indonesia** (unggah, tagar, daring) adalah keputusan penulis, bukan tugas skill.
- **Serapan Arab**: pertahankan /x ʃ z f q ʔ/ pada ragam baku (*khusus, syukur, zakat, maaf* /ma.ʔaf/, *Al-Qur'an*).

## 5. Ejaan lama nama diri
oe → /u/ (*Soekarno*), dj → /dʒ/ (*Gadjah Mada*), tj → /tʃ/, j (lama) → /j/ (*Soerabaja*), nj → /ɲ/, sj → /ʃ/, ch → /x/. Jangan ubah ejaan nama di teks tampilan.

## 6. Nama merek dan URL
- Merek: ikuti bacaan resmi/lazim; jika tidak diketahui → biarkan + RAGU.
- Domain: titik → "dot" (lazim) atau "titik" (formal): konten.com → konten dot com.
- Surel: @ → "et"; handle media sosial di narasi → baca nama tanpa "@", mis. @hidupdariinternet → hidup dari internet.
- Huruf kapital di tengah nama (CamelCase: ManyChat, LinkedIn) dibaca sebagai frasa.

## 7. Pembentukan kata dengan singkatan
Prefiks Indonesia + singkatan: prefiks dibaca biasa, singkatan tetap: di-DM → di di em; nge-share → nge syer (informal). Reduplikasi dengan tanda hubung dibaca diulang: *anak-anak*.
