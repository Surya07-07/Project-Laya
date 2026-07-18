from core.brain.agent_brain import AgentBrain


class VoiceAgentBridge:

    def __init__(self):

        self.brain = AgentBrain()

    def process_voice(self, text):

        print("\n🎤 Voice Input:")

        print(text)

        result = self.brain.think(text)

        return result
