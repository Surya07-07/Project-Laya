from core.ai.service import AIService
from core.ai.prompt_builder import PromptBuilder
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
        self.prompt_builder = PromptBuilder()

    def process(self, command):

        intent = self.intent.detect(command)

        # ---------- Skills ----------

        if intent == "skill":

            result = self.skills.execute(command)

            if result is not None:
                return result

        # ---------- Router ----------

        result = self.router.route(command)

        if result is not None:
            return result

        # ---------- AI ----------

        prompt = self.prompt_builder.build(
            self.gateway.history,
            command
        )

        return self.ai.ask(prompt)