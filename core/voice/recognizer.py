from faster_whisper import WhisperModel


class VoiceRecognizer:

    def __init__(self):

        print("Loading Whisper model...")

        self.model = WhisperModel("tiny", device="cpu", compute_type="int8")

        print("Whisper Ready.")

    def recognize(self, audio_file):

        segments, info = self.model.transcribe(audio_file)

        text = ""

        for segment in segments:
            text += segment.text + " "

        return text.strip()
