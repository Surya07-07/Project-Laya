from core.agent.context import AgentContext
from core.agent.executor import Executor
from core.agent.planner import Planner
from core.agent.result import AgentResult


class Agent:

    def __init__(self, ai_core):

        self.ai = ai_core

        self.context = AgentContext()

        self.planner = Planner()

        self.executor = Executor()

    def process(self, command):

        self.context.reset()

        self.context.command = command

        plan = self.planner.plan(self.context)

        self.executor.execute(plan)

        result = AgentResult()

        result.response = self.ai.process(command)

        return result.response
