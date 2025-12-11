def get_age_lbyl(utilisateur):
    """
    Version LBYL (Look Before You Leap) :
    On vérifie si la clé existe avant d'essayer de l'utiliser.
    """
    if "age" in utilisateur:
        return utilisateur["age"]
    else:
        print("Clé 'age' manquante (LBYL).")
        return None


def get_age_eafp(utilisateur):
    """
    Version EAFP (Easier to Ask Forgiveness than Permission) :
    On tente d'accéder à la clé, et si elle n'existe pas → KeyError.
    """
    try:
        return utilisateur["age"]
    except KeyError:
        print("Clé 'age' manquante (EAFP).")
        return None


# -------- Bloc principal pour tester les fonctions --------
if __name__ == "__main__":

    utilisateur_complet = {"nom": "Alice", "age": 25}
    utilisateur_incomplet = {"nom": "Bob"}

    print("--- Test LBYL ---")
    print("Avec clé age :", get_age_lbyl(utilisateur_complet))
    print("Sans clé age :", get_age_lbyl(utilisateur_incomplet))

    print("\n--- Test EAFP ---")
    print("Avec clé age :", get_age_eafp(utilisateur_complet))
    print("Sans clé age :", get_age_eafp(utilisateur_incomplet))
