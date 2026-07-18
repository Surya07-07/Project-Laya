from core.voice.service import VoiceService

voice = VoiceService()

print()
print("Speak now...")
print()

text = voice.listen()

print()
print("Recognized:")
print(text)
