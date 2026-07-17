import subprocess
import tempfile
import os
import time


class LayaVoice:


    def __init__(self):

        self.voice_model = (
            "models/piper/voices/en_US-lessac-medium.onnx"
        )


    def speak(self, text):

        print("\n🔊 Laya:", text)


        wav_file = tempfile.mktemp(
            suffix=".wav"
        )


        try:

            command = [
                "piper",
                "-m",
                self.voice_model,
                "-f",
                wav_file
            ]


            process = subprocess.Popen(
                command,
                stdin=subprocess.PIPE,
                text=True
            )


            process.communicate(text)


            if os.path.exists(wav_file):

                os.system(
                    f'start "" "{wav_file}"'
                )


                # allow speaker to finish
                time.sleep(3)


                return True


            print(
                "❌ Piper failed"
            )

            return False



        except Exception as e:

            print(
                "Piper error:",
                e
            )

            return False
