from cryptography.fernet import Fernet
from anonymizer.base import DataAnonymizer

class CryptographyAnonymizer(DataAnonymizer):
    def __init__(self, key: bytes):
        """
        Args:
            key (bytes): C'est la clé de cryptage, elle est de type bytes.
        """
        self.cipher = Fernet(key)

    def anonymize(self, data: str) -> str:
        return self.cipher.encrypt(data.encode()).decode()