class ContextEngine:

    def build(
        self,
        history,
        memories,
        user_message
    ):

        prompt = ""

        prompt += "### Conversation ###\n\n"

        for item in history:

            prompt += f"{item.role}: {item.text}\n"

        prompt += "\n"

        prompt += "### Memory ###\n\n"

        for key, value in memories.items():

            prompt += f"{key}: {value}\n"

        prompt += "\n"

        prompt += "### User ###\n\n"

        prompt += user_message

        return prompt