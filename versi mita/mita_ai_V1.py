import speech_recognition as sr
from gtts import gTTS
import os
import datetime
import webbrowser
import time

recognizer = sr.Recognizer()

# =========================
# TEXT TO SPEECH
# =========================
def speak(text):

    print("MITA:", text)

    try:
        file = "/tmp/mita_voice.mp3"

        tts = gTTS(text=text, lang="id")
        tts.save(file)

        os.system(f"mpg123 {file} > /dev/null 2>&1")

    except:
        print("Error memainkan suara")


# =========================
# MICROPHONE LISTEN
# =========================
def listen():

    with sr.Microphone() as source:

        print("🎤 Silakan bicara...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
        except:
            return ""

    try:

        text = recognizer.recognize_google(audio, language="id-ID")

        print("Anda:", text)

        return text.lower()

    except:
        print("Tidak mengerti")
        return ""


# =========================
# COMMAND PROCESSOR
# =========================
def process(command):

    if "halo" in command:
        speak("Halo Rifqi, ada yang bisa saya bantu")

    elif "perkenalkan dirimu" in command:
        speak("Halo, nama saya Mita. Saya adalah asisten AI yang dibuat oleh Rifqi")

    elif "siapa kamu" in command:
        speak("Saya adalah asisten virtual bernama Mita")

    elif "siapa yang membuatmu" in command:
        speak("Saya dibuat oleh Rifqi menggunakan bahasa pemrograman python")

    elif "jam berapa" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"Sekarang jam {now}")

    elif "tanggal berapa" in command:
        today = datetime.date.today()
        speak(f"Hari ini tanggal {today}")

    elif "hari apa" in command:
        day = datetime.datetime.now().strftime("%A")
        speak(f"Hari ini adalah hari {day}")

    elif "buka youtube" in command:
        speak("Membuka youtube")
        webbrowser.open("https://youtube.com")

    elif "buka google" in command:
        speak("Membuka google")
        webbrowser.open("https://google.com")

    elif "buka github" in command:
        speak("Membuka github")
        webbrowser.open("https://github.com")

    elif "apa itu ai" in command:
        speak("Artificial intelligence adalah teknologi yang memungkinkan komputer meniru kecerdasan manusia")

    elif "siapa presiden indonesia" in command:
        speak("Presiden Indonesia saat ini adalah Prabowo Subianto")

    elif "apa itu python" in command:
        speak("Python adalah bahasa pemrograman yang populer untuk pengembangan software dan kecerdasan buatan")

    elif "terima kasih" in command:
        speak("Sama sama, senang membantu")

    elif "cari" in command:

        query = command.replace("cari", "")
        speak(f"Mencari {query} di google")

        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif "keluar" in command:
        speak("Baik sampai jumpa")
        return False

    else:
        speak("Maaf saya belum mengerti")

    return True


# =========================
# MAIN PROGRAM
# =========================

print("===== MITA AI ASSISTANT =====")

speak("Halo, saya Mita AI assistant. Sistem siap digunakan")

running = True

while running:

    command = listen()

    if command != "":
        running = process(command)

    time.sleep(1)
