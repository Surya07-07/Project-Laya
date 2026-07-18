import queue
import threading

import numpy as np
import sounddevice as sd


class Microphone:

    def __init__(self):
        self.sample_rate = 16000
        self.channels = 1
        self.audio_queue = queue.Queue()
        self.running = False

    def callback(self, indata, frames, time, status):

        if status:
            print("Microphone status:", status)

        audio = np.copy(indata[:, 0])

        self.audio_queue.put(audio)

    def start(self):

        if self.running:
            return

        self.running = True

        self.stream = sd.InputStream(
            samplerate=self.sample_rate,
            channels=self.channels,
            dtype="float32",
            callback=self.callback,
        )

        self.stream.start()

        print("🎤 Microphone started")

    def read(self):

        if not self.audio_queue.empty():
            return self.audio_queue.get()

        return None

    def pause(self):

        if hasattr(self, "stream"):

            self.stream.stop()

        print("🎤 Microphone paused")

    def resume(self):

        if hasattr(self, "stream"):

            self.stream.start()

        print("🎤 Microphone resumed")

    def stop(self):

        self.running = False

        if hasattr(self, "stream"):
            self.stream.stop()
            self.stream.close()

        print("🎤 Microphone stopped")
