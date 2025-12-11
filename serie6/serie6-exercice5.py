class Client:
    """Représente un client."""
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email
    
    def __str__(self):
        """Méthode spéciale pour une représentation lisible de l'objet."""
        return f"{self.nom} <{self.email}>"


class LigneCommande:
    """Représente un article avec sa quantité dans une commande."""
    def __init__(self, description, quantite, prix_unitaire):
        self.description = description
        self.quantite = quantite
        self.prix_unitaire = prix_unitaire

    def total_ligne(self):
        """Calcule le montant total de cette ligne."""
        return self.quantite * self.prix_unitaire
    
    def __str__(self):
        return f"{self.quantite} x {self.description} ({self.prix_unitaire:.2f}€ / unité) = {self.total_ligne():.2f}€"


class Commande:
    """Représente une commande passée par un client, contenant plusieurs lignes."""
    def __init__(self, client):
        # Composition : l'attribut client est une instance de la classe Client
        self.client = client
        self.lignes = [] # Composition : l'attribut lignes est une liste de LigneCommande

    def ajouter_ligne(self, ligne):
        """Ajoute une instance de LigneCommande à la liste."""
        self.lignes.append(ligne)

    def total(self):
        """Calcule le montant total de la commande en sommant les totaux des lignes."""
        montant_total = 0
        for ligne in self.lignes:
            montant_total += ligne.total_ligne()
        return montant_total
    
    def afficher_recap(self):
        """Affiche un récapitulatif complet de la commande."""
        print("=" * 40)
        print("RÉCAPITULATIF DE COMMANDE")
        print("=" * 40)
        print(f"Client : {self.client}")
        print("\nDétails des lignes :")
        
        for ligne in self.lignes:
            # Utilise la méthode __str__ de LigneCommande
            print(f"  - {ligne}") 
            
        print("\n" + "=" * 40)
        print(f"TOTAL COMMANDE : {self.total():.2f}€")
        print("=" * 40)


# Bloc principal pour les tests
if __name__ == "__main__":
    # 1. Créer un client
    client_a = Client("Sophie Dubois", "sophie.dubois@mail.com")

    # 2. Créer des lignes de commande
    lc1 = LigneCommande("Support Technique (10h)", 1, 450.00)
    lc2 = LigneCommande("Licence Logiciel Pro", 2, 199.99)
    lc3 = LigneCommande("Formation POO (2 jours)", 1, 950.00)

    # 3. Créer la commande associée au client
    commande_c1 = Commande(client_a)

    # 4. Ajouter les lignes à la commande
    commande_c1.ajouter_ligne(lc1)
    commande_c1.ajouter_ligne(lc2)
    commande_c1.ajouter_ligne(lc3)

    # 5. Afficher le récapitulatif
    commande_c1.afficher_recap()