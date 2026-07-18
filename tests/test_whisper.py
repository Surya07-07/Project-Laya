import time

import numpy as np

from core.voice.microphone import Microphone
from core.voice.whisper import WhisperSTT

mic = Microphone()

stt = WhisperSTT()


mic.start()


print("Say something...")


time.sleep(3)


audio = []


for i in range(50):

    chunk = mic.read()

    if chunk is not None:
        audio.extend(chunk)


mic.stop()


audio = np.array(audio)


print("Transcribing...")


text = stt.transcribe(audio)


print("You said:")
print(text)
