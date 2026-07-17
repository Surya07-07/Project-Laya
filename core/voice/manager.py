from core.voice.state import VoiceState
from core.voice.listener import Listener
from core.voice.microphone import Microphone
from core.voice.speaker import Speaker
from core.voice.wake_word import WakeWord


class VoiceManager:

    def __init__(self):

        self.state = VoiceState.SLEEPING

        self.listener = Listener()

        self.microphone = Microphone()

        self.speaker = Speaker()

        self.wake = WakeWord()

    def start(self):

        self.microphone.start()

        self.listener.start()

        self.state = VoiceState.SLEEPING

        print("🎤 Voice Manager Ready")

    def stop(self):

        self.listener.stop()

        self.microphone.stop()

        self.state = VoiceState.STOPPED

    def activate(self):

        self.state = VoiceState.LISTENING

        print("👂 Listening...")

    def think(self):

        self.state = VoiceState.THINKING

        print("🧠 Thinking...")

    def speak(self, text):

        self.state = VoiceState.SPEAKING

        self.speaker.speak(text)

        self.state = VoiceState.SLEEPING
