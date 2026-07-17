from core.agent.goal import Goal
from core.ai.ollama_client import OllamaClient


class AIPlanner:


    def __init__(self):
        self.ai = OllamaClient()


    def create_plan(self, request):

        prompt = f"""
You are Laya AI Planner.

User Goal:
{request}

Create a safe step-by-step plan.

Rules:
- Do not perform dangerous actions.
- Explain steps clearly.
- Mention if permission is required.
"""

        response = self.ai.ask(prompt)


        goal = Goal(request)

        goal.add_step(response)

        goal.risk = "unknown"
        goal.permission_required = True

        goal.update_status(
            "planned_by_ai"
        )

        return goal
