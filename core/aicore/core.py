from core.ai.service import AIService
from core.intent.router import IntentRouter


class AICore:

    def __init__(
        self,
        router,
        memory,
        gateway,
        heart,
        guardian,
        skill_manager
    ):

        self.router = router
        self.memory = memory
        self.gateway = gateway
        self.heart = heart
        self.guardian = guardian
        self.skills = skill_manager

        self.intent = IntentRouter()
        self.ai = AIService()

    def process(self, command):

        intent = self.intent.detect(command)

        if intent == "skill":
            response = self.skills.execute(command)

            if response is not None:
                return response

        response = self.router.route(command)

        if response is not None:
            return response

        return self.ai.ask(command)