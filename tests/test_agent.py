from core.agent.agent import Agent


class DummyAI:

    def process(self, command):

        return "AI Response -> " + command


agent = Agent(DummyAI())

print(agent.process("Hello Laya"))
