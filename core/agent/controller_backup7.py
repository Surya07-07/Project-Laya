from core.agent.executor import Executor
from core.agent.learning import LearningMemory
from core.cognition.intent import IntentDetector
from core.agent.router import ActionRouter
from core.agent.goal_manager import GoalManager
from core.agent.verifier import PlanVerifier
from core.agent.retry_engine import RetryEngine



class AgentController:


    def __init__(self):

        self.executor = Executor()

        self.memory = LearningMemory()

        self.intent = IntentDetector()

        self.router = ActionRouter()

        self.goal = GoalManager()

        self.verifier = PlanVerifier()

        self.retry = RetryEngine()



    def process(self, request):


        print("\n🧠 Detecting intent...")


        intent_result = self.intent.detect(
            request
        )


        tool = self.router.route(
            intent_result["intent"]
        )


        print(
            "Intent:",
            intent_result
        )


        print(
            "Tool:",
            tool
        )



        goal = self.goal.create_goal(

            request,

            [

                {

                    "tool": tool,

                    "data": request

                }

            ]

        )



        results = []



        print("\n⚙️ Executing goal...")


        while True:


            step = self.goal.next_step()


            if step is None:

                break



            retry_result = self.retry.run(

                self.executor.execute,

                step["tool"],

                step["data"]

            )



            verification = self.verifier.verify(

                retry_result["result"]

            )



            results.append({

                "retry": retry_result,

                "verification": verification

            })



            if verification["verified"]:

                print(
                    "✅ Task completed"
                )

            else:

                print(
                    "❌ Task failed after retries"
                )



        memory = self.memory.save_success(

            request,

            intent_result["intent"],

            results

        )



        return {

            "goal": goal,

            "results": results,

            "memory": memory

        }
