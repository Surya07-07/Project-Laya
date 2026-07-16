from core.ai.ollama_client import OllamaClient


class AIService:

    def __init__(self):
        self.client = OllamaClient()

    def ask(self, prompt):
        return self.client.ask(prompt)