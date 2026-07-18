from core.agent.executor import Executor
from core.agent.goal_manager import GoalManager
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

        self.goal = GoalManager()

    def process(self, request):

        print("\n🧠 Detecting intent...")

        intent_result = self.intent.detect(request)

        tool = self.router.route(intent_result["intent"])

        print("Intent:", intent_result)

        print("Tool:", tool)

        print("\n🧩 Planning goal...")

        goal = self.goal.create_goal(request, [{"tool": tool, "data": request}])

        print(goal)

        print("\n⚙️ Executing steps...")

        results = []

        while True:

            step = self.goal.next_step()

            if step is None:

                break

            result = self.executor.execute(step["tool"], step["data"])

            results.append(result)

        memory = self.memory.save_success(request, intent_result["intent"], results)

        return {"goal": goal, "results": results, "memory": memory}
