import random
from anonymizer.base import DataAnonymizer

class RandomizationAnonymizer(DataAnonymizer):
    def anonymize(self, data: str) -> str:
        if data.isdigit():
            number = int(data)
            return str(number + random.randint(-10, 10))
        return data