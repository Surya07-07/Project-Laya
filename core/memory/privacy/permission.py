class MemoryPermission:

    def __init__(self):

        self.pending = None

    def check(self, text):

        sensitive = [
            "password",
            "bank",
            "account number",
            "aadhaar",
            "pan",
            "otp",
            "pin",
            "card",
            "private key",
        ]

        text = text.lower()

        for word in sensitive:

            if word in text:

                self.pending = text

                return {
                    "status": "permission_required",
                    "reason": f"Sensitive data detected: {word}",
                }

        return {"status": "approved"}

    def approve(self):

        data = self.pending

        self.pending = None

        return data

    def reject(self):

        self.pending = None

        return True
