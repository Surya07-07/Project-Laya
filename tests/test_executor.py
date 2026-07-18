from core.agent.executor import GoalExecutor
from core.agent.planner import GoalPlanner

planner = GoalPlanner()

executor = GoalExecutor()

while True:

    print()

    command = input("You : ")

    if command.lower() == "exit":

        break

    goal = planner.create_goal(command)

    print()

    print("Goal")

    print("-" * 40)

    print(goal.summary())

    print()

    print("Executing...")

    print()

    result = executor.execute(goal)

    for item in result:

        print("✓", item)
