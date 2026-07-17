class PermissionManager:


    def __init__(self):

        self.sensitive_actions = [

            "delete",

            "remove",

            "shutdown",

            "install",

            "password",

            "payment",

            "bank"

        ]



    def requires_permission(self, text):

        text = text.lower()


        for action in self.sensitive_actions:

            if action in text:

                return True


        return False



    def ask_permission(self, action):


        print("\n⚠️ Permission Required")

        print(
            "Action:",
            action
        )


        answer = input(
            "Allow? (yes/no): "
        )


        return answer.lower() == "yes"
