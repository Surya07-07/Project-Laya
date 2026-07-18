import requests


class OllamaClient:

    def __init__(self):

        self.url = "http://127.0.0.1:11434/api/generate"
        self.model = "llama3.2:3b"

    def ask(self, prompt):

        data = {"model": self.model, "prompt": prompt, "stream": False}

        response = requests.post(self.url, json=data)

        result = response.json()

        return result.get("response", "I could not answer")
