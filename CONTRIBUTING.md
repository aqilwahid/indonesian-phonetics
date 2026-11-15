# Panduan Kontribusi

Terima kasih ingin berkontribusi. Prioritas proyek ini: **akurasi linguistik, konsistensi data, dan kejujuran tentang ketidakpastian** — bukan jumlah entri.

## Jenis kontribusi yang paling dibutuhkan

1. **Validasi linguistik** — meninjau entri `unreviewed`, terutama kualitas *e* dan IPA (lihat [docs/sources.md](docs/sources.md) untuk sumber yang belum dicek: `accessed_in_build: false`).
2. **Rujukan penelitian** untuk variasi regional (saat ini sebagian besar `needs_validation`).
3. **Bukti TTS** — hasil uji mesin TTS (sebut mesin, model, suara, tanggal, metode cek).
4. Entri baru dengan sumber yang jelas.

## Alur kerja

```bash
pip install -r requirements.txt
# 1. edit dictionary/*.json (JANGAN edit skills/.../assets/lexicon.json)
# 2. bangun ulang leksikon skill
python scripts/build-skill-assets.py
# 3. jalankan semua pemeriksaan
python scripts/validate-data.py
python scripts/validate-dictionary.py --stats
python scripts/run-tests.py
python scripts/check-repo.py
```

Semua pemeriksaan juga berjalan otomatis di GitHub Actions (`.github/workflows/validate.yml`).

## Menambah entri

1. Pilih berkas sesuai kategori ([docs/data-standards.md](docs/data-standards.md#1-berkas)).
2. Pakai id berikutnya (`prefix-NNNN`), berurutan.
3. Isi semua field wajib. `normalized_text` = huruf kecil + spasi tunggal dari `text`.
4. **IPA**: isi hanya jika Anda yakin dan ada dasarnya; selain itu `null` + `ipa_note`.
5. **Sumber**: tambahkan ke `dictionary/meta/sources.json` bila belum ada, lalu perbarui `docs/sources.md`.
6. **Confidence**: `standard` hanya bila sumber normatif menyatakannya; `attested` bila ada bukti pemakaian; `derived` bila diturunkan aturan; selain itu `needs_validation`.
7. **Variasi**: catat di `variants` dengan `context`; tandai `meaning_changing` bila maknanya berbeda dan set `ambiguous: true` + `disambiguation`.
8. Tambahkan kasus uji di `tests/pronunciation-tests.json` untuk perilaku baru.

## Meninjau entri (`review_status: reviewed`)

- Cek sumber asli (KBBI, EYD V, literatur).
- Ubah `review_status` ke `reviewed` dan tulis di `notes`: `review: <nama/handle>, <tanggal>, <sumber yang dicek>`.
- Catat di [CHANGELOG.md](CHANGELOG.md).

## Aturan isi

- Dokumentasi berbahasa Indonesia; istilah teknis Inggris boleh dalam kurung.
- Pisahkan **[Fakta]**, **[Variasi]**, dan **[Rekomendasi]**.
- Jangan menggeneralisasi satu logat daerah sebagai standar.
- Jangan menyalin teks berhak cipta (kamus, buku, ebook). Fakta boleh diadopsi dengan atribusi dan kata-kata sendiri.
- Jangan menyertakan audio, data pribadi, kunci API, atau berkas referensi berlisensi pribadi.

## Pesan commit

Gunakan format ringkas: `data: tambah 12 istilah keamanan`, `docs: perbaiki contoh asimilasi nasal`, `skill: tangani format jam 19:00`, `fix: ...`.
