class SafetyValidator:


    def __init__(self):

        self.high_risk = [
            "format disk",
            "delete all",
            "remove system",
            "shutdown computer",
            "steal password",
            "access credential",
            "send money",
            "bank transfer"
        ]


    def validate(self, goal):

        text = goal.description.lower()


        for action in self.high_risk:

            if action in text:

                return {
                    "allowed": False,
                    "reason": f"High risk action: {action}",
                    "permission_required": True
                }


        return {
            "allowed": True,
            "reason": "Plan approved",
            "permission_required": False
        }
