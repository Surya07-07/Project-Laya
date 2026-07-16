class SemanticMemory:

    def __init__(self):

        self.aliases = {

            "city": [
                "city",
                "hometown",
                "home town",
                "live",
                "place",
                "location"
            ],

            "name": [
                "name",
                "who am i",
                "myself"
            ],

            "college": [
                "college",
                "university",
                "campus"
            ],

            "language": [
                "language",
                "coding language",
                "programming language"
            ]
        }

    def find_key(self, question):

        question = question.lower()

        for key, words in self.aliases.items():

            for word in words:

                if word in question:

                    return key

        return None