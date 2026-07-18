import sounddevice as sd
import soundfile as sf


class AudioRecorder:

    def __init__(self):
        self.sample_rate = 16000
        self.channels = 1

    def record(self, seconds=5):

        print("🎤 Listening...")

        audio = sd.rec(
            int(seconds * self.sample_rate),
            samplerate=self.sample_rate,
            channels=self.channels,
        )

        sd.wait()

        filename = "temp.wav"

        sf.write(filename, audio, self.sample_rate)

        print("✅ Saved:", filename)

        return filename
