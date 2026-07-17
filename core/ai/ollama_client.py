import ollama
from app.config import Config


class OllamaClient:

    def __init__(self):
        config = Config()

        self.model = config.get("ai", "model")

        self.client = ollama.Client(
            host="http://127.0.0.1:11434"
        )


    def ask(self, prompt):

        print("🔹 Connecting to Ollama...")
        print("Model:", self.model)

        try:
            response = self.client.chat(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            print("🔹 Ollama replied")

            return response["message"]["content"].strip()


        except Exception as e:

            print("❌ Ollama Error:", e)

            return (
                "I am unable to connect to my local AI brain. "
                "Please start Ollama."
            )