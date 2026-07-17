from faster_whisper import WhisperModel
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import tempfile
import os



class SpeechRecognizer:


    def __init__(self):

        self.model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8"
        )



    def record(self, seconds=5):

        print(
            "\n🎤 Listening..."
        )


        sample_rate = 16000


        audio = sd.rec(

            int(seconds * sample_rate),

            samplerate=sample_rate,

            channels=1,

            dtype="float32"

        )


        sd.wait()


        return audio, sample_rate



    def transcribe(self):


        audio, rate = self.record()


        path = tempfile.mktemp(
            suffix=".wav"
        )


        write(
            path,
            rate,
            audio
        )


        segments, info = self.model.transcribe(
            path
        )


        text = ""


        for segment in segments:

            text += segment.text



        os.remove(path)


        return text.strip()
