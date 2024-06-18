import uuid
from anonymizer.base import DataAnonymizer

class TokenizationAnonymizer(DataAnonymizer):
    def __init__(self):
        self.token_map = {}

    def anonymize(self, data: str) -> str:
        if data not in self.token_map:
            self.token_map[data] = str(uuid.uuid4())
        return self.token_map[data]