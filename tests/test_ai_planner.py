from pprint import pprint

from core.agent.ai_planner import AIPlanner

planner = AIPlanner()

while True:

    print()

    command = input("You : ")

    if command.lower() == "exit":

        break

    print()

    result = planner.create_plan(command)

    pprint(result)

    print()
