from core.cognition.intent import IntentDetector
from core.agent.router import ActionRouter
from core.agent.executor import Executor
from core.agent.learning import LearningMemory
from core.memory.context import ContextManager
from core.agent.goal_manager import GoalManager
from core.agent.verifier import PlanVerifier
from core.agent.retry_engine import RetryEngine



class AgentBrain:


    def __init__(self):

        self.intent = IntentDetector()

        self.router = ActionRouter()

        self.executor = Executor()

        self.memory = LearningMemory()

        self.context = ContextManager()

        self.goal = GoalManager()

        self.verify = PlanVerifier()

        self.retry = RetryEngine()



    def think(self, request):


        print(
            "\n🧠 Laya Brain Thinking..."
        )


        # Intent

        intent = self.intent.detect(
            request
        )


        print(
            "Intent:",
            intent
        )



        # Tool selection

        tool = self.router.route(
            intent["intent"]
        )


        print(
            "Tool:",
            tool
        )



        # Goal creation

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



        while True:


            step = self.goal.next_step()


            if step is None:

                break



            result = self.retry.run(

                self.executor.execute,

                step["tool"],

                step["data"]

            )



            check = self.verify.verify(

                result["result"]

            )


            results.append({

                "execution": result,

                "verification": check

            })



            self.context.update(

                request,

                tool,

                result

            )



        memory = self.memory.save_success(

            request,

            intent["intent"],

            results

        )



        return {


            "intent": intent,

            "tool": tool,

            "goal": goal,

            "results": results,

            "context": self.context.get(),

            "memory": memory

        }
