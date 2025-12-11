def lire_fichier_securise(nom_fichier):
    """
    Essaie de lire le contenu d'un fichier.
    Retourne le contenu sous forme de chaîne si tout va bien,
    ou None si le fichier n'existe pas.
    """
    try:
        with open(nom_fichier, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Erreur : le fichier '{nom_fichier}' n'a pas été trouvé.")
        return None

# Bloc principal
nom_fichier = input("Saisissez le nom du fichier à lire : ")
contenu = lire_fichier_securise(nom_fichier)

if contenu is not None:
    print("Contenu du fichier :")
    print(contenu)
else:
    print("Lecture impossible")
