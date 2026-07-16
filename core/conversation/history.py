class ConversationHistory:

    def __init__(self):
        self.messages = []

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