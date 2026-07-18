import time

from core.voice.listener import Listener
from core.voice.microphone import Microphone
from core.voice.speaker import Speaker
from core.voice.state import VoiceState
from core.voice.wake_word import WakeWordDetector


class VoiceManager:

    SESSION_TIMEOUT = 15

    def __init__(self):

        self.state = VoiceState.SLEEPING

        self.listener = Listener()

        self.microphone = Microphone()

        self.speaker = Speaker()

        self.wake = WakeWordDetector()

        self.session_active = False

        self.last_activity = 0

    def start(self):

        print("🎤 Starting Voice Manager...")

        try:
            self.microphone.start()
        except Exception:
            pass

        try:
            self.listener.start()
        except Exception:
            pass

        self.state = VoiceState.SLEEPING
        self.session_active = False

        print("✅ Voice Manager Ready")

    def stop(self):

        print("🛑 Stopping Voice Manager...")

        try:
            self.listener.stop()
        except Exception:
            pass

        try:
            self.microphone.stop()
        except Exception:
            pass

        self.session_active = False
        self.state = VoiceState.STOPPED

        print("✅ Voice Manager Stopped")

    def wait_for_wake_word(self):

        print("🎤 Waiting for wake word...")

        while True:

            if self.wake.detected():

                self.activate()

                return True

    def activate(self):

        self.state = VoiceState.LISTENING

        self.session_active = True

        self.last_activity = time.time()

        print("👂 Listening...")

    def keep_alive(self):

        self.last_activity = time.time()

    def session_alive(self):

        if not self.session_active:

            return False

        return (time.time() - self.last_activity) < self.SESSION_TIMEOUT

    def sleep(self):

        self.session_active = False

        self.state = VoiceState.SLEEPING

        print("😴 Session Ended")

    def listening(self):

        self.state = VoiceState.LISTENING

        self.keep_alive()

        print("👂 Listening...")

    def thinking(self):

        self.state = VoiceState.THINKING

        self.keep_alive()

        print("🧠 Thinking...")

    def speaking(self, text):

        self.state = VoiceState.SPEAKING

        self.keep_alive()

        print("🔊 Speaking...")

        try:

            self.speaker.speak(text)

        except Exception as e:

            print("Speaker Error:", e)

        if self.session_alive():

            self.listening()

        else:

            self.sleep()

    def run(self):

        self.start()

        while True:

            if not self.session_active:

                self.wait_for_wake_word()

            else:

                if not self.session_alive():

                    self.sleep()

                time.sleep(0.2)
