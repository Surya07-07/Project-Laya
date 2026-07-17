import sounddevice as sd
import soundfile as sf


class Microphone:

    def __init__(self):

        self.sample_rate = 16000

        self.channels = 1

    def record(self, seconds=3):

        print(f"🎤 Recording {seconds} seconds...")

        audio = sd.rec(
            int(seconds * self.sample_rate),
            samplerate=self.sample_rate,
            channels=self.channels
        )

        sd.wait()

        sf.write(
            "data/input.wav",
            audio,
            self.sample_rate
        )

        print("💾 Saved to data/input.wav")

        return audio

    def start(self):

        print("🎤 Ready")

    def stop(self):

        print("🎤 Stopped")
