from core.ai.service import AIService


class Assistant:

    def __init__(
        self,
        memory,
        skills,
        gateway
    ):

        self.memory = memory
        self.skills = skills
        self.gateway = gateway

        self.ai = AIService()

    def process(self, text):

        # Learn automatically
        self.memory.learn(text)

        # Skills
        result = self.skills.execute(text)

        if result is not None:
            return result

        # AI
        return self.ai.ask(text)