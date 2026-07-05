from core.voice.listener import VoiceListener
from core.voice.recognizer import VoiceRecognizer


listener = VoiceListener()

recognizer = VoiceRecognizer()

audio = listener.listen()

text = recognizer.recognize(audio)

print()

print("You said:")

print(text)