import re


class MemoryExtractor:

    def extract(self, sentence):

        text = sentence.strip()

        patterns = [

            (r"my name is (.+)", "name"),
            (r"i am (.+)", "name"),
            (r"my favorite (.+) is (.+)", None),
            (r"my birthday is (.+)", "birthday"),
            (r"my city is (.+)", "city"),
            (r"my college is (.+)", "college"),
            (r"i prefer (.+)", "preference"),

        ]

        for pattern, key in patterns:

            match = re.search(pattern, text, re.IGNORECASE)

            if match:

                if key is None:
                    return (
                        "favorite_" + match.group(1).strip(),
                        match.group(2).strip()
                    )

                return (
                    key,
                    match.group(1).strip()
                )

        return None