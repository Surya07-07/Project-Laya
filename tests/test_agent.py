from core.agent.planner import AIPlanner


planner = AIPlanner()

goal = planner.create_plan(
    "Organize my downloads folder"
)

print("\n🧠 Laya AI Agent Test\n")

print(goal.show())
