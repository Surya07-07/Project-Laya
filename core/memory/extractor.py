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
            # Sensitive information detection
            (r"my password is (.+)", "password"),
            (r"my bank account number is (.+)", "bank_account"),
            (r"my account number is (.+)", "account_number"),
            (r"my aadhaar number is (.+)", "aadhaar"),
            (r"my pan number is (.+)", "pan"),
        ]

        for pattern, key in patterns:

            match = re.search(pattern, text, re.IGNORECASE)

            if match:

                if key is None:

                    return (
                        "favorite_" + match.group(1).strip(),
                        match.group(2).strip(),
                    )

                return (key, match.group(1).strip())

        return None
