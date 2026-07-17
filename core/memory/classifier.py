class MemoryClassifier:
    """
    Decides importance and category of memories.
    """

    def __init__(self):
        self.permanent_keywords = [
            "my name",
            "i am",
            "remember my",
            "my birthday",
            "my preference"
        ]

        self.important_keywords = [
            "i like",
            "i prefer",
            "my project",
            "my work",
            "my study"
        ]


    def classify(self, text):

        text_lower = text.lower()

        # Permanent memory
        for keyword in self.permanent_keywords:
            if keyword in text_lower:
                return {
                    "category": "permanent",
                    "score": 95
                }


        # Important memory
        for keyword in self.important_keywords:
            if keyword in text_lower:
                return {
                    "category": "important",
                    "score": 60
                }


        # Temporary memory
        return {
            "category": "temporary",
            "score": 20
        }