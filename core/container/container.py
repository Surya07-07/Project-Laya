from app.config import Config
from core.ai.service import AIService
from core.dna.dna import DNA
from core.emotion.engine import EmotionEngine
from core.gateway.gateway import Gateway
from core.guardian.guardian import Guardian
from core.heart.heart import Heart
from core.memory.memory import Memory
from core.plugins.plugin_manager import PluginManager
from core.skills.manager import SkillManager
from plugins.calculator.plugin import CalculatorPlugin


class ServiceContainer:

    def __init__(self):

        self.config = Config()

        self.dna = DNA()

        self.guardian = Guardian()

        self.heart = Heart(self.guardian)

        self.memory = Memory()

        self.gateway = Gateway()

        self.skills = SkillManager()

        self.ai = AIService()

        self.plugins = PluginManager()

        self.emotion = EmotionEngine()

        self.plugins.register("calculator", CalculatorPlugin())
