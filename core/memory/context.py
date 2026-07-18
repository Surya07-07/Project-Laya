import time


class ContextManager:

    def __init__(self):

        self.context = {
            "last_action": None,
            "last_tool": None,
            "last_result": None,
            "time": None,
        }

    def update(self, action, tool, result):

        self.context = {
            "last_action": action,
            "last_tool": tool,
            "last_result": result,
            "time": time.time(),
        }

        return self.context

    def get(self):

        return self.context

    def clear(self):

        self.context = {
            "last_action": None,
            "last_tool": None,
            "last_result": None,
            "time": None,
        }
