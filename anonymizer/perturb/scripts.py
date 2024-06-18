import random
from anonymizer.base import DataAnonymizer

class PerturbationAnonymizer(DataAnonymizer):
    def anonymize(self, data: str) -> str:
        if data.replace('.', '', 1).isdigit():
            number = float(data)
            return str(number + random.uniform(-5.0, 5.0))
        return data