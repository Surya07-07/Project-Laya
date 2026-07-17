from app.config import Config
from core.memory.memory import Memory
from core.gateway.gateway import Gateway
from core.skills.manager import SkillManager
from core.ai.service import AIService


class ServiceContainer:

    def __init__(self):

        self.config = Config()

        self.memory = Memory()

        self.gateway = Gateway()

        self.skills = SkillManager()

        self.ai = AIService()