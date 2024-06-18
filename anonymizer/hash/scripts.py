import hashlib
from anonymizer.base import DataAnonymizer

class HashingAnonymizer(DataAnonymizer):
    def anonymize(self, data: str) -> str:
        return hashlib.sha256(data.encode()).hexdigest()