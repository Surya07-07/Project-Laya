from core.memory.service import MemoryService


class CommandProcessor:

    def __init__(self, memory, heart, ai_core):

        self.memory = memory
        self.heart = heart
        self.ai = ai_core

    def execute(self, command):

        lower = command.lower().strip()

        # ---------- Memory ----------

        if lower.startswith("remember my"):

            text = command[12:]

            if " is " in text:

                key, value = text.split(" is ", 1)

                return self.memory.remember(
                    key.strip(),
                    value.strip()
                )

        if lower.startswith("what is my"):

            key = command[11:].strip().rstrip("?")

            return self.memory.recall(key)

        # ---------- AI ----------

        return self.ai.process(command)