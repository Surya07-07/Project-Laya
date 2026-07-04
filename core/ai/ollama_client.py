import ollama

from app.config import Config


class OllamaClient:

    def __init__(self):

        config = Config()

        self.model = config.get(
            "ai",
            "model"
        )

    def ask(self, prompt):

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]