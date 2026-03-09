from datetime import datetime
from mita_voice import speak
from mita_ui import set_state
import wikipedia

# bahasa wikipedia
wikipedia.set_lang("id")

# kata yang dianggap noise
ignored_words = [
    "hmm",
    "eh",
    "ah",
    "emm",
    "test",
    "tes",
    "halo halo"
]


def search_internet(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except:
        return None


def process(text):

    # jika kosong jangan respon
    if not text:
        return

    text = text.lower().strip()

    # abaikan kata noise
    for word in ignored_words:
        if text == word:
            return

    # ================= SALAM =================

    if "halo" in text or "hai" in text:

        set_state("talking")
        speak("Halo, ada yang bisa saya bantu")

    # ================= PERKENALAN =================

    elif "siapa kamu" in text:

        set_state("talking")
        speak(
            "Saya adalah Mita, asisten kecerdasan buatan yang berjalan di komputer anda."
        )

    elif "perkenalkan dirimu" in text:

        set_state("talking")
        speak(
            "Halo, saya Mita. Saya adalah AI assistant yang sedang terus dikembangkan."
        )

    # ================= PEMBUAT =================

    elif (
        "siapa yang membuatmu" in text
        or "siapa pembuatmu" in text
        or "siapa yang menciptakanmu" in text
        or "siapa developer kamu" in text
        or "siapa yang membuat kamu" in text
    ):

        set_state("talking")

        speak(
            "Saya dibuat oleh Rifqi. "
            "Rifqi adalah developer yang mengembangkan saya sebagai asisten kecerdasan buatan. "
            "Dia terus meningkatkan kemampuan saya agar saya bisa membantu manusia dengan lebih baik."
        )

    # ================= JAM =================

    elif "jam berapa" in text:

        now = datetime.now().strftime("%H:%M")

        set_state("talking")
        speak(f"Sekarang jam {now}")

    # ================= TERIMA KASIH =================

    elif "terima kasih" in text:

        set_state("talking")
        speak("Sama sama, senang bisa membantu")

    # ================= FITUR =================

    elif "fitur kamu apa" in text or "kamu bisa apa" in text:

        set_state("talking")

        speak(
            "Saya bisa mendengar suara anda, berbicara, menjawab pertanyaan, "
            "dan mencari informasi dari internet."
        )

    # ================= PENCARIAN INTERNET =================

    else:

        set_state("thinking")

        speak("Tunggu sebentar, saya akan mencari jawabannya di internet")

        result = search_internet(text)

        if result:

            set_state("talking")
            speak(result)

        else:

            set_state("confused")
            speak("Maaf, saya belum menemukan jawaban yang tepat.")
