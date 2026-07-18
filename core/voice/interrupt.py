import threading
import time


class InterruptController:

    def __init__(self, assistant):

        self.assistant = assistant
        self.running = False

    def start(self):

        self.running = True

        thread = threading.Thread(target=self.monitor, daemon=True)

        thread.start()

        print("🛑 Interrupt listener active")

    def monitor(self):

        while self.running:

            if self.assistant.tts.playing:

                print("👂 Listening for interruption...")

                text = self.assistant.listen_once()

                if text:

                    print("Interrupt heard:", text)

                    text = text.lower()

                    if "stop" in text or "cancel" in text or "quiet" in text:

                        print("🛑 Interrupt detected")

                        self.assistant.tts.stop()

            time.sleep(0.2)

    def stop(self):

        self.running = False
