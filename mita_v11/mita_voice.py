from gtts import gTTS
import pygame
import tempfile
import os

from mita_ui import set_state

pygame.mixer.init()


def speak(text):

    if not text:
        return

    try:

        print("MITA:", text)

        set_state("talking")

        # buat file audio sementara
        tts = gTTS(text=text, lang="id")

        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        temp_path = temp_file.name

        tts.save(temp_path)

        # play audio
        pygame.mixer.music.load(temp_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

        pygame.mixer.music.stop()

        os.remove(temp_path)

    except Exception as e:

        print("Voice error:", e)

    finally:

        set_state("idle")
