class DataAnonymizer:
    """_summary_
        La classe DataAnonymiser est la classe mère de toutes les autres classes d'anonymisation considèrées 
        dans ce module.
    """
    def anonymize(self, data: str) -> str:
        """_summary_
        
        Args:
            data (str): contient le texte à anonymiser de type chaine de caractaire

        Raise: Permet de gerer les exception.
            NotImplementedError: Le type d'erreur que la fonction raise permet de gerer.

        Returns: La méthode retourne soit le message contenu dans data sous forme crypter soit le message
                d'erreur ci-après lorsque la methode n'existe pas dans le modèle.
        """
        raise NotImplementedError("Cette méthode doit être surchargée dans les sous-classes")