import time

from core.voice.microphone import Microphone

mic = Microphone()

mic.start()

print("Speak something...")


for i in range(50):

    audio = mic.read()

    if audio is not None:
        print("Audio captured:", len(audio))

    time.sleep(0.1)


mic.stop()
