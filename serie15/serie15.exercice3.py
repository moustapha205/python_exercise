# td15_ex3.py
from math import pi

class Forme:
    """Classe de base pour toutes les formes géométriques."""
    def aire(self):
        """Méthode abstraite/interface que toutes les sous-classes DOIVENT implémenter."""
        raise NotImplementedError("Méthode aire() à implémenter dans les sous-classes pour calculer la surface.")
        
    def __str__(self):
        # Affichage du nom de la classe, utile pour la boucle principale
        return f"Forme : {self.__class__.__name__}"


class Rectangle(Forme):
    """Hérite de Forme et implémente aire() pour un rectangle."""
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

class Cercle(Forme):
    """Hérite de Forme et implémente aire() pour un cercle."""
    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return pi * self.rayon**2

class TriangleRectangle(Forme):
    """Hérite de Forme et implémente aire() pour un triangle rectangle."""
    def __init__(self, base, hauteur):
        self.base = base
        self.hauteur = hauteur
        
    def aire(self):
        return (self.base * self.hauteur) / 2


# --- Fonction qui exploite le polymorphisme ---
def afficher_aires(formes):
    """
    Prend une liste d'objets de type Forme et appelle aire() sur chacun.
    """
    print("\n--- Fonction afficher_aires() (Polymorphisme) ---")
    for f in formes:
        # La fonction n'a pas besoin de savoir si f est un Cercle ou un Rectangle
        # Elle demande juste : "Peux-tu calculer ton aire ?"
        print(f"Type: {f.__class__.__name__:<15}, aire = {f.aire():.2f}")


# --- Bloc principal ---
if __name__ == "__main__":
    
    # Création d'une liste polymorphique
    formes = [
        Rectangle(4, 5), # aire = 20
        Cercle(3),       # aire = 28.27
        Rectangle(10, 2), # aire = 20
        TriangleRectangle(6, 4), # aire = 12
        Cercle(1)        # aire = 3.14
    ]

    # Appel de la fonction polymorphique
    afficher_aires(formes)

    # COMMENTAIRE sur le Polymorphisme
    """
    La fonction 'afficher_aires' illustre le polymorphisme (spécifiquement le duck typing
    et l'héritage) car elle ne vérifie JAMAIS le type exact (isinstance) de l'objet 'f'.
    
    Elle se contente de savoir que chaque objet dans la liste POSSÈDE une méthode 'aire()'.
    L'appel 'f.aire()' est interprété différemment par Python à l'exécution :
    - Si f est un Rectangle, il utilise la formule Rectangle.aire().
    - Si f est un Cercle, il utilise la formule Cercle.aire().
    
    C'est la capacité d'un même appel à avoir plusieurs formes de comportement.
    """