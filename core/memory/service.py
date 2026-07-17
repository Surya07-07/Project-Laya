from core.memory.database import Database
from core.memory.classifier import MemoryClassifier


class MemoryService:

    def __init__(self):

        self.db = Database()
        self.classifier = MemoryClassifier()


    def remember(self, key, value):

        text = f"{key} {value}"

        decision = self.classifier.classify(text)

        self.db.save(
            key,
            value,
            decision["category"],
            decision["score"]
        )

        return (
            f"I'll remember your {key}. "
            f"Memory type: {decision['category']} "
            f"Score: {decision['score']}"
        )


    def recall(self, key):

        value = self.db.get(key)

        if value is None:
            return f"I don't know your {key}."

        return value


    def memories(self):

        return self.db.get_all()


    def forget(self, key):

        self.db.delete(key)

        return f"I forgot your {key}."