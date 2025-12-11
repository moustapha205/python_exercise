class Employe:
    """Classe de base pour tous les employés."""
    def __init__(self, nom, salaire_base):
        self.nom = nom
        self.salaire_base = salaire_base

    def calculer_salaire(self):
        """Calcule le salaire (méthode de base)."""
        return self.salaire_base

    def afficher(self):
        """Affiche le nom et le salaire calculé."""
        # Utile pour obtenir le nom de la classe enfant (Manager ou Developpeur)
        type_employe = self.__class__.__name__ 
        salaire = self.calculer_salaire()
        print(f"| {type_employe:12} | {self.nom:15} | {salaire:10.2f}€ |")


class Developpeur(Employe):
    """Classe dérivée de Employe avec une prime technique."""
    def __init__(self, nom, salaire_base, prime_technique):
        # Appel du constructeur de la classe parente (Employe)
        super().__init__(nom, salaire_base)
        self.prime_technique = prime_technique

    def calculer_salaire(self):
        """Redéfinit la méthode pour inclure la prime technique."""
        return self.salaire_base + self.prime_technique


class Manager(Employe):
    """Classe dérivée de Employe avec une prime de management."""
    def __init__(self, nom, salaire_base, prime_management):
        # Appel du constructeur de la classe parente (Employe)
        super().__init__(nom, salaire_base)
        self.prime_management = prime_management

    def calculer_salaire(self):
        """Redéfinit la méthode pour inclure la prime de management."""
        return self.salaire_base + self.prime_management


# Bloc principal pour les tests
if __name__ == "__main__":
    # Création des instances
    e1 = Employe("Jean Dupont", 3000)
    d1 = Developpeur("Alice Martin", 3500, 500)
    d2 = Developpeur("Bob Tremblay", 3800, 750.50)
    m1 = Manager("Carole Petit", 4500, 1000)

    # Stockage dans une liste (Polymorphisme : chaque objet est un Employe)
    equipe = [e1, d1, d2, m1]

    print("--- Équipe et Salaires Calculés ---")
    print(f"| {'Type':12} | {'Nom':15} | {'Salaire Net':12} |")
    print("|" + "-"*12 + "|" + "-"*15 + "|" + "-"*12 + "|")
    
    for employe in equipe:
        # La méthode afficher appelle calculer_salaire() appropriée à chaque objet
        employe.afficher()
    
    print("-" * 43)