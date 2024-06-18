from anonymizer.base import DataAnonymizer

class GeneralizationAnonymizer(DataAnonymizer):
    def anonymize(self, data: str) -> str:
        return "generalized_value"