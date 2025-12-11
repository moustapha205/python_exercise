class CompteBancaire:
    """
    Modélise un compte bancaire avec un titulaire et un solde.
    Permet les opérations de dépôt et de retrait.
    """
    def __init__(self, titulaire, solde=0):
        """Constructeur du compte, solde initialisé à 0 par défaut."""
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        """Ajoute le montant au solde si le montant est positif."""
        if montant > 0:
            self.solde += montant
            print(f" Dépôt de {montant}€ effectué. Nouveau solde : {self.solde}€")
        else:
            print(" Erreur : Le montant du dépôt doit être positif.")

    def retirer(self, montant):
        """Soustrait le montant si le solde est suffisant."""
        if montant < 0:
            print(" Erreur : Le montant du retrait doit être positif.")
        elif montant > self.solde:
            print(f"Erreur : Solde insuffisant ({self.solde}€) pour un retrait de {montant}€.")
        else:
            self.solde -= montant
            print(f" Retrait de {montant}€ effectué. Nouveau solde : {self.solde}€")

    def afficher(self):
        """Affiche le titulaire et le solde actuel."""
        print(f"\n--- Compte de {self.titulaire} ---")
        print(f"Solde actuel : {self.solde}€")


# Bloc principal pour les tests
if __name__ == "__main__":
    compte_alice = CompteBancaire("Alice Dupont")
    compte_bob = CompteBancaire("Bob Martin", 500)

    # Historique des opérations d'Alice
    compte_alice.afficher()
    
    compte_alice.deposer(150)
    compte_alice.retirer(50)
    compte_alice.deposer(300.50)
    
    # Test des cas d'erreur
    compte_alice.retirer(1000)  # Solde insuffisant
    compte_alice.deposer(-10)   # Montant négatif
    
    compte_alice.afficher()

    # Affichage du compte de Bob
    compte_bob.afficher()