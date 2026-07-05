import json

from core.ai.ollama_client import OllamaClient


class AIIntentClassifier:

    def __init__(self):
        self.ai = OllamaClient()

    def classify(self, command):

        prompt = f"""
You are an intent classifier.

Return ONLY valid JSON.

Supported intents:

open_app
calculator
remember_name
recall_name
chat

User:

{command}

Examples:

User: Open Notepad

{{"intent":"open_app","target":"notepad"}}

User: calc 5+6

{{"intent":"calculator","expression":"5+6"}}

User: remember my name is Surya

{{"intent":"remember_name","name":"Surya"}}

User: what is my name

{{"intent":"recall_name"}}

User: Explain AI

{{"intent":"chat","message":"Explain AI"}}
"""

        response = self.ai.ask(prompt)

        try:
            return json.loads(response)

        except Exception:

            return {"intent": "chat", "message": command}
