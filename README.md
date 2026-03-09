# MITA AI 🤖

### Simple Python Voice Assistant with Animated Avatar

MITA adalah **AI assistant sederhana berbasis Python** yang dapat mendengar suara pengguna, menjawab pertanyaan, dan menampilkan **avatar animasi di layar**.

Proyek ini dibuat sebagai **eksperimen pengembangan AI desktop** untuk mempelajari:

* Voice Recognition
* Text To Speech
* Interactive Character UI
* Python AI Assistant

MITA terus dikembangkan dari prototype sederhana hingga menjadi **AI assistant dengan avatar animasi**.

---

# ✨ Fitur MITA

Beberapa kemampuan MITA saat ini:

* 🎤 Voice Recognition (mendengar suara pengguna)
* 🧠 Basic AI Brain System
* 🔊 Text To Speech
* 🌐 Internet Search menggunakan Wikipedia
* 🧑‍🎤 Avatar AI dengan animasi
* 👀 Animasi mata berkedip
* 👄 Animasi mulut saat berbicara
* 🔇 Noise handling untuk microphone

---

# 📜 MITA AI Development Log

Berikut perkembangan MITA dari versi pertama hingga versi terbaru.

## V1 – Prototype

MITA masih sangat sederhana. Program hanya menampilkan teks di terminal dan belum memiliki suara maupun UI.

---

## V2 – Text to Speech

MITA mulai bisa berbicara menggunakan sistem Text To Speech sehingga jawaban tidak hanya berupa teks.

Library:
pyttsx3

---

## V3 – Voice Recognition

MITA mulai bisa mendengar suara pengguna dan mengubah suara menjadi teks.

Library:
SpeechRecognition
pyaudio

---

## V4 – Brain System

Ditambahkan sistem **brain** agar MITA dapat memahami beberapa perintah dasar seperti:

* salam
* menanyakan waktu
* pertanyaan sederhana

Library:
datetime (bawaan Python)

---

## V5 – Internet Search

MITA dapat mencari jawaban dari internet menggunakan Wikipedia.

Library:
wikipedia

---

## V6 – Avatar UI

MITA mulai memiliki **avatar AI di layar** menggunakan pygame.

Library:
pygame

---

## V7 – Emotion System

Avatar MITA memiliki beberapa ekspresi seperti:

* idle
* talking
* thinking
* blink

---

## V8 – Lip Movement

Mulut avatar MITA mulai bergerak ketika sedang berbicara.

---

## V9 – Noise Handling

MITA mulai bisa mengabaikan noise seperti:

* suara angin
* suara pantulan dari speaker
* suara latar yang tidak penting

---

## V10 – Better Voice

Sistem suara diperbaiki menggunakan **Google Text To Speech** agar terdengar lebih natural.

Library:
gTTS

---

## V11 – Anime Pixel Avatar

MITA memiliki **avatar pixel AI yang lebih hidup** dengan animasi:

* mata berkedip
* mulut bergerak saat berbicara
* ekspresi berpikir

Assets:

* idle.png
* blink.png
* talk1.png
* talk2.png
* think.png

---

# 📦 Dependencies untuk MITA V11

Install semua library berikut sebelum menjalankan MITA:

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

# 📂 Struktur Project

```
mita_v11

run_mita.py
mita_brain.py
mita_listen.py
mita_voice.py
mita_ui.py

assets/
  idle.png
  blink.png
  talk1.png
  talk2.png
  think.png
```

---

# 🚀 Cara Menjalankan MITA

Masuk ke folder project:

```
cd mita_v11
```

Jalankan program:

```
python run_mita.py
```

---

# 👨‍💻 Developer

MITA AI dikembangkan oleh:

**Rifqi**

Proyek ini dibuat sebagai **eksperimen pengembangan AI assistant menggunakan Python**.

---

# 📜 Copyright

Hak cipta © 2026 oleh Rifqi.
Semua hak dilindungi undang-undang.

---

⭐ Jika kamu menyukai proyek ini, jangan lupa memberikan **star di GitHub**!
