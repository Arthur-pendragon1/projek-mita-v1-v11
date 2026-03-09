import threading
import time
from mita_listen import listen, get_microphone
from mita_brain import process
from mita_ui import ui_loop

mic = get_microphone()


def brain_loop():

    while True:

        text = listen(mic)

        if text:
            process(text)

        time.sleep(0.1)


brain_thread = threading.Thread(target=brain_loop)
brain_thread.daemon = True
brain_thread.start()

ui_loop()
