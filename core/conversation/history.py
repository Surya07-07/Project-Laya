class ConversationHistory:

    def __init__(self):

        self.messages = []
        self._emotion = "neutral"

    def add(self, role, message):

        self.messages.append(
            {
                "role": role,
                "message": message
            }
        )

    def last(self, count=10):

        return self.messages[-count:]

    def build_prompt(self):

        prompt = ""

        for item in self.messages:

            prompt += f"{item['role']}: {item['message']}\n"

        return prompt.strip()

    def clear(self):

        self.messages.clear()

    def set_emotion(self, emotion):

        self._emotion = emotion

    def last_emotion(self):

        return self._emotion