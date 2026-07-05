from core.memory.database import Database


class MemoryService:

    def __init__(self):
        self.db = Database()

    def remember(self, key, value):
        self.db.save(key, value)
        return f"I'll remember your {key}."

    def recall(self, key):
        value = self.db.get(key)

        if value is None:
            return f"I don't know your {key}."

        return value
