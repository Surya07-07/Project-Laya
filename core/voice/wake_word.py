class WakeWord:

    def __init__(self):

        self.keyword = "hey laya"

    def detect(self, text):

        return self.keyword in text.lower()
