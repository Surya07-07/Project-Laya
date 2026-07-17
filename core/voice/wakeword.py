import openwakeword
from openwakeword.model import Model
import sounddevice as sd
import numpy as np


class WakeWord:

    def __init__(self):

        print("🧠 Loading wake word engine...")

        openwakeword.utils.download_models()

        self.model = Model()

        print("✅ Wake engine ready")


    def listen(self):

        print("🎤 Waiting for wake word...")


        def callback(indata, frames, time, status):

            if status:
                print(status)


            # Convert (frames,1) -> (frames,)
            audio = np.squeeze(indata)


            # Convert float32 -> int16
            audio = (
                audio * 32767
            ).astype(np.int16)


            prediction = self.model.predict(
                audio
            )


            for key, score in prediction.items():

                if score > 0.5:

                    print(
                        "Wake detected:",
                        key,
                        score
                    )

                    self.detected = True



        self.detected = False


        with sd.InputStream(
            samplerate=16000,
            channels=1,
            dtype="float32",
            blocksize=1280,
            callback=callback
        ):

            while not self.detected:

                sd.sleep(100)


        return True
