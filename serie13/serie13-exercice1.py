# td13_ex1.py

class Produit:
    """
    Représente un produit avec un attribut de classe partagé (taux_tva).
    """
    # Attribut de CLASSE (partagé par toutes les instances)
    taux_tva = 0.2

    def __init__(self, nom, prix_ht):
        """Initialise les attributs d'instance."""
        if prix_ht < 0:
            raise ValueError("Le prix HT doit être positif.")
        
        # Attributs d'INSTANCE
        self.nom = nom
        self.prix_ht = prix_ht

    def prix_ttc(self):
        """Renvoie le prix TTC en utilisant l'attribut de classe partagé."""
        # On peut accéder à l'attribut de classe via self ou via Produit
        return self.prix_ht * (1 + Produit.taux_tva)

# --- Bloc principal ---
if __name__ == "__main__":
    
    # Création de deux produits
    p1 = Produit("Clavier", 80.0)
    p2 = Produit("Souris", 25.0)

    print("--- Avant modification du taux de TVA (20%) ---")
    print(f"Taux de TVA (Classe) : {Produit.taux_tva * 100:.0f}%")
    print(f"{p1.nom:10} | HT: {p1.prix_ht:.2f}€ | TTC: {p1.prix_ttc():.2f}€") # TTC: 96.00€
    print(f"{p2.nom:10} | HT: {p2.prix_ht:.2f}€ | TTC: {p2.prix_ttc():.2f}€") # TTC: 30.00€

    # ----------------------------------------------------
    # Modification de l'attribut de classe
    # ----------------------------------------------------
    Produit.taux_tva = 0.1 # Nouveau taux de 10%

    print("\n--- Après modification du taux de TVA (10%) ---")
    print(f"Nouveau Taux de TVA (Classe) : {Produit.taux_tva * 100:.0f}%")
    
    # Les mêmes instances p1 et p2 utilisent la nouvelle valeur de taux_tva
    print(f"{p1.nom:10} | HT: {p1.prix_ht:.2f}€ | TTC: {p1.prix_ttc():.2f}€") # TTC: 88.00€
    print(f"{p2.nom:10} | HT: {p2.prix_ht:.2f}€ | TTC: {p2.prix_ttc():.2f}€") # TTC: 27.50€

    # Conclusion : La modification de Produit.taux_tva affecte toutes 
    # les instances existantes et futures, car elles partagent le même attribut de classe.
    
    # Vérification des accès (Indice)
    print("\nVérification de l'accès à l'attribut :")
    print(f"Accès via l'instance p1.taux_tva : {p1.taux_tva}")
    print(f"Accès via la classe Produit.taux_tva : {Produit.taux_tva}")