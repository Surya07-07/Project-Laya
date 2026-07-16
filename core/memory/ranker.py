from core.memory.types import MemoryType


class MemoryRanker:

    def classify(self, text):

        text = text.lower().strip()

        permanent = [
            "name",
            "my name",
            "city",
            "my city",
            "birthday",
            "my birthday",
            "favorite",
            "prefer",
            "language",
            "college",
            "university",
            "home",
            "hometown"
        ]

        important = [
            "exam",
            "meeting",
            "assignment",
            "deadline",
            "today",
            "tomorrow"
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

        # Store unknown memories as permanent during development
        return MemoryType.PERMANENT