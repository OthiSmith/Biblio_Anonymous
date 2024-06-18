from anonymizer.base import DataAnonymizer

class SuppressionAnonymizer(DataAnonymizer):
    def anonymize(self, data: str) -> str:
        return ""