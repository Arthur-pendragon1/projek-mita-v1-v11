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
pygame.display.set_caption("MITA AI V5.1")

BLACK=(0,0,0)
WHITE=(255,255,255)

mouth_open=False
blink=False
emotion="idle"

recognizer=sr.Recognizer()

MIC_INDEX=None   # otomatis detect mic


# =====================
# SPEAK
# =====================

def speak(text):

    global mouth_open

    print("MITA:",text)

    tts=gTTS(text=text,lang="id")
    tts.save("voice.mp3")

    mouth_open=True

    os.system("mpg123 voice.mp3 > /dev/null 2>&1")

    mouth_open=False


# =====================
# MIC CALIBRATION
# =====================

def calibrate():

    global recognizer

    with sr.Microphone(device_index=MIC_INDEX) as source:

        print("🔧 Kalibrasi mikrofon...")

        recognizer.adjust_for_ambient_noise(source, duration=2)

        recognizer.energy_threshold = recognizer.energy_threshold * 0.8
        recognizer.dynamic_energy_threshold = True

        print("Threshold:", recognizer.energy_threshold)


# =====================
# LISTEN
# =====================

def listen():

    try:

        with sr.Microphone(device_index=MIC_INDEX) as source:

            print("🎤 Mendengarkan...")

            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio, language="id-ID")

        print("Anda:",text)

        return text.lower()

    except sr.UnknownValueError:
        return ""

    except Exception as e:
        print("Mic error:",e)
        return ""


# =====================
# DRAW FACE
# =====================

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


# =====================
# BLINK LOOP
# =====================

def blink_loop():

    global blink

    while True:

        time.sleep(random.randint(3,6))

        blink=True
        time.sleep(0.2)
        blink=False


# =====================
# PROCESS COMMAND
# =====================

def process(cmd):

    global emotion

    if "halo" in cmd:

        emotion="happy"
        speak("Halo ada yang bisa saya bantu")

    elif "perkenalkan dirimu" in cmd:

        speak("Halo nama saya Mita AI assistant")

    elif "siapa kamu" in cmd:

        speak("Saya adalah asisten virtual bernama Mita")

    elif "fiturmu" in cmd:

        speak("Saya memiliki avatar pixel hidup dan dapat menjawab berbagai pertanyaan")

    elif "jam berapa" in cmd:

        now=datetime.datetime.now().strftime("%H:%M")
        speak(f"Sekarang jam {now}")

    elif "tanggal berapa" in cmd:

        today=datetime.date.today()
        speak(f"Hari ini tanggal {today}")

    elif "apa itu ai" in cmd:

        speak("Artificial intelligence adalah teknologi yang memungkinkan komputer berpikir seperti manusia")

    elif "terima kasih" in cmd:

        speak("Sama sama senang membantu")

    else:

        speak("Maaf saya belum mengerti")


# =====================
# VOICE LOOP
# =====================

def voice_loop():

    while True:

        cmd=listen()

        if cmd!="":
            process(cmd)


# =====================
# START SYSTEM
# =====================

calibrate()

threading.Thread(target=blink_loop,daemon=True).start()
threading.Thread(target=voice_loop,daemon=True).start()

speak("Halo saya Mita AI siap digunakan")


# =====================
# MAIN LOOP
# =====================

running=True

while running:

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            running=False

    draw()

pygame.quit()
