class VoiceBridge:


    def __init__(self, agent):

        self.agent = agent



    def handle_voice_input(self, text):

        print("\n🎤 User said:")
        print(text)


        result = self.agent.process(
            text
        )


        return result
