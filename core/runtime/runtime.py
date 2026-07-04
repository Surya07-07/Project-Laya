from app.logger import Logger
from app.config import Config

from core.dna.dna import DNA
from core.guardian.guardian import Guardian
from core.heart.heart import Heart
from core.memory.memory import Memory
from core.gateway.gateway import Gateway

from core.brain.processor import CommandProcessor

from core.plugins.plugin_manager import PluginManager
from plugins.calculator.plugin import CalculatorPlugin

from core.router.router import TaskRouter


class LayaRuntime:

    def __init__(self):

        # Configuration
        self.config = Config()

        # Core Modules
        self.dna = DNA()
        self.guardian = Guardian()
        self.heart = Heart(self.guardian)
        self.memory = Memory()
        self.gateway = Gateway()

        # Brain
        self.brain = CommandProcessor(
            self.memory,
            self.heart
        )

        # Plugin Manager
        self.plugins = PluginManager()

        self.plugins.register(
            "calculator",
            CalculatorPlugin()
        )

        # Router
        self.router = TaskRouter(
            self.brain,
            self.plugins
        )

    def start(self):

        Logger.info("Starting Laya Runtime")

        print("=" * 60)
        print("                PROJECT IGRIS")
        print("                     LAYA")
        print("=" * 60)

        print()

        print("Assistant :", self.config.get("assistant", "name"))
        print("Version   :", self.config.get("assistant", "version"))
        print("AI Model  :", self.config.get("ai", "model"))

        print()

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

        print("\n✅ Runtime Ready\n")

    def chat(self):

        print("Type 'exit' to quit.\n")

        while True:

            user = input("You : ")

            Logger.info(f"USER : {user}")

            if user.lower() == "exit":

                Logger.info("Runtime Closed")

                print("Laya : Goodbye!")

                break

            response = self.router.route(user)

            Logger.info(f"LAYA : {response}")

            print("Laya :", response)