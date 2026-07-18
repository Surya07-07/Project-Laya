from datetime import datetime


class MemoryAudit:

    def __init__(self):

        self.file = "logs/memory_audit.log"

    def write(self, action, key):

        with open(self.file, "a", encoding="utf-8") as f:

            f.write(f"{datetime.now()} | " f"{action} | " f"{key}\n")
