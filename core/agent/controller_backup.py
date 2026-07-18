from core.agent.executor import Executor
from core.agent.planner import AIPlanner
from core.agent.validator import SafetyValidator


class AgentController:

    def __init__(self):

        self.planner = AIPlanner()
        self.validator = SafetyValidator()
        self.executor = Executor()

    def process(self, request):

        print("\n🧠 Creating plan...")

        goal = self.planner.create_plan(request)

        print("\n🛡️ Checking safety...")

        security = self.validator.validate(goal)

        if not security["allowed"]:

            return {"status": "blocked", "security": security}

        print("\n⚙️ Executing task...")

        result = self.executor.execute("create_folder", "Laya_Test")

        return {"plan": goal.show(), "security": security, "execution": result}
