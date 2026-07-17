from pprint import pprint

from core.agent.goal import Goal


goal = Goal(

    title="Continue Project Laya",

    goal_type="development",

    priority="high"

)

goal.add_task("Open VS Code")

goal.add_task("Open Project Folder")

goal.add_task("Start Ollama")

goal.add_task("Load Memory")

goal.add_task("Open Git Bash")

goal.add_note("Resume previous milestone")

goal.add_note("Check runtime status")

print()

print("=" * 60)

print("PROJECT LAYA GOAL TEST")

print("=" * 60)

print()

pprint(goal.summary())

print()

print("✓ Goal Manager Working")
