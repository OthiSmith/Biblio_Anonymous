from anonymizer.base import DataAnonymizer

class SubstitutionAnonymizer(DataAnonymizer):
    def __init__(self, substitution_dict: dict):
        self.substitution_dict = substitution_dict
        """
            Substitution_dict est un dictionnaire ayant comme clef une lettre ou mot de data et comme
            valeur l'élément à substituer.
        """

    def anonymize(self, data: str) -> str:
        return ''.join([self.substitution_dict.get(char, char) for char in data])