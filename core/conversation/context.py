class ContextBuilder:

    def build(self, history):

        context = ""

        for msg in history.get_messages():
            context += f"{msg.role}: {msg.text}\n"

        return context