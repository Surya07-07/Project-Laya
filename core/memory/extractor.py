import re


class MemoryExtractor:

    def extract(self, text):

        text = text.strip()

        patterns = [

            (r"my name is (.+)", "name"),

            (r"i am (.+)", "identity"),

            (r"i'm (.+)", "identity"),

            (r"my birthday is (.+)", "birthday"),

            (r"my college is (.+)", "college"),

            (r"my city is (.+)", "city"),

            (r"my favorite (.+) is (.+)", "favorite")

        ]

        lower = text.lower()

        for pattern, key in patterns:

            match = re.search(pattern, lower)

            if match:

                if key == "favorite":

                    return (
                        f"favorite_{match.group(1).strip()}",
                        match.group(2).strip()
                    )

                return (
                    key,
                    match.group(1).strip()
                )

        return None