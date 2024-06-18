from anonymizer.base import DataAnonymizer

class SubstitutionAnonymizer(DataAnonymizer):
    def __init__(self, substitution_dict: dict):
        self.substitution_dict = substitution_dict

    def anonymize(self, data: str) -> str:
        return ''.join([self.substitution_dict.get(char, char) for char in data])