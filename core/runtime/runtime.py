from app.logger import Logger

from core.dna.dna import DNA
from core.guardian.guardian import Guardian
from core.heart.heart import Heart
from core.memory.memory import Memory
from core.gateway.gateway import Gateway
from core.brain.processor import CommandProcessor


class LayaRuntime:

    def __init__(self):

        self.dna = DNA()
        self.guardian = Guardian()
        self.heart = Heart(self.guardian)
        self.memory = Memory()
        self.gateway = Gateway()

        self.brain = CommandProcessor(
            self.memory,
            self.heart
        )

    def start(self):

        Logger.info("Starting Runtime")

        print("\nStarting Laya...\n")

        self.dna.load()
        Logger.info("DNA Loaded")

        self.guardian.load()
        Logger.info("Guardian Loaded")

        self.heart.load()
        Logger.info("Heart Loaded")

        self.memory.load()
        Logger.info("Memory Loaded")

        self.gateway.load()
        Logger.info("Gateway Loaded")

        print("\nLaya Runtime Ready.\n")

    def chat(self):

        while True:

            user = input("You : ")

            Logger.info(f"USER : {user}")

            if user.lower() == "exit":

                Logger.info("Runtime Closed")

                print("Laya : Goodbye.")

                break

            response = self.brain.execute(user)

            Logger.info(f"LAYA : {response}")

            print("Laya :", response)