from core.memory.types import MemoryType


class MemoryRanker:

    def classify(self, text):

        text = text.lower()

        permanent = [
            "my name",
            "i am",
            "i'm",
            "my birthday",
            "favorite",
            "prefer",
            "my city",
            "my college"
        ]

        important = [
            "exam",
            "meeting",
            "assignment",
            "deadline",
            "tomorrow",
            "today"
        ]

        temporary = [
            "remember this",
            "note",
            "current task"
        ]

        for word in permanent:
            if word in text:
                return MemoryType.PERMANENT

        for word in important:
            if word in text:
                return MemoryType.IMPORTANT

        for word in temporary:
            if word in text:
                return MemoryType.TEMPORARY

        return MemoryType.IGNORE