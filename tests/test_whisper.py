from core.voice.microphone import Microphone
from core.speech.whisper_engine import WhisperEngine
from core.language.manager import LanguageManager

mic = Microphone()

engine = WhisperEngine()

lang = LanguageManager()

mic.start()

print()
print("========================================")
print("Speak in ANY language")
print("English")
print("తెలుగు")
print("हिन्दी")
print("தமிழ்")
print("ಕನ್ನಡ")
print("========================================")
print()

mic.record(5)

result = engine.transcribe("data/input.wav")

lang.update(result["language"])

print()

print("Detected Code :", lang.code())
print("Detected Name :", lang.name())

print()

print("Recognized Text")

print("----------------------------------------")

print(result["text"])

mic.stop()
