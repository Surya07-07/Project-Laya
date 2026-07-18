from core.security.encryption import EncryptionManager

security = EncryptionManager()


secret = "My name is Surya"


encrypted = security.encrypt(secret)


print("Encrypted:")
print(encrypted)


decrypted = security.decrypt(encrypted)


print("\nDecrypted:")
print(decrypted)
