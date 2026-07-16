from core.personality.personality import Personality


class PromptBuilder:

    def __init__(self):
        self.personality = Personality()

    def build(self, history, user):

        conversation = history.build_prompt()

        return f"""
{self.personality.prompt()}

Conversation:

{conversation}

User: {user}

Laya:
""".strip()