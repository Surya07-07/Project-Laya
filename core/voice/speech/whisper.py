from faster_whisper import WhisperModel


class SpeechRecognizer:

    def __init__(self):

        print("🎧 Loading Whisper model...")

        self.model = WhisperModel("small", device="cpu", compute_type="int8")

        print("✅ Whisper Ready")

    def transcribe(self, audio_file):

        segments, info = self.model.transcribe(audio_file, language="en", beam_size=5)

        text = ""

        for segment in segments:

            text += segment.text

        return text.lower().strip()
