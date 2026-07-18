class GoalManager:

    def __init__(self):

        self.active_goal = None

    def create_goal(self, name, steps):

        self.active_goal = {
            "goal": name,
            "steps": steps,
            "current_step": 0,
            "status": "created",
        }

        return self.active_goal

    def next_step(self):

        if not self.active_goal:

            return None

        index = self.active_goal["current_step"]

        if index >= len(self.active_goal["steps"]):

            self.active_goal["status"] = "completed"

            return None

        step = self.active_goal["steps"][index]

        self.active_goal["current_step"] += 1

        return step

    def status(self):

        return self.active_goal
