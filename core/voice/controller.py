from core.voice.speech.whisper import SpeechRecognizer


class VoiceController:

    def __init__(self):

        self.recognizer = SpeechRecognizer()

    def check_wake_word(self, audio_file):

        text = self.recognizer.transcribe(audio_file)

        print("Heard:", text)

        if len(text) < 5:

            return False

        wake_words = [
            "hey laya",
            "hey leia",
            "hey leya",
            "hey layer",
            "hey layout",
            "hey player",
        ]

        for word in wake_words:

            if word in text:

                return True

        return False
