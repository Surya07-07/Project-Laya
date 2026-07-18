from core.agent.executor import Executor
from core.agent.learning import LearningMemory
from core.agent.planner import AIPlanner
from core.agent.validator import SafetyValidator
from core.cognition.intent import IntentDetector


class AgentController:

    def __init__(self):

        self.planner = AIPlanner()

        self.validator = SafetyValidator()

        self.executor = Executor()

        self.memory = LearningMemory()

        self.intent = IntentDetector()

    def process(self, request):

        print("\n🧠 Detecting intent...")

        intent_result = self.intent.detect(request)

        print("Intent:", intent_result)

        print("\n🧩 Creating plan...")

        goal = self.planner.create_plan(request)

        security = self.validator.validate(goal)

        if not security["allowed"]:

            return {"status": "blocked", "security": security}

        result = self.executor.execute("create_folder", "Laya_Test")

        memory = self.memory.save_success(request, intent_result["intent"], result)

        return {
            "intent": intent_result,
            "plan": goal.show(),
            "security": security,
            "execution": result,
            "memory": memory,
        }
