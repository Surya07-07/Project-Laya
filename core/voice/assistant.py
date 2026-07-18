import time

import numpy as np

from core.ai.ollama_client import OllamaClient
from core.voice.interrupt import InterruptController
from core.voice.microphone import Microphone
from core.voice.tts import PiperTTS
from core.voice.vad import VoiceActivityDetector
from core.voice.wake_detector import WakeDetector
from core.voice.whisper import WhisperSTT


class VoiceAssistant:

    def __init__(self):

        print("🎙️ Initializing Laya Voice System")

        self.mic = Microphone()
        self.stt = WhisperSTT()
        self.vad = VoiceActivityDetector()
        self.wake = WakeDetector()
        self.tts = PiperTTS()
        self.is_speaking = False
        self.ollama = OllamaClient()
        self.interrupt = InterruptController(self)

        print("✅ Voice System Ready")

    def listen_once(self):

        if self.is_speaking:
            return ""

        audio_data = []

        print("🎤 Listening...")

        start = time.time()

        while time.time() - start < 5:

            chunk = self.mic.read()

            if chunk is not None:
                audio_data.extend(chunk)

        if len(audio_data) == 0:
            return ""

        audio = np.array(audio_data, dtype=np.float32)

        if not self.vad.has_voice(audio):
            return ""

        print("🧠 Processing speech...")

        text = self.stt.transcribe(audio)

        print("Heard:", text)

        return text

    def speak(self, text):

        self.is_speaking = True

        self.mic.pause()

        self.tts.speak(text)

        time.sleep(1)

        self.mic.resume()

        self.is_speaking = False

    def handle_command(self, text):

        print("🧠 Command:", text)

        response = self.ollama.ask(text)

        self.mic.pause()

        self.speak(response)

        self.mic.resume()

    def start(self):

        self.mic.start()

        self.interrupt.start()

        print()
        print("==============================")
        print("     LAYA VOICE MODE ACTIVE")
        print("==============================")
        print("Say: Hey Laya")
        print()

        while True:

            text = self.listen_once()

            if self.wake.detect(text):

                print("✨ Laya Activated")

            self.mic.pause()

            self.speak("Yes, I am listening")

            self.mic.resume()

            while True:

                command = self.listen_once()

                if (
                    "stop" in command.lower()
                    or "shut up" in command.lower()
                    or "quiet" in command.lower()
                ):

                    self.speak("Okay, going back to sleep")

                    break

                self.handle_command(command)

            time.sleep(0.2)
