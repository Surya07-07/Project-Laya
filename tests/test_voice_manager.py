from core.voice.manager import VoiceManager


voice = VoiceManager()

voice.start()

print("Current State:", voice.state.value)

voice.activate()

voice.think()

voice.speak("Hello, I am Laya.")

voice.stop()

print("Current State:", voice.state.value)
