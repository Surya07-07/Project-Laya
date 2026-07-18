from faster_whisper import WhisperModel


class WhisperSTT:

    def __init__(self):

        print("🧠 Loading Whisper model...")

        self.model = WhisperModel("base", device="cpu", compute_type="int8")

        print("✅ Whisper loaded")

    def transcribe(self, audio):

        segments, info = self.model.transcribe(
            audio,
            language="en",
            task="transcribe",
            beam_size=5,
            vad_filter=True,
            temperature=0,
        )

        text = ""

        for segment in segments:
            text += segment.text

        return text.strip()
