class ConversationContext:

    def __init__(self):

        self.items = []

    def add(self, role, text):

        self.items.append({
            "role": role,
            "text": text
        })

    def last(self, count=10):

        return self.items[-count:]

    def build(self):

        prompt = ""

        for item in self.items:

            prompt += f'{item["role"]}: {item["text"]}\n'

        return prompt.strip()

    def clear(self):

        self.items.clear()
