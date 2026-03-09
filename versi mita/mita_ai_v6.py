import speech_recognition as sr
import subprocess
import asyncio
import edge_tts

VOICE = "id-ID-GadisNeural"

recognizer = sr.Recognizer()
recognizer.energy_threshold = 250
recognizer.dynamic_energy_threshold = True


# ================= SPEAK =================

async def speak_async(text):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save("mita_voice.mp3")

    subprocess.run(["mpg123", "-q", "mita_voice.mp3"])


def speak(text):
    print("MITA:", text)
    asyncio.run(speak_async(text))


# ================= LISTEN =================

def listen():

    with sr.Microphone() as source:

        print("🎤 Mendengarkan...")

        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)

            text = recognizer.recognize_google(audio, language="id-ID")

            print("ANDA:", text)

            return text.lower()

        except sr.WaitTimeoutError:
            return ""

        except sr.UnknownValueError:
            print("❓ Tidak mengerti")
            return ""

        except Exception as e:
            print("ERROR:", e)
            return ""


# ================= BRAIN =================

def brain(text):

    if "halo" in text:
        speak("Halo, ada yang bisa saya bantu")

    elif "perkenalkan dirimu" in text:
        speak("Halo, saya Mita. Asisten AI yang dibuat untuk membantu anda")

    elif "jam berapa" in text:
        from datetime import datetime
        now = datetime.now().strftime("%H:%M")
        speak(f"Sekarang jam {now}")

    elif "terima kasih" in text:
        speak("Sama sama, senang membantu")

    elif "siapa kamu" in text:
        speak("Saya Mita, AI yang tinggal di laptop anda")

    elif "apa itu ai" in text:
        speak("AI adalah kecerdasan buatan yang dibuat untuk membantu manusia")

    elif text != "":
        speak("Maaf saya belum mengerti pertanyaan itu")


# ================= MAIN =================

def main():

    print("🔧 Mencari microphone...")

    for i, name in enumerate(sr.Microphone.list_microphone_names()):
        print(i, name)

    speak("Halo saya Mita AI versi enam, siap membantu")

    while True:

        text = listen()

        if text != "":
            brain(text)


# ================= RUN =================

if __name__ == "__main__":
    main()
