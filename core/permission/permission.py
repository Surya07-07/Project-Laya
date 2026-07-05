class PermissionManager:

    def ask(self, action):

        while True:

            answer = input(f"\nLaya wants to {action}.\nAllow? (y/n): ")

            answer = answer.lower().strip()

            if answer == "y":
                return True

            if answer == "n":
                return False
