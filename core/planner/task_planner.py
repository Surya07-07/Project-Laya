from core.planner.task_executor import TaskExecutor
from core.planner.task_parser import TaskParser


class TaskPlanner:

    def __init__(self):

        self.parser = TaskParser()

        self.executor = TaskExecutor()

    def run(self, command):

        tasks = self.parser.parse(command)

        results = []

        for task in tasks:

            results.append(self.executor.execute(task))

        return results
