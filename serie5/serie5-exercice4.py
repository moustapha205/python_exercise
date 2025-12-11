def appliquer_remise(prix: float, remise: float) -> float:
    """
    Calcule le prix final après application d'une remise.

    :param prix: prix initial en euros.
    :param remise: pourcentage de remise (0 à 1), par exemple 0.2 pour 20%.
    :return: prix final après remise.

    Exemple :
    >>> appliquer_remise(100, 0.2)
    80.0
    """
    prix_final = prix * (1 - remise)
    return prix_final


def compter_commandes_superieures(commandes: list[float], seuil: float) -> int:
    """
    Compte le nombre de commandes dont le montant est supérieur ou égal à un seuil.

    :param commandes: liste des montants de commandes.
    :param seuil: montant minimum à considérer.
    :return: nombre de commandes >= seuil.

    Exemple :
    >>> compter_commandes_superieures([50, 120, 200], 100)
    2
    """
    compteur = 0
    for montant in commandes:
        if montant >= seuil:
            compteur += 1
    return compteur


def normaliser_email(email: str) -> str:
    """
    Nettoie et normalise un email.

    - Supprime les espaces au début et à la fin.
    - Transforme tous les caractères en minuscules.

    :param email: email brut.
    :return: email normalisé.

    Exemple :
    >>> normaliser_email("  Test@Email.COM ")
    'test@email.com'
    """
    return email.strip().lower()


# Tests

if __name__ == "__main__":
    print(appliquer_remise(100, 0.2))                       
    print(compter_commandes_superieures([10, 50, 150], 30)) 
    print(normaliser_email("  Bonjour@TEST.com   "))        

    # Affichage de la docstring pour vérifier
    help(appliquer_remise)
