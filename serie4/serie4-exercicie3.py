produits = ["PC Portable", "Écran", "Clavier", "Souris", "Casque"]

try:
    
    indice = int(input("Saisissez l'indice du produit : "))
    
    
    print("Produit sélectionné :", produits[indice])

except ValueError:
    print("Erreur : vous devez saisir un nombre entier.")

except IndexError:
    print(f"Indice invalide (doit être entre 0 et {len(produits) - 1}).")#je l'ai fait pour les autres exos si la liste est beaucoup plus complexe pour que ça marche avec n'importe quelle liste 
