import speech_recognition as sr
import subprocess
import asyncio
import edge_tts
from datetime import datetime

VOICE = "id-ID-GadisNeural"

recognizer = sr.Recognizer()
recognizer.energy_threshold = 200
recognizer.dynamic_energy_threshold = True


# ================= VOICE =================

async def speak_async(text):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save("voice.mp3")
    subprocess.run(["mpg123", "-q", "voice.mp3"])


def speak(text):
    print("MITA:", text)
    asyncio.run(speak_async(text))


# ================= MICROPHONE SETUP =================

print("\nMencari Microphone...\n")

mic_list = sr.Microphone.list_microphone_names()

for i, mic in enumerate(mic_list):
    print(f"{i} : {mic}")

MIC_INDEX = 0   # ubah jika mic anda bukan 0

mic = sr.Microphone(device_index=MIC_INDEX)


# ================= LISTEN =================

def listen():

    with mic as source:

        print("\n🎤 Mendengarkan...")

        try:

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=6
            )

            text = recognizer.recognize_google(
                audio,
                language="id-ID"
            )

            print("ANDA:", text)

            return text.lower()

        except sr.WaitTimeoutError:
            print("⏳ Tidak ada suara")
            return ""

        except sr.UnknownValueError:
            print("❓ Tidak mengerti suara")
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
        now = datetime.now().strftime("%H:%M")
        speak(f"Sekarang jam {now}")

    elif "terima kasih" in text:
        speak("Sama sama")

    elif "siapa kamu" in text:
        speak("Saya Mita, AI yang tinggal di laptop anda")

    elif text != "":
        speak("Maaf saya belum memahami pertanyaan itu")


# ================= MAIN =================

def main():

    print("\nKalibrasi microphone...")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=2)

    print("Kalibrasi selesai\n")

    speak("Halo saya Mita, saya siap membantu")

    while True:

        text = listen()

        if text != "":
            brain(text)


# ================= RUN =================

if __name__ == "__main__":
    main()
