import sounddevice as sd
import webrtcvad
import wave
import collections
import time


class Microphone:


    def __init__(self):

        self.sample_rate = 16000
        self.device = 1

        self.vad = webrtcvad.Vad(2)



    def listen_for_speech(self, filename="data/input.wav"):


        print("🎤 Listening silently...")


        frame_ms = 30

        frame_size = int(
            self.sample_rate * frame_ms / 1000
        )


        ring = collections.deque(
            maxlen=15
        )


        audio_frames = []


        triggered = False

        silence = 0

        max_frames = int(
            10 * 1000 / frame_ms
        )


        counter = 0



        with sd.InputStream(
            samplerate=self.sample_rate,
            channels=1,
            dtype="int16",
            device=self.device
        ) as stream:



            while True:


                frame, _ = stream.read(
                    frame_size
                )


                counter += 1


                raw = frame.tobytes()


                speech = self.vad.is_speech(
                    raw,
                    self.sample_rate
                )



                if not triggered:


                    ring.append(
                        (raw, speech)
                    )


                    score = sum(
                        1 for _,x in ring if x
                    )


                    if score > 10:


                        print(
                            "🎙 Voice started"
                        )


                        triggered=True


                        for data,_ in ring:

                            audio_frames.append(data)


                        ring.clear()



                else:


                    audio_frames.append(raw)


                    if speech:

                        silence=0

                    else:

                        silence += 1



                    if silence > 20:

                        print(
                            "🛑 Voice stopped"
                        )

                        break



                # safety timeout

                if counter > max_frames:


                    print(
                        "⏱ Timeout"
                    )

                    break



        # ignore tiny recordings

        if len(audio_frames) < 20:

            return None



        with wave.open(
            filename,
            "wb"
        ) as wf:


            wf.setnchannels(1)

            wf.setsampwidth(2)

            wf.setframerate(
                self.sample_rate
            )

            wf.writeframes(
                b"".join(audio_frames)
            )



        print(
            "💾 Saved:",
            filename
        )


        return filename



    def record(self,seconds=3):

        return self.listen_for_speech()
