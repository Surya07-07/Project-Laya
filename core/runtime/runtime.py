from app.config import Config
from app.logger import Logger
from core.brain.processor import CommandProcessor
from core.dna.dna import DNA
from core.gateway.gateway import Gateway
from core.guardian.guardian import Guardian
from core.heart.heart import Heart
from core.memory.memory import Memory
from core.plugins.plugin_manager import PluginManager
from core.router.router import TaskRouter
from plugins.calculator.plugin import CalculatorPlugin
from core.aicore.core import AICore
from core.skills.manager import SkillManager
from skills.calculator.skill import CalculatorSkill
from core.conversation.history import ConversationHistory

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

        # Plugin Manager
        self.plugins = PluginManager()
        self.plugins.register(
            "calculator",
            CalculatorPlugin()
        )

        # Skill Manager
        self.skill_manager = SkillManager()
        self.skill_manager.register(
            CalculatorSkill()
        )

        # Router
        self.router = TaskRouter(
            None,
            self.plugins
        )

        # AI Core
        self.ai_core = AICore(
            router=self.router,
            memory=self.memory,
            gateway=self.gateway,
            heart=self.heart,
            guardian=self.guardian,
            skill_manager=self.skill_manager
        )

        # Brain
        self.brain = CommandProcessor(
            self.memory,
            self.heart,
            self.ai_core
        )

        # Connect router to brain
        self.router.brain = self.brain

        # Conversation History
        self.history = ConversationHistory()

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

            self.history.add("User", user)

            response = self.ai_core.process(user)

            self.history.add("Laya", response)

            Logger.info(f"LAYA : {response}")

            print("Laya :", response)
