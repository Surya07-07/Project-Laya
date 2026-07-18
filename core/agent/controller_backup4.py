from core.agent.executor import Executor
from core.agent.learning import LearningMemory
from core.agent.planner import AIPlanner
from core.agent.router import ActionRouter
from core.agent.validator import SafetyValidator
from core.cognition.intent import IntentDetector
from core.security.permission import PermissionManager


class AgentController:

    def __init__(self):

        self.planner = AIPlanner()

        self.validator = SafetyValidator()

        self.executor = Executor()

        self.memory = LearningMemory()

        self.intent = IntentDetector()

        self.router = ActionRouter()

        self.permission = PermissionManager()

    def process(self, request):

        print("\n🧠 Detecting intent...")

        intent_result = self.intent.detect(request)

        print("Intent:", intent_result)

        tool = self.router.route(intent_result["intent"])

        print("Tool:", tool)

        print("\n🧩 Creating plan...")

        goal = self.planner.create_plan(request)

        print("\n🛡️ Checking safety...")

        security = self.validator.validate(goal)

        if not security["allowed"]:

            return {"status": "blocked", "security": security}

        if self.permission.requires_permission(request):

            approved = self.permission.ask_permission(request)

            if not approved:

                return {"status": "permission_denied"}

        print("\n⚙️ Executing task...")

        result = self.executor.execute(tool, request)

        memory = self.memory.save_success(request, intent_result["intent"], result)

        return {
            "intent": intent_result,
            "tool": tool,
            "execution": result,
            "memory": memory,
        }
