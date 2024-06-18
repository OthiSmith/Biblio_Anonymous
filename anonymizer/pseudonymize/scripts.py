import uuid
from anonymizer.base import DataAnonymizer

class PseudonymizationAnonymizer(DataAnonymizer):
    def anonymize(self, data: str) -> str:
        return str(uuid.uuid4())