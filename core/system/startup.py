import subprocess
import time
import requests


class StartupManager:

    def check_ollama(self):

        try:
            requests.get(
                "http://127.0.0.1:11434",
                timeout=2
            )
            return True

        except:
            return False


    def start_ollama(self):

        print("🧠 Starting local AI brain...")

        subprocess.Popen(
            ["ollama", "serve"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        time.sleep(5)


    def initialize(self):

        print("🚀 Initializing Laya system...")


        if self.check_ollama():
            print("✅ Ollama already running")

        else:
            self.start_ollama()

            if self.check_ollama():
                print("✅ Ollama started")

            else:
                print("❌ Unable to start Ollama")


        print("✅ Startup complete")
