from core.agent.planner import AIPlanner
from core.agent.validator import SafetyValidator


class AgentController:


    def __init__(self):

        self.planner = AIPlanner()
        self.validator = SafetyValidator()


    def process(self, request):

        print("\n🧠 Creating plan...")

        goal = self.planner.create_plan(
            request
        )


        print("\n🛡️ Checking safety...")

        result = self.validator.validate(
            goal
        )


        return {
            "plan": goal.show(),
            "security": result
        }
