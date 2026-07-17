from core.memory.types import MemoryType


class MemoryRanker:

    def rank(self, text):

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
            "tomorrow",
            "project"
        ]


        temporary = [
            "remember this",
            "note",
            "current task"
        ]


        for word in permanent:

            if word in text:

                return {
                    "type": MemoryType.PERMANENT,
                    "score": 95
                }



        for word in important:

            if word in text:

                return {
                    "type": MemoryType.IMPORTANT,
                    "score": 60
                }



        for word in temporary:

            if word in text:

                return {
                    "type": MemoryType.TEMPORARY,
                    "score": 20
                }



        return {
            "type": MemoryType.TEMPORARY,
            "score": 10
        }