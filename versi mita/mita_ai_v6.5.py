import speech_recognition as sr
import asyncio
import edge_tts
import subprocess
import threading
from datetime import datetime

VOICE = "id-ID-GadisNeural"

recognizer = sr.Recognizer()
recognizer.energy_threshold = 200
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.6


# ================= SPEAK ENGINE =================

def speak(text):

    def run():
        print("MITA:", text)

        async def voice():
            communicate = edge_tts.Communicate(text, VOICE)
            await communicate.save("mita_voice.mp3")

        asyncio.run(voice())

        subprocess.run(["mpg123", "-q", "mita_voice.mp3"])

    threading.Thread(target=run).start()


# ================= MICROPHONE SETUP =================

print("\nMencari Microphone...\n")

mic_list = sr.Microphone.list_microphone_names()

for i, mic in enumerate(mic_list):
    print(i, mic)

MIC_INDEX = None   # otomatis pilih mic terbaik

mic = sr.Microphone(device_index=MIC_INDEX)


# ================= LISTEN ENGINE =================

def listen():

    with mic as source:

        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

            text = recognizer.recognize_google(
                audio,
                language="id-ID"
            )

            print("ANDA:", text)

            return text.lower()

        except sr.WaitTimeoutError:
            return ""

        except sr.UnknownValueError:
            return ""

        except Exception as e:
            print("ERROR:", e)
            return ""


# ================= BRAIN =================

def brain(text):

    if "halo" in text:
        speak("Halo, ada yang bisa saya bantu")

    elif "mita" in text:
        speak("Ya, saya mendengarkan")

    elif "perkenalkan dirimu" in text:
        speak("Halo, saya Mita. Asisten AI yang sedang dikembangkan")

    elif "jam berapa" in text:
        now = datetime.now().strftime("%H:%M")
        speak(f"Sekarang jam {now}")

    elif "terima kasih" in text:
        speak("Sama sama")

    elif "siapa kamu" in text:
        speak("Saya Mita, AI yang hidup di laptop anda")

    elif "fitur kamu apa" in text:
        speak("Saya bisa menjawab pertanyaan dasar, berbicara, dan sedang terus dikembangkan")

    elif text != "":
        speak("Maaf saya belum memahami itu")


# ================= MAIN =================

def main():

    print("\nKalibrasi microphone...")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)

    print("Kalibrasi selesai")

    speak("Halo, saya Mita versi enam koma lima, siap membantu")

    while True:

        text = listen()

        if text != "":
            brain(text)


# ================= RUN =================

if __name__ == "__main__":
    main()
