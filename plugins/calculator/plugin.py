class CalculatorPlugin:

    def run(self, expression):

        try:
            return eval(expression)

        except Exception:
            return "Invalid expression."