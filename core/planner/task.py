class Task:

    def __init__(self, action, target):

        self.action = action

        self.target = target

    def __repr__(self):

        return f"{self.action} -> {self.target}"
