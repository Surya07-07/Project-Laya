from core.agent.goal import Goal


class GoalPlanner:

    def create_goal(self, command):

        text = command.lower().strip()

        goal = Goal(title=command)

        # ------------------------
        # Development
        # ------------------------

        if "laya" in text:

            goal.goal_type = "development"
            goal.priority = "high"

            goal.add_task("Open VS Code")
            goal.add_task("Open Project Folder")
            goal.add_task("Open Git Bash")
            goal.add_task("Start Ollama")
            goal.add_task("Load Memory")

            return goal

        # ------------------------
        # Study
        # ------------------------

        if "study" in text or "exam" in text:

            goal.goal_type = "study"
            goal.priority = "high"

            goal.add_task("Open Browser")
            goal.add_task("Open Notes")
            goal.add_task("Open PDF Reader")

            return goal

        # ------------------------
        # Coding
        # ------------------------

        if "code" in text or "program" in text:

            goal.goal_type = "coding"

            goal.priority = "high"

            goal.add_task("Open VS Code")
            goal.add_task("Open Terminal")

            return goal

        # ------------------------
        # Music
        # ------------------------

        if "music" in text:

            goal.goal_type = "music"

            goal.add_task("Open Spotify")

            return goal

        # ------------------------
        # Browser
        # ------------------------

        if "browser" in text or "internet" in text:

            goal.goal_type = "browser"

            goal.add_task("Open Browser")

            return goal

        # ------------------------
        # Default
        # ------------------------

        goal.goal_type = "general"

        goal.add_task(command)

        return goal
