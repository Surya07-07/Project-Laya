from cryptography.fernet import Fernet, InvalidToken
import os


class EncryptionManager:


    def __init__(self):

        self.key_file = "data/laya.key"

        self.key = self.load_key()

        self.cipher = Fernet(self.key)



    def load_key(self):

        if not os.path.exists(self.key_file):

            key = Fernet.generate_key()

            with open(self.key_file, "wb") as file:
                file.write(key)

            return key


        with open(self.key_file, "rb") as file:

            return file.read()



    def encrypt(self, text):

        return self.cipher.encrypt(
            text.encode()
        ).decode()



    def decrypt(self, text):

        try:

            return self.cipher.decrypt(
                text.encode()
            ).decode()


        except InvalidToken:

            # Old unencrypted memories
            return text