import os

def lire_fichier_lbyl(nom_fichier):
    """
    Version LBYL :
    - On vérifie d'abord si le fichier existe.
    - Si oui → on le lit.
    - Sinon → message + None.
    """
    if os.path.exists(nom_fichier):
        with open(nom_fichier, "r", encoding="utf-8") as f:
            return f.read()
    else:
        print(f"Fichier introuvable (LBYL) : {nom_fichier}")
        return None


def lire_fichier_eafp(nom_fichier):
    """
    Version EAFP :
    - On essaie d'ouvrir le fichier.
    - Si FileNotFoundError =>message + None.
    """
    try:
        with open(nom_fichier, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Fichier introuvable (EAFP) : {nom_fichier}")
        return None


#test
if __name__ == "__main__":

    print("--- TEST AVEC FICHIER EXISTANT  ---")
    print("LBYL :", lire_fichier_lbyl("data.txt"))
    print("EAFP :", lire_fichier_eafp("data.txt"))

    print("--- TEST AVEC FICHIER INEXISTANT ---")
    print("LBYL :", lire_fichier_lbyl("fichier_inexistant.txt"))
    print("EAFP :", lire_fichier_eafp("fichier_inexistant.txt"))
