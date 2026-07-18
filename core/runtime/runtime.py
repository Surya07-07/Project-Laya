from app.config import Config
from app.logger import Logger
from core.aicore.core import AICore
from core.brain.processor import CommandProcessor
from core.container.container import ServiceContainer
from core.conversation.history import ConversationHistory
from core.dna.dna import DNA
from core.gateway.gateway import Gateway
from core.guardian.guardian import Guardian
from core.heart.heart import Heart
from core.memory.memory import Memory
from core.plugins.plugin_manager import PluginManager
from core.router.router import TaskRouter
from core.skills.manager import SkillManager
from core.system.startup import StartupManager
from core.voice.microphone import Microphone
from core.voice.speech.whisper import SpeechRecognizer
from core.voice.voice_response import LayaVoice

# Voice imports
from core.voice.wakeword import WakeWord
from plugins.calculator.plugin import CalculatorPlugin
from skills.calculator.skill import CalculatorSkill


class LayaRuntime:

    def __init__(self):

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
            self.emotion = None

        self.plugins = PluginManager()

        self.plugins.register("calculator", CalculatorPlugin())

        self.skill_manager = SkillManager()

        self.skill_manager.register(CalculatorSkill())

        self.router = TaskRouter(None, self.plugins)

        self.ai_core = AICore(
            router=self.router,
            memory=self.memory,
            gateway=self.gateway,
            heart=self.heart,
            guardian=self.guardian,
            skill_manager=self.skill_manager,
        )

        self.brain = CommandProcessor(self.memory, self.heart, self.ai_core)

        self.router.brain = self.brain

        self.history = ConversationHistory()

        self.startup = StartupManager()

        # Voice system

        self.voice = WakeWord()

        self.microphone = Microphone()

        self.recognizer = SpeechRecognizer()

        self.speaker = LayaVoice()

    def start(self):

        Logger.info("Starting Runtime")

        print("=" * 60)
        print("                PROJECT IGRIS")
        print("                     LAYA")
        print("=" * 60)

        print()

        print("Assistant :", self.config.get("assistant", "name"))

        print("Version   :", self.config.get("assistant", "version"))

        print("AI Model  :", self.config.get("ai", "model"))

        self.startup.initialize()

        self.dna.load()

        self.guardian.load()

        self.heart.load()

        self.memory.load()

        self.gateway.load()

        print()

        print("🧬 DNA Loaded")
        print("🛡 Guardian Loaded")
        print("❤️ Heart Loaded")
        print("📦 Memory Loaded")
        print("🌐 Gateway Loaded")

        print()

        print("✅ Runtime Ready")

        print()

        print("🎤 Voice Assistant Ready")
        print("Say 'Hey Laya'")

    def chat(self):

        while True:

            try:

                activated = self.voice.listen()

                if not activated:

                    continue

                print("🔥 Laya Activated")

                # Record user command

                print("🎤 Listening...")

                self.microphone.record(seconds=5)

                user = self.recognizer.transcribe("data/input.wav")

                print("You:", user)

                if not user:

                    continue

                if user.lower() == "exit":

                    self.speaker.speak("Goodbye")

                    break

                response = self.ai_core.process(user)

                print("Laya:", response)

                self.speaker.speak(response)

            except Exception as e:

                print("Laya Error:", e)
