import numpy as np
import sounddevice as sd


class VoiceListener:

    def __init__(self):

        self.sample_rate = 16000
        self.duration = 5

    def listen(self):

        print("🎤 Listening...")

        audio = sd.rec(
            int(self.duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=1,
            dtype=np.int16,
        )

        sd.wait()

        print("✅ Recording finished.")

        return audio
