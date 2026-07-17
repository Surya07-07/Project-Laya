import speech_recognition as sr



class WakeWordDetector:


    def __init__(self):

        self.recognizer = sr.Recognizer()



    def listen(self):


        with sr.Microphone() as source:


            print(
                "\n🎤 Waiting for Hey Laya..."
            )


            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )


            audio = self.recognizer.listen(
                source
            )



        try:

            text = self.recognizer.recognize_google(
                audio
            )


            print(
                "Heard:",
                text
            )


            return text.lower()



        except:


            return ""



    def detected(self):


        text = self.listen()


        if "hey laya" in text:


            print(
                "✅ Wake word detected"
            )


            return True



        return False
