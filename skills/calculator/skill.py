from core.skills.base import Skill


class CalculatorSkill(Skill):

    name = "calculator"

    def can_handle(self, command):
        return command.lower().startswith("calc ")

    def execute(self, command):

        expression = command[5:]

        try:
            return str(eval(expression))
        except Exception:
            return "Invalid expression."
