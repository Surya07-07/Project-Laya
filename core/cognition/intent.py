class IntentDetector:

    def __init__(self):

        self.intents = {
            "create_folder": ["create folder", "make folder", "new folder"],
            "open_application": ["open", "launch", "start"],
            "type_text": ["type", "write"],
            "press_key": ["press", "hit key"],
            "memory_save": ["remember", "save this"],
        }

    def detect(self, text):

        text = text.lower().strip()

        for intent, words in self.intents.items():

            for word in words:

                if word in text:

                    return {"intent": intent, "confidence": 0.9}

        return {"intent": "unknown", "confidence": 0}
