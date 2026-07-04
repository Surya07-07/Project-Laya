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

        print("\nStarting Laya...\n")

        self.dna.load()
        self.guardian.load()
        self.heart.load()
        self.memory.load()
        self.gateway.load()

        print("\nLaya Runtime Ready.\n")

    def chat(self):

        while True:

            user = input("You : ")

            if user.lower() == "exit":
                print("Laya : Goodbye.")
                break

            response = self.brain.execute(user)

            print("Laya :", response)