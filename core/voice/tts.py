import os
import subprocess
import tempfile

import sounddevice as sd
import soundfile as sf


class PiperTTS:

    def __init__(self):

        self.playing = False

        print("🔊 Piper TTS Ready")

    def speak(self, text):

        print("Laya:", text)

        self.playing = True

        output = tempfile.mktemp(suffix=".wav")

        command = [
            "piper",
            "--model",
            "en_US-lessac-medium.onnx",
            "--output_file",
            output,
        ]

        process = subprocess.Popen(command, stdin=subprocess.PIPE, text=True)

        process.communicate(text)

        audio, rate = sf.read(output)

        sd.play(audio, rate)

        sd.wait()

        os.remove(output)

        self.playing = False

    def stop(self):

        if self.playing:

            sd.stop()

            self.playing = False

            print("🛑 Speech stopped")
