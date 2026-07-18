from core.brain.agent_brain import AgentBrain

laya = AgentBrain()


print("""
=========================
      PROJECT IGRIS
          LAYA

      Brain Mode
=========================
""")


while True:

    user = input("\nYou: ")

    if user.lower() in ["exit", "quit"]:

        print("Laya shutting down...")

        break

    # remove You: if typed accidentally

    if user.lower().startswith("you:"):

        user = user[4:].strip()

    result = laya.think(user)

    print("\nLaya:")

    print(result)
