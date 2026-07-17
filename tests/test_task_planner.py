from core.planner.task_planner import TaskPlanner

planner = TaskPlanner()

while True:

    command = input("You : ")

    if command == "exit":
        break

    result = planner.run(command)

    print()

    for item in result:

        print("Laya :", item)

    print()
