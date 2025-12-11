class Rectangle:
    """
    Définit un rectangle avec sa largeur et sa hauteur,
    et permet de calculer sa surface et son périmètre.
    """
    def __init__(self, largeur, hauteur):
        """Constructeur pour initialiser la largeur et la hauteur."""
        self.largeur = largeur  # Attribut d'instance
        self.hauteur = hauteur  # Attribut d'instance

    def surface(self):
        """Retourne l'aire du rectangle (largeur * hauteur)."""
        return self.largeur * self.hauteur

    def perimetre(self):
        """Retourne le périmètre du rectangle (2 * (largeur + hauteur))."""
        return 2 * (self.largeur + self.hauteur)

    def afficher(self):
        """Affiche les informations complètes du rectangle."""
        print("-" * 30)
        print(f"Rectangle ({self.largeur} x {self.hauteur})")
        print(f"  Largeur : {self.largeur}")
        print(f"  Hauteur : {self.hauteur}")
        print(f"  Surface : {self.surface()}")
        print(f"  Périmètre : {self.perimetre()}")
        print("-" * 30)


# Bloc principal pour les tests
if __name__ == "__main__":
    # Création des instances (objets)
    r1 = Rectangle(4, 5)
    r2 = Rectangle(10, 2)
    r3 = Rectangle(7.5, 3)

    print("--- Affichage du Rectangle 1 ---")
    r1.afficher()

    print("\n--- Affichage du Rectangle 2 ---")
    r2.afficher()
    
    # Exemple d'accès direct aux attributs et méthodes
    print(f"\nLe Rectangle 3 a une largeur de {r3.largeur} et une surface de {r3.surface()}")