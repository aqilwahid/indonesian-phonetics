# Changelog

Format mengikuti [Keep a Changelog](https://keepachangelog.com/id-ID/1.1.0/) dan [Semantic Versioning](https://semver.org/lang/id/).

## [1.0.0] — 2026-11-15

### Ditambahkan
- **Knowledge base**: `docs/` (pengantar, fonetik, fonologi, IPA, aturan pelafalan, standar data, sumber, analisis referensi ZIP) dan `knowledge/` (vokal, konsonan, diftong, suku kata, tekanan & intonasi, proses fonologis, variasi regional).
- **Dataset** 787 entri dalam 8 berkas JSON (`dictionary/`), dengan registri sumber (22 sumber) dan taksonomi terkendali.
- **Skema** JSON Schema 2020-12 untuk dataset, sumber, dan kasus uji.
- **AI Skill** `skills/indonesian-phonetics/` (Agent Skills): `SKILL.md`, 6 berkas `references/`, leksikon terkompilasi, skrip `lookup.py` dan `normalize.py`.
- **Kasus uji** 92 kasus (`tests/pronunciation-tests.json`) mencakup kata umum, singkatan, akronim, serapan, teknologi, angka & uang, simbol, tanggal & jam, ambiguitas, variasi, IPA, dan ketidakpastian.
- **Skrip QA**: `validate-data.py`, `validate-dictionary.py`, `run-tests.py`, `check-repo.py`, `build-skill-assets.py`; GitHub Actions.
- Adopsi fakta dari materi referensi "Voice Over AI pakai ElevenLabs" (Hidup dari Internet, 2026): 153/153 entri kamus terwakili; hasil 18 Galeri Tes dicatat di `tts_notes`.

### Catatan
- Seluruh entri berstatus `review_status: unreviewed`. Belum ada validasi oleh linguis atau panel penutur.
