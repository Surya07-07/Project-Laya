class LanguageManager:

    LANGUAGE_NAMES = {
        "en": "English",
        "te": "Telugu",
        "hi": "Hindi",
        "ta": "Tamil",
        "kn": "Kannada",
        "ml": "Malayalam",
        "mr": "Marathi",
        "bn": "Bengali",
        "gu": "Gujarati",
        "pa": "Punjabi",
        "ur": "Urdu"
    }

    def __init__(self):

        self.current_language = "en"

    def update(self, language_code):

        if language_code:

            self.current_language = language_code

    def code(self):

        return self.current_language

    def name(self):

        return self.LANGUAGE_NAMES.get(
            self.current_language,
            self.current_language
        )
