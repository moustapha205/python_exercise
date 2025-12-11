# td15_ex2.py

class CompteBancaire:
    """Classe de base avec les fonctionnalités communes : dépôt et retrait simple."""
    
    def __init__(self, titulaire, solde_initial=0):
        self.titulaire = titulaire
        self.solde = solde_initial
        print(f" Compte créé pour {titulaire}. Solde initial : {self.solde:.2f}€")

    def deposer(self, montant):
        if montant <= 0:
            raise ValueError("Le montant du dépôt doit être positif.")
        self.solde += montant
        print(f"   Dépôt de {montant:.2f}€.")

    def retirer(self, montant):
        """Retrait standard sans découvert."""
        if montant <= 0:
            raise ValueError("Le montant du retrait doit être positif.")
        if montant > self.solde:
            raise ValueError(f"Solde insuffisant (Max: {self.solde:.2f}€).")
        
        self.solde -= montant
        print(f"   Retrait de {montant:.2f}€.")

    def afficher(self):
        print(f"\n--- {self.titulaire} ---")
        print(f"Solde final : {self.solde:.2f}€")
        # Affichage d'informations spécifiques à la sous-classe (Polymorphisme)
        if hasattr(self, 'taux_interet'):
            print(f"Type: Compte Épargne | Taux : {self.taux_interet * 100:.2f}%")
        elif hasattr(self, 'decouvert_autorise'):
            print(f"Type: Compte Courant | Découvert autorisé : {self.decouvert_autorise:.2f}€")
        else:
            print("Type: Compte Bancaire Standard")


class CompteEpargne(CompteBancaire):
    """Hérite de CompteBancaire et ajoute le concept de taux d'intérêt."""
    
    def __init__(self, titulaire, solde_initial=0, taux_interet=0.02):
        # 1. Utilisation de super() pour réutiliser l'initialisation du parent
        super().__init__(titulaire, solde_initial) 
        self.taux_interet = taux_interet

    def appliquer_interets(self):
        """Méthode spécifique au Compte Epargne."""
        montant_interets = self.solde * self.taux_interet
        self.solde += montant_interets
        print(f"   Intérêts appliqués ({self.taux_interet * 100:.2f}%) : +{montant_interets:.2f}€.")


class CompteCourant(CompteBancaire):
    """Hérite de CompteBancaire et surcharge retirer() pour autoriser le découvert."""
    
    def __init__(self, titulaire, solde_initial=0, decouvert_autorise=500.0):
        # 1. Utilisation de super() pour réutiliser l'initialisation du parent
        super().__init__(titulaire, solde_initial)
        self.decouvert_autorise = decouvert_autorise

    def retirer(self, montant):
        """
        Surcharge de la méthode retirer() : autorise le découvert.
        """
        if montant <= 0:
            raise ValueError("Le montant du retrait doit être positif.")
        
        # Le seuil minimum est -decouvert_autorise
        seuil_min = -self.decouvert_autorise
        nouveau_solde = self.solde - montant
        
        if nouveau_solde < seuil_min:
            raise ValueError(f"Découvert dépassé (Max autorisé: {self.decouvert_autorise:.2f}€).")
            
        self.solde = nouveau_solde
        print(f"   Retrait de {montant:.2f}€. Nouveau solde: {self.solde:.2f}€.")


# --- Bloc principal ---
if __name__ == "__main__":
    
    compte_std = CompteBancaire("Paul", 100)
    compte_epargne = CompteEpargne("Alice", 500, taux_interet=0.03) # 3%
    compte_courant = CompteCourant("Bob", 200, decouvert_autorise=300)

    # Scénario
    print("\n--- Scénario ---")
    
    compte_epargne.deposer(100) # Alice dépose 100
    compte_epargne.appliquer_interets() # Alice gagne des intérêts
    
    compte_courant.retirer(350) # Bob retire 350. Solde = 200 - 350 = -150 (OK, car découvert max est -300)
    
    try:
        compte_courant.retirer(200) # Bob tente de retirer 200 de plus. Solde = -150 - 200 = -350 (Trop)
    except ValueError as e:
        print(f"    ERREUR interceptée : {e}")
        
    # Affichage des soldes finaux (Polymorphisme : chaque objet répond à afficher())
    compte_std.afficher()
    compte_epargne.afficher()
    compte_courant.afficher()
    
    # COMMENTAIRES
    """
    Utilisation de super() :
    - Dans __init__ de CompteEpargne et CompteCourant : super().__init__(titulaire, solde_initial)
      permet de réutiliser la logique d'initialisation du titulaire et du solde
      définie dans la classe parente (CompteBancaire).
      
    Méthodes surchargées :
    - CompteCourant surcharge la méthode retirer(self, montant) pour implémenter une 
      règle spécifique (vérification du découvert autorisé) qui diffère de la règle 
      de la classe parente (solde doit être >= 0).
      
    Cas particuliers :
    - CompteEpargne et CompteCourant sont des cas particuliers de CompteBancaire 
      (relation "est un") car ils possèdent l'état et le comportement de base 
      (titulaire, solde, déposer) mais ajoutent (Epargne) ou modifient (Courant) 
      une partie de ce comportement.
    """