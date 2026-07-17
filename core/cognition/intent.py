class IntentDetector:


    def __init__(self):

        self.intents = {

            "create_folder": [
                "create folder",
                "make folder",
                "new folder"
            ],


            "open_application": [
                "open",
                "launch",
                "start"
            ],


            "search": [
                "search",
                "find",
                "look for"
            ],


            "memory_save": [
                "remember",
                "save this",
                "don't forget"
            ]

        }



    def detect(self, text):

        text = text.lower()


        for intent, keywords in self.intents.items():

            for keyword in keywords:

                if keyword in text:

                    return {

                        "intent": intent,

                        "confidence": 0.9

                    }


        return {

            "intent": "unknown",

            "confidence": 0.0

        }
