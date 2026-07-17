from app.config import Config
from app.logger import Logger

from core.container.container import ServiceContainer

from core.dna.dna import DNA
from core.guardian.guardian import Guardian
from core.heart.heart import Heart
from core.memory.memory import Memory
from core.gateway.gateway import Gateway

from core.plugins.plugin_manager import PluginManager
from plugins.calculator.plugin import CalculatorPlugin

from core.skills.manager import SkillManager
from skills.calculator.skill import CalculatorSkill

from core.router.router import TaskRouter
from core.brain.processor import CommandProcessor
from core.aicore.core import AICore

from core.conversation.history import ConversationHistory
from core.system.startup import StartupManager
from core.voice.wakeword import WakeWord


class LayaRuntime:

    def __init__(self):

        # ------------------------------
        # Dependency Container
        # ------------------------------

        try:

            self.container = ServiceContainer()

            self.config = self.container.config
            self.dna = self.container.dna
            self.guardian = self.container.guardian
            self.heart = self.container.heart
            self.memory = self.container.memory
            self.gateway = self.container.gateway
            self.emotion = self.container.emotion

        except Exception:

            self.config = Config()
            self.dna = DNA()
            self.guardian = Guardian()
            self.heart = Heart(self.guardian)
            self.memory = Memory()
            self.gateway = Gateway()


        # ------------------------------
        # Plugins
        # ------------------------------

        self.plugins = PluginManager()

        self.plugins.register(
            "calculator",
            CalculatorPlugin()
        )


        # ------------------------------
        # Skills
        # ------------------------------

        self.skill_manager = SkillManager()

        self.skill_manager.register(
            CalculatorSkill()
        )


        # ------------------------------
        # Router
        # ------------------------------

        self.router = TaskRouter(
            None,
            self.plugins
        )


        # ------------------------------
        # AI Core
        # ------------------------------

        self.ai_core = AICore(
            router=self.router,
            memory=self.memory,
            gateway=self.gateway,
            heart=self.heart,
            guardian=self.guardian,
            skill_manager=self.skill_manager
        )


        # ------------------------------
        # Brain
        # ------------------------------

        self.brain = CommandProcessor(
            self.memory,
            self.heart,
            self.ai_core
        )

        self.router.brain = self.brain


        # ------------------------------
        # Conversation
        # ------------------------------

        self.history = ConversationHistory()


        # ------------------------------
        # Voice System
        # ------------------------------

        self.startup = StartupManager()

        self.voice = WakeWord()



    def start(self):

        Logger.info("Starting Runtime")


        print("=" * 60)
        print("                PROJECT IGRIS")
        print("                     LAYA")
        print("=" * 60)

        print()


        print(
            "Assistant :",
            self.config.get("assistant", "name")
        )

        print(
            "Version   :",
            self.config.get("assistant", "version")
        )

        print(
            "AI Model  :",
            self.config.get("ai", "model")
        )


        # Start Ollama automatically

        self.startup.initialize()



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


        print()

        print("🧬 DNA Loaded")
        print("🛡 Guardian Loaded")
        print("❤️ Heart Loaded")
        print("📦 Memory Loaded")
        print("🌐 Gateway Loaded")

        print()

        print("✅ Runtime Ready")

        print()

        print("🎤 Wake word listener ready")
        print("Say 'Hey Laya' to activate")



    def chat(self):

        print(
            "Waiting for Hey Laya...\n"
        )


        while True:

            try:

                # Listen for wake word

                activated = self.voice.listen()


                if not activated:

                    continue


                print(
                    "🎤 Laya Activated"
                )


                user = input(
                    "You : "
                ).strip()



                if not user:

                    continue



                if user.lower() == "exit":

                    Logger.info(
                        "Runtime Closed"
                    )

                    print(
                        "Laya : Goodbye!"
                    )

                    break



                Logger.info(
                    f"USER : {user}"
                )


                self.history.add(
                    "User",
                    user
                )


                emotion = self.emotion.update(
                    user
                )


                self.gateway.history.set_emotion(
                    emotion.value
                )


                print(
                    f"😊 Emotion: {emotion.value}"
                )


                response = self.ai_core.process(
                    user
                )


                self.history.add(
                    "Laya",
                    response
                )


                Logger.info(
                    f"LAYA : {response}"
                )


                print(
                    "Laya :",
                    response
                )



            except Exception as e:


                Logger.error(
                    str(e)
                )


                print(
                    "Laya Error:",
                    e
                )