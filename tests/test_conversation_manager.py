from core.conversation.conversation_manager import ConversationManager

cm = ConversationManager()

cm.language("en")

cm.emotion("happy")

cm.user("Hello Laya")

cm.assistant("Hello! How can I help you?")

cm.user("My name is Surya")

print("=" * 40)
print(cm.prompt())
print("=" * 40)
print(cm.info())
