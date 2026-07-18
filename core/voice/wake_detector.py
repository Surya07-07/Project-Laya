class WakeDetector:

    def __init__(self):

        self.keyword = "hey laya"

    def detect(self, text):

        if not text:
            return False

        text = text.lower().strip()

        # remove common recognition mistakes
        replacements = {
            "hey leia": "hey laya",
            "hey layer": "hey laya",
            "hey laia": "hey laya",
            "hey leiaa": "hey laya",
        }

        for wrong, correct in replacements.items():
            text = text.replace(wrong, correct)

        if self.keyword in text:
            return True

        return False
