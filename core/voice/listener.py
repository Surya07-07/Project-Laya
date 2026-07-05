import sounddevice as sd
import soundfile as sf


class VoiceListener:

    def __init__(self):

        self.sample_rate = 16000
        self.duration = 5

    def listen(self):

        print("Listening...")

        audio = sd.rec(
            int(self.sample_rate * self.duration),
            samplerate=self.sample_rate,
            channels=1
        )

        sd.wait()

        sf.write(
            "temp.wav",
            audio,
            self.sample_rate
        )

        print("Saved temp.wav")

        return "temp.wav"