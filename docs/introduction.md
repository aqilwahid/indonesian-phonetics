# Pengantar

## Apa ini

**Indonesian Phonetics** adalah basis pengetahuan terstruktur tentang fonetik, fonologi, dan pelafalan bahasa Indonesia yang dirancang untuk dua jenis pembaca sekaligus:

- **Manusia** — linguis, guru, penulis naskah, voice-over artist, editor caption.
- **Mesin** — sistem NLP, Text-to-Speech (TTS), Speech Recognition (ASR), dan AI Agent (lewat [AI Skill](../skills/indonesian-phonetics/SKILL.md)).

## Ruang lingkup

| Domain | Lokasi |
|---|---|
| Fondasi fonetik (alat ucap, IPA, fonem/alofon, transkripsi) | [phonetics.md](phonetics.md), [ipa.md](ipa.md) |
| Fonologi (sistem bunyi, suku kata, fonotaktik, prosodi, proses) | [phonology.md](phonology.md), folder [knowledge/](../knowledge/) |
| Aturan pelafalan (grafem–fonem, singkatan, serapan, pengecualian) | [pronunciation-rules.md](pronunciation-rules.md) |
| Kamus pelafalan praktis (787 entri, 8 berkas JSON) | folder [dictionary/](../dictionary/) |
| Variasi regional dan ragam | [knowledge/regional-variations.md](../knowledge/regional-variations.md) |
| Standar data dan skema | [data-standards.md](data-standards.md), [schemas/](../schemas/) |
| Asal-usul data | [sources.md](sources.md), [zip-reference-analysis.md](zip-reference-analysis.md) |

Di luar cakupan (saat ini): rekaman audio, model akustik, transkripsi korpus besar, dan pelafalan bahasa daerah itu sendiri (yang dicatat hanya pengaruhnya pada bahasa Indonesia).

## Tiga tingkat klaim

Setiap dokumen memisahkan jenis informasi dengan label:

| Label | Arti | Contoh |
|---|---|---|
| **[Fakta]** | Didukung sumber yang dirujuk (normatif atau ilmiah) | Enam fonem vokal /i e ə a o u/ |
| **[Variasi]** | Realisasi yang berbeda antarpenutur, daerah, atau ragam | *pakai* → *pake* dalam ragam santai |
| **[Rekomendasi]** | Saran praktis repo (interpretasi), terutama untuk TTS | Ekspansi *dll.* sebelum dikirim ke TTS |

Di dataset, pembedaan ini diwujudkan lewat field `confidence` (`standard`, `attested`, `derived`, `needs_validation`) dan `provenance` (`zip-reference`, `external-source`, `interpretation`, `mixed`). Lihat [data-standards.md](data-standards.md).

## Status validasi

**Belum ada entri yang ditinjau linguis atau panel penutur independen** (`review_status: unreviewed` untuk seluruh 787 entri). Data telah lolos validasi skema, konsistensi, dan uji otomatis, tetapi itu bukan validasi linguistik. Sumber yang tidak dibuka langsung saat build ditandai di [sources.md](sources.md). Perlakukan dataset sebagai **draf berkualitas yang terdokumentasi**, bukan rujukan normatif.

## Cara membaca repo ini

1. Pemula: mulai dari [phonetics.md](phonetics.md) → [ipa.md](ipa.md) → [knowledge/vowels.md](../knowledge/vowels.md).
2. Developer/TTS: [data-standards.md](data-standards.md) → [dictionary/](../dictionary/) → [examples/](../examples/).
3. Pengguna AI Agent: [skills/indonesian-phonetics/SKILL.md](../skills/indonesian-phonetics/SKILL.md).
4. Kontributor: [CONTRIBUTING.md](../CONTRIBUTING.md).
