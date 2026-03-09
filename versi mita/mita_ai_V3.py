import pygame
import speech_recognition as sr
from gtts import gTTS
import threading
import datetime
import os
import time
import random

pygame.init()

screen = pygame.display.set_mode((320,320))
pygame.display.set_caption("MITA AI")

BLACK = (0,0,0)
WHITE = (255,255,255)

mouth_open = False
blink = False

recognizer = sr.Recognizer()

# ganti jika mic berbeda
MIC_INDEX = 1


def speak(text):

    global mouth_open

    print("MITA:", text)

    tts = gTTS(text=text, lang="id")
    tts.save("voice.mp3")

    mouth_open = True

    os.system("mpg123 voice.mp3 > /dev/null 2>&1")

    mouth_open = False


def listen():

    try:

        with sr.Microphone(device_index=MIC_INDEX) as source:

            print("🎤 MITA mendengarkan...")

            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

        text = recognizer.recognize_google(audio, language="id-ID")

        print("Anda:", text)

        return text.lower()

    except sr.WaitTimeoutError:
        return ""

    except sr.UnknownValueError:
        return ""

    except Exception as e:
        print("Error mic:", e)
        return ""


def draw():

    screen.fill(BLACK)

    if blink:
        pygame.draw.line(screen,WHITE,(120,130),(140,130),4)
        pygame.draw.line(screen,WHITE,(180,130),(200,130),4)
    else:
        pygame.draw.circle(screen,WHITE,(130,130),8)
        pygame.draw.circle(screen,WHITE,(190,130),8)

    if mouth_open:
        pygame.draw.rect(screen,WHITE,(145,180,30,15))
    else:
        pygame.draw.line(screen,WHITE,(145,185),(175,185),3)

    pygame.display.update()


def blink_loop():

    global blink

    while True:

        time.sleep(random.randint(3,6))

        blink = True
        time.sleep(0.2)
        blink = False


def process(cmd):

    if "halo" in cmd:
        speak("Halo ada yang bisa saya bantu")

    elif "perkenalkan dirimu" in cmd:
        speak("Halo nama saya Mita AI assistant")

    elif "jam berapa" in cmd:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"Sekarang jam {now}")

    elif "tanggal berapa" in cmd:
        today = datetime.date.today()
        speak(f"Hari ini tanggal {today}")

    elif "fiturmu" in cmd:
        speak("Saya memiliki avatar pixel, animasi wajah, dan bisa menjawab pertanyaan")

    else:
        speak("Maaf saya belum mengerti")


def voice_loop():

    while True:

        cmd = listen()

        if cmd != "":
            process(cmd)

        time.sleep(0.5)


threading.Thread(target=blink_loop, daemon=True).start()
threading.Thread(target=voice_loop, daemon=True).start()

speak("Halo saya Mita AI siap digunakan")

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    draw()

pygame.quit()
