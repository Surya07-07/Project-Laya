from core.voice.microphone import Microphone

mic = Microphone()

mic.start()

audio = mic.record(3)

print()

print("Shape :", audio.shape)

print("Samples :", len(audio))

mic.stop()
