from faster_whisper import WhisperModel


class WhisperEngine:

    def __init__(self):

        print("Loading Whisper Tiny Model...")

        self.model = WhisperModel("tiny", device="cpu", compute_type="int8")

        print("✅ Whisper Ready")

    def transcribe(self, filename):

        segments, _ = self.model.transcribe(filename)

        text = ""

        for segment in segments:
            text += segment.text

        return text.strip()
