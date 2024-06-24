import os
from anonymizer.mask.scripts import MaskingAnonymizer
from anonymizer.pseudonymize.scripts import PseudonymizationAnonymizer
from anonymizer.suppress.scripts import SuppressionAnonymizer
from anonymizer.hash.scripts import HashingAnonymizer
from anonymizer.substitute.scripts import SubstitutionAnonymizer
from anonymizer.generalize.scripts import GeneralizationAnonymizer
from anonymizer.randomize.scripts import RandomizationAnonymizer
from anonymizer.crypto.scripts import CryptographyAnonymizer
from anonymizer.tokenize.scripts import TokenizationAnonymizer
from anonymizer.perturb.scripts import PerturbationAnonymizer
from cryptography.fernet import Fernet

class Anonymizer:
    def __init__(self):
        self.anonymizers = {
            'mask': MaskingAnonymizer(),
            'pseudonymize': PseudonymizationAnonymizer(),
            'suppress': SuppressionAnonymizer(),
            'hash': HashingAnonymizer(),
            'substitute': SubstitutionAnonymizer(substitution_dict={'a': '@', 'e': '3', 'i': '1', 'o': '0', 'u': 'ü'}),
            'generalize': GeneralizationAnonymizer(),
            'randomize': RandomizationAnonymizer(),
            'crypto': CryptographyAnonymizer(Fernet.generate_key()),
            'tokenize': TokenizationAnonymizer(),
            'perturb': PerturbationAnonymizer()
        }

    def anonymize_text(self, text: str, method: str) -> str:
        anonymizer = self.anonymizers.get(method)
        if anonymizer:
            return anonymizer.anonymize(text)
        return text

    def anonymize_file(self, file_path: str, method: str):
        if not os.path.isfile(file_path):
            print(f"File {file_path} does not exist.")
            return

        with open(file_path, 'r') as file:
            content = file.read()

        anonymized_content = self.anonymize_text(content, method)

        # Générer un nouveau chemin d'accès au fichier
        directory, filename = os.path.split(file_path)
        name, ext = os.path.splitext(filename)
        new_file_path = os.path.join(directory, f"{name}_anonymized{ext}")

        with open(new_file_path, 'w') as new_file:
            new_file.write(anonymized_content)

        print(f"Fichier anonymisé créé dans: {new_file_path}")
            
if __name__ == '__main__':
    anonymizer = Anonymizer()

    # Anonymiser un texte
    texte = "Anonymisation de texte"
    texte_anonymise = anonymizer.anonymize_text(texte, 'pseudonymize')
    print("Texte anonymisé:", texte_anonymise)

    # Anonymiser un fichier
    anonymizer.anonymize_file('test.txt', 'pseudonymize')