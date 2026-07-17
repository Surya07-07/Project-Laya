from core.voice.wake_word import WakeWordDetector
from core.voice.speech_recognizer import SpeechRecognizer
from core.voice.agent_bridge import VoiceAgentBridge



wake = WakeWordDetector()

speech = SpeechRecognizer()

brain = VoiceAgentBridge()



print("""
=========================
       PROJECT IGRIS
           LAYA

       WAKE MODE
=========================
""")


while True:


    if wake.detected():


        print(
            "\n🎤 Listening Command..."
        )


        command = speech.transcribe()



        print(
            "Command:",
            command
        )



        if command:


            result = brain.process_voice(
                command
            )


            print(
                "\nLaya:"
            )


            print(
                result
            )
