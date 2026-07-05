class Skill:

    name = "base"

    def can_handle(self, command):
        return False

    def execute(self, command):
        return "Skill not implemented."