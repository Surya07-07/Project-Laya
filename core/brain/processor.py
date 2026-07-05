from core.ai.ollama_client import OllamaClient
from core.memory.service import MemoryService


class CommandProcessor:

    def __init__(self, memory, heart):

        self.memory = MemoryService()
        self.ai = OllamaClient()

    def execute(self, command):

        lower = command.lower()

        if lower.startswith("remember my"):

            text = command[12:]

            if " is " in text:

                key, value = text.split(" is ", 1)

                return self.memory.remember(key.strip(), value.strip())

        if lower.startswith("what is my"):

            key = command[11:].strip().rstrip("?")

            return self.memory.recall(key)

        return self.ai.ask(command)
