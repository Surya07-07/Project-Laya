from core.ai.ollama_client import OllamaClient


class AIService:

    def __init__(self):
        self.client = OllamaClient()

    def ask(self, prompt):

        print("🔹 AIService: sending prompt...")

        response = self.client.ask(prompt)

        print("🔹 AIService: received response")

        return response
