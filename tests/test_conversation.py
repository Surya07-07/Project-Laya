from core.conversation.history import ConversationHistory
from core.conversation.context import ContextBuilder

history = ConversationHistory()

history.add_user("My name is Surya.")
history.add_assistant("Hello Surya.")

history.add_user("I study AI.")

builder = ContextBuilder()

print(builder.build(history))