import torch
from silero_vad import get_speech_timestamps, load_silero_vad


class VoiceActivityDetector:

    def __init__(self):

        print("🛡️ Loading VAD...")

        self.model = load_silero_vad()

        print("✅ VAD loaded")

    def has_voice(self, audio, sample_rate=16000):

        audio_tensor = torch.tensor(audio, dtype=torch.float32)

        speech = get_speech_timestamps(
            audio_tensor, self.model, sampling_rate=sample_rate
        )

        return len(speech) > 0
