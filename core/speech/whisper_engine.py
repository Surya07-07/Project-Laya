from faster_whisper import WhisperModel


class WhisperEngine:

    def __init__(self):

        print("🧠 Loading Faster-Whisper...")

        self.model = WhisperModel("small", device="cpu", compute_type="int8")

        print("✅ Whisper Ready")

    def transcribe(self, audio_file):

        segments, info = self.model.transcribe(audio_file, beam_size=5, vad_filter=True)

        print()
        print("Detected Language :", info.language)
        print("Confidence        :", round(info.language_probability, 3))
        print()

        text = ""

        for segment in segments:
            text += segment.text

        return {
            "text": text.strip(),
            "language": info.language,
            "confidence": info.language_probability,
        }
