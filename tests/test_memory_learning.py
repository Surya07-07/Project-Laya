from core.memory.memory import Memory


class CommandProcessor:

    def __init__(self, memory, heart, ai_core):

        self.memory = memory
        self.heart = heart
        self.ai = ai_core

    def execute(self, command):

        lower = command.lower().strip()

        # -------- Learn automatically --------

        self.memory.learn(command)

        # -------- Memory Questions --------

        if lower == "what is my name":
            value = self.memory.recall("name")

            if value:
                return f"Your name is {value}."

        if lower == "what is my college":
            value = self.memory.recall("college")

            if value:
                return f"You study at {value}."

        if lower == "what is my city":
            value = self.memory.recall("city")

            if value:
                return f"You live in {value}."

        # -------- AI --------

        return self.ai.ask(command)