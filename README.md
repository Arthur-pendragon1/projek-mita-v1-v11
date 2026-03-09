# Hak Cipta MITA AI

Hak cipta © 2026 oleh Rifqi. Semuanya dilindungi undang-undang.

File ini dibuat untuk diposting di GitHub sebagai catatan hak cipta dan log pengembangan MITA.

---

## MITA AI Development Log

MITA adalah AI assistant sederhana yang dibuat menggunakan Python.
AI ini memiliki kemampuan mendengar suara, menjawab pertanyaan, dan menampilkan avatar di layar.

### Versi Pengembangan MITA

**V1 – Prototype**
- MITA masih sangat sederhana. Program hanya menampilkan teks di terminal dan belum memiliki suara maupun UI.

**V2 – Text to Speech**
- MITA mulai bisa berbicara menggunakan sistem Text To Speech sehingga jawaban tidak hanya berupa teks.
- Library: pyttsx3

**V3 – Voice Recognition**
- MITA mulai bisa mendengar suara pengguna dan mengubah suara menjadi teks.
- Library: SpeechRecognition, pyaudio

**V4 – Brain System**
- Ditambahkan sistem "brain" agar MITA dapat memahami beberapa perintah dasar seperti salam dan menanyakan waktu.
- Library: datetime (bawaan python)

**V5 – Internet Search**
- MITA bisa mencari jawaban dari internet menggunakan Wikipedia.
- Library: wikipedia

**V6 – Avatar UI**
- MITA mulai memiliki tampilan avatar di layar menggunakan pygame.
- Library: pygame

**V7 – Emotion System**
- Avatar MITA memiliki beberapa ekspresi seperti idle, talking, thinking, dan blink.

**V8 – Lip Movement**
- Mulut avatar MITA bergerak ketika sedang berbicara.

**V9 – Noise Handling**
- MITA mulai bisa mengabaikan noise seperti suara angin atau suara pantulan dari speaker.

**V10 – Better Voice**
- Sistem suara diperbaiki menggunakan Google Text To Speech agar terdengar lebih natural.
- Library: gTTS

**V11 – Anime Pixel Avatar**
- MITA memiliki avatar pixel yang lebih hidup dengan animasi mata berkedip dan mulut bergerak.
- Assets:
  - idle.png
  - blink.png
  - talk1.png
  - talk2.png
  - think.png

### Dependencies untuk MITA V11

```
pip install pygame
pip install SpeechRecognition
pip install pyaudio
pip install pyttsx3
pip install gTTS
pip install wikipedia
```

Tambahan untuk Linux:

```
sudo apt install portaudio19-dev
```

---

Terima kasih telah menggunakan MITA AI!
