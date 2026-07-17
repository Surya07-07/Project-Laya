import json

from core.ai.service import AIService


class AIPlanner:

    def __init__(self):

        self.ai = AIService()

    def create_plan(self, command):

        prompt = f"""
You are an AI task planner.

Convert the user's request into JSON.

Return ONLY valid JSON.

Format:

{{
    "goal":"",

    "priority":"normal",

    "tasks":[
        "...",
        "..."
    ]
}}

User Request:

{command}
"""

        response = self.ai.ask(prompt)

        try:

            return json.loads(response)

        except Exception:

            return {

                "goal": command,

                "priority": "normal",

                "tasks": [

                    command

                ]

            }
