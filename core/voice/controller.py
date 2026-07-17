from core.voice.speech.whisper import SpeechRecognizer


class VoiceController:

    def __init__(self):

        self.recognizer = SpeechRecognizer()


    def check_wake_word(self, audio):

        text = self.recognizer.transcribe(audio)

        print("Heard:", text)


        if "hey laya" in text:
            return True

        return False
