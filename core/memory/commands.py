from core.memory.cleanup import MemoryCleanup
from core.memory.service import MemoryService


class MemoryCommandProcessor:

    def __init__(self):

        self.memory = MemoryService()

        self.cleanup = MemoryCleanup()

        self.locked = False

    def process(self, command):

        command = command.lower().strip()

        if "show my memories" in command:

            return self.show_memories()

        if "forget my" in command:

            key = command.replace("forget my", "").strip()

            return self.forget(key)

        if "clear temporary memories" in command:

            return self.clear_temporary()

        if "lock memory" in command:

            self.locked = True

            return {"status": "memory_locked"}

        if "unlock memory" in command:

            self.locked = False

            return {"status": "memory_unlocked"}

        return {"status": "unknown_command"}

    def show_memories(self):

        if self.locked:

            return {"status": "memory_locked"}

        return {"status": "success", "memories": self.memory.memories()}

    def forget(self, key):

        return self.memory.forget(key)

    def clear_temporary(self):

        self.cleanup.clear_temporary()

        return {"status": "temporary_memories_cleared"}
