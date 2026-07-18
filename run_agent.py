from core.agent.controller import AgentController
from core.voice.bridge import VoiceBridge

agent = AgentController()

voice = VoiceBridge(agent)


print("""
========================
      PROJECT IGRIS
          LAYA

 AI Agent Mode Started
========================
""")


while True:

    user = input("\nYou: ")

    if user.lower() in ["exit", "quit"]:

        print("Laya shutting down...")

        break

    response = voice.handle_voice_input(user)

    print("\nLaya:", response)
