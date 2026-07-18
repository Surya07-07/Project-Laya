import json
import os
from datetime import datetime


class LearningMemory:

    def __init__(self):

        self.file = "data/agent_memory.json"

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(self.file):

            with open(self.file, "w") as f:
                json.dump([], f)

    def save_success(self, task, action, result):

        with open(self.file, "r") as f:
            memory = json.load(f)

        entry = {
            "task": task,
            "action": action,
            "result": result,
            "time": str(datetime.now()),
        }

        memory.append(entry)

        with open(self.file, "w") as f:

            json.dump(memory, f, indent=4)

        return entry

    def get_memory(self):

        with open(self.file, "r") as f:

            return json.load(f)
