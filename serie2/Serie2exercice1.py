
mot_de_passe = input("Entrez votre mot de passe : ")


a_longueur = len(mot_de_passe) >= 8
a_minuscule = any(c.islower() for c in mot_de_passe)
a_majuscule = any(c.isupper() for c in mot_de_passe)
a_chiffre = any(c.isdigit() for c in mot_de_passe)


if a_longueur and a_minuscule and a_majuscule and a_chiffre:
    print("Mot de passe valide")
else:
    print("Mot de passe invalide pour les raisons suivantes :")
    if not a_longueur:
        print("- Le mot de passe doit contenir au moins 8 caractères")
    if not a_minuscule:
        print("- Il manque une lettre minuscule")
    if not a_majuscule:
        print("- Il manque une lettre majuscule")
    if not a_chiffre:
        print("- Il manque un chiffre")
