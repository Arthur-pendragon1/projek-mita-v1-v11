import pygame
import threading
import time
import random
from gtts import gTTS
import os
import datetime
import webbrowser

pygame.init()

WIDTH = 320
HEIGHT = 320

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MITA AI")

BLACK = (0,0,0)
WHITE = (255,255,255)

emotion = "idle"
mouth_open = False
blink_timer = 0


def speak(text):

    global mouth_open

    print("MITA:", text)

    tts = gTTS(text=text, lang="id")
    tts.save("voice.mp3")

    mouth_open = True
    os.system("mpg123 voice.mp3 > /dev/null 2>&1")
    mouth_open = False


def draw_face():

    global blink_timer

    screen.fill(BLACK)

    eye_y = 130

    if blink_timer > 0:
        pygame.draw.line(screen, WHITE,(120,eye_y),(140,eye_y),4)
        pygame.draw.line(screen, WHITE,(180,eye_y),(200,eye_y),4)
    else:
        pygame.draw.circle(screen,WHITE,(130,eye_y),8)
        pygame.draw.circle(screen,WHITE,(190,eye_y),8)

    if mouth_open:
        pygame.draw.rect(screen,WHITE,(145,180,30,15))
    else:
        pygame.draw.line(screen,WHITE,(145,185),(175,185),3)

    if emotion == "happy":
        pygame.draw.arc(screen,WHITE,(130,170,60,40),3.14,0,3)

    elif emotion == "sad":
        pygame.draw.arc(screen,WHITE,(130,190,60,40),0,3.14,3)

    elif emotion == "angry":
        pygame.draw.line(screen,WHITE,(115,120),(135,130),3)
        pygame.draw.line(screen,WHITE,(205,120),(185,130),3)

    elif emotion == "surprised":
        pygame.draw.circle(screen,WHITE,(160,190),10)

    pygame.display.update()


def process(command):

    global emotion

    if "halo" in command:

        emotion = "happy"
        speak("Halo, ada yang bisa saya bantu")

    elif "perkenalkan dirimu" in command:

        emotion = "happy"
        speak("Halo, nama saya Mita. Saya adalah asisten AI robot")

    elif "apa saja fiturmu" in command:

        emotion = "proud"
        speak("Saya memiliki avatar pixel hidup, delapan emosi, animasi mulut saat berbicara, dan dapat menjawab berbagai pertanyaan")

    elif "apa yang bisa kamu lakukan" in command:

        emotion = "happy"
        speak("Saya bisa menjawab pertanyaan, membuka website, memberi informasi waktu dan menjadi asisten virtual")

    elif "siapa yang membuatmu" in command:

        emotion = "happy"
        speak("Saya dibuat oleh Rifqi menggunakan python")

    elif "jam berapa" in command:

        emotion = "idle"
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"Sekarang jam {now}")

    elif "tanggal berapa" in command:

        emotion = "idle"
        today = datetime.date.today()
        speak(f"Hari ini tanggal {today}")

    elif "buka youtube" in command:

        emotion = "happy"
        speak("Membuka youtube")
        webbrowser.open("https://youtube.com")

    elif "buka google" in command:

        emotion = "happy"
        speak("Membuka google")
        webbrowser.open("https://google.com")

    elif "apa itu ai" in command:

        emotion = "thinking"
        speak("Artificial intelligence adalah teknologi yang membuat komputer dapat meniru kecerdasan manusia")

    else:

        emotion = "confused"
        speak("Maaf saya belum mengerti pertanyaan itu")


def idle_animation():

    global blink_timer

    while True:

        time.sleep(random.randint(3,6))

        blink_timer = 5
        time.sleep(0.2)
        blink_timer = 0


threading.Thread(target=idle_animation, daemon=True).start()

print("MITA AI siap digunakan")

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:
                process("halo")

            if event.key == pygame.K_2:
                process("perkenalkan dirimu")

            if event.key == pygame.K_3:
                process("apa saja fiturmu")

            if event.key == pygame.K_4:
                process("jam berapa")

            if event.key == pygame.K_5:
                process("apa itu ai")

    draw_face()
