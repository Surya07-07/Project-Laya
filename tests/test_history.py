from core.conversation.history import ConversationHistory

history = ConversationHistory()

history.add("User", "Hello")

history.add("Laya", "Hi!")

history.add("User", "How are you?")

history.add("Laya", "I'm good!")

print(history.last())

print("Messages:", history.size())