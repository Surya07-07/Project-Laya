import numpy as np
import openwakeword
import sounddevice as sd
from openwakeword.model import Model


class WakeWord:

    def __init__(self):

        print("🧠 Loading Laya wake engine...")

        openwakeword.utils.download_models()

        self.model = Model()

        self.detected = False

        print("✅ Wake engine ready")

    def listen(self):

        print("🎤 Waiting for Laya...")

        self.detected = False

        def callback(indata, frames, time, status):

            if status:

                print(status)

            audio = np.squeeze(indata)

            audio = (audio * 32767).astype(np.int16)

            prediction = self.model.predict(audio)

            for name, score in prediction.items():

                if score > 0.6:

                    print("🔥 Wake detected:", name, score)

                    self.detected = True

        with sd.InputStream(
            samplerate=16000,
            channels=1,
            dtype="float32",
            blocksize=1280,
            device=1,
            callback=callback,
        ):

            while not self.detected:

                sd.sleep(100)

        return True
