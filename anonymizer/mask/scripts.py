from anonymizer.base import DataAnonymizer

class MaskingAnonymizer(DataAnonymizer):
    def anonymize(self, data: str) -> str:
        return ''.join(['X' for _ in data])