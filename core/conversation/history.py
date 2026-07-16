class ConversationHistory:

    def __init__(self):
        self.history = []

    def add(self, role, message):
        self.history.append(
            {
                "role": role,
                "message": message
            }
        )

    def last(self, count=10):
        return self.history[-count:]

    def clear(self):
        self.history.clear()

    def size(self):
        return len(self.history)