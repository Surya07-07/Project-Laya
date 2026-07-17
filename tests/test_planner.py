from pprint import pprint

from core.agent.planner import GoalPlanner

planner = GoalPlanner()

while True:

    print()

    command = input("You : ")

    if command.lower() == "exit":

        break

    goal = planner.create_goal(command)

    print()

    print("=" * 60)

    pprint(goal.summary())

    print()
