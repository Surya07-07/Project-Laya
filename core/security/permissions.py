import json
from datetime import datetime

class PermissionManager:
    def __init__(self, log_file="logs/permissions.log"):
        self.log_file = log_file

    def request_permission(self, action, target):
        print(f"\n[PERMISSION REQUEST]")
        print(f"Action : {action}")
        print(f"Target : {target}")
        choice = input("Allow? (y/n): ").strip().lower()

        self.log(action, target, choice)
        return choice == "y"

    def log(self, action, target, decision):
        entry = {
            "time": str(datetime.now()),
            "action": action,
            "target": target,
            "decision": decision
        }

        with open(self.log_file, "a") as f:
            f.write(json.dumps(entry) + "\n")
