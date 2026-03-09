import speech_recognition as sr

# ================= INIT RECOGNIZER =================

recognizer = sr.Recognizer()

# agar mic tidak terlalu sensitif (mengurangi noise angin)
recognizer.energy_threshold = 400
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8


# ================= GET MICROPHONE =================

def get_microphone():

    try:
        mic = sr.Microphone()
        return mic

    except Exception as e:
        print("Microphone Error:", e)
        return None


# ================= LISTEN FUNCTION =================

def listen(mic):

    if mic is None:
        return ""

    with mic as source:

        try:

            print("MITA listening...")

            # kalibrasi suara sekitar
            recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=6
            )

            text = recognizer.recognize_google(audio, language="id-ID")

            print("User:", text)

            return text.lower()

        except sr.UnknownValueError:
            return ""

        except sr.WaitTimeoutError:
            return ""

        except Exception as e:
            print("Listen Error:", e)
            return ""
