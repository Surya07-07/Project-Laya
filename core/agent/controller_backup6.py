from core.agent.executor import Executor
from core.agent.goal_manager import GoalManager
from core.agent.learning import LearningMemory
from core.agent.router import ActionRouter
from core.agent.verifier import PlanVerifier
from core.cognition.intent import IntentDetector


class AgentController:

    def __init__(self):

        self.executor = Executor()

        self.memory = LearningMemory()

        self.intent = IntentDetector()

        self.router = ActionRouter()

        self.goal = GoalManager()

        self.verifier = PlanVerifier()

    def process(self, request):

        print("\n🧠 Detecting intent...")

        intent_result = self.intent.detect(request)

        tool = self.router.route(intent_result["intent"])

        print("Intent:", intent_result)

        print("Tool:", tool)

        print("\n🧩 Creating goal...")

        goal = self.goal.create_goal(request, [{"tool": tool, "data": request}])

        results = []

        print("\n⚙️ Executing...")

        while True:

            step = self.goal.next_step()

            if step is None:

                break

            result = self.executor.execute(step["tool"], step["data"])

            verification = self.verifier.verify(result)

            results.append({"result": result, "verification": verification})

            if not verification["verified"]:

                print("🔄 Attempt failed")

            else:

                print("✅ Step verified")

        memory = self.memory.save_success(request, intent_result["intent"], results)

        return {"goal": goal, "results": results, "memory": memory}
