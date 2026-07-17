class Guardian:

    def __init__(self):

        self.protection = True

        self.allowed_actions = [
            "open_app",
            "read_file",
            "remember",
            "speak"
        ]


        self.sensitive_words = [

            "password",
            "passwd",
            "pin",
            "otp",
            "cvv",
            "credit card",
            "debit card",
            "bank account",
            "api key",
            "secret key",
            "private key",
            "token"
        ]



    def load(self):

        print("🛡️ Guardian Loaded")



    def authorize(self, action):

        print(
            f"🛡️ Checking permission for: {action}"
        )


        if action == "internet":

            return False


        if action in self.allowed_actions:

            return True


        return False



    def check_memory(self, text):

        text = text.lower()


        for word in self.sensitive_words:

            if word in text:

                return {
                    "allowed": False,
                    "reason": "Sensitive information detected"
                }


        return {
            "allowed": True,
            "reason": "Safe memory"
        }