from core.ai.ollama_client import OllamaClient


class CommandProcessor:

    def __init__(self, memory, heart):
        self.memory = memory
        self.heart = heart
        self.ai = OllamaClient()

    def execute(self, command):

        command = command.strip()

        if command.lower() == "exit":
            return None

        if command.lower() == "what is my name":
            name = self.memory.recall("name")

            if name:
                return f"Your name is {name}."

        if command.lower().startswith("remember my name is"):

            name = command[20:].strip()

            self.memory.remember("name", name)

            return f"I'll remember your name, {name}."

        return self.ai.ask(command)