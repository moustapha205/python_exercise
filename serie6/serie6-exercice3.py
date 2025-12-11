class Produit:
    """
    Modélise un produit avec son nom, son prix HT et son stock.
    """
    def __init__(self, nom, prix_ht, stock):
        """Constructeur du produit."""
        self.nom = nom
        self.prix_ht = prix_ht
        self.stock = stock

    def prix_ttc(self, taux_tva):
        """Calcule et retourne le prix TTC."""
        return self.prix_ht * (1 + taux_tva)

    def valeur_stock_ttc(self, taux_tva):
        """Calcule et retourne la valeur totale TTC du stock."""
        return self.prix_ttc(taux_tva) * self.stock
    
    def afficher(self, taux_tva):
        """Affiche les informations détaillées du produit."""
        # Arrondir à 2 décimales pour l'affichage monétaire
        pttc = round(self.prix_ttc(taux_tva), 2)
        vsttc = round(self.valeur_stock_ttc(taux_tva), 2)
        
        print(f"| {self.nom:15} | {self.prix_ht:8.2f}€ | {pttc:8.2f}€ | {self.stock:5} | {vsttc:10.2f}€ |")


# Bloc principal pour les tests
if __name__ == "__main__":
    TAUX_TVA_STANDARD = 0.20 # 20%

    # Création des instances de produits
    p1 = Produit("Clavier Mécanique", 85.00, 15)
    p2 = Produit("Souris Sans Fil", 29.99, 50)
    p3 = Produit("Moniteur 27 pouces", 249.50, 8)

    # Stockage dans une liste
    catalogue = [p1, p2, p3]

    print(f"--- Catalogue de Produits (TVA: {TAUX_TVA_STANDARD * 100}%) ---")
    print(f"| {'Nom':15} | {'Prix HT':8} | {'Prix TTC':8} | {'Stock':5} | {'Val Stock TTC':12} |")
    print("|" + "-"*15 + "|" + "-"*8 + "€|" + "-"*8 + "€|" + "-"*5 + "|" + "-"*10 + "€|")

    somme_valeurs_stock_ttc = 0

    for produit in catalogue:
        produit.afficher(TAUX_TVA_STANDARD)
        somme_valeurs_stock_ttc += produit.valeur_stock_ttc(TAUX_TVA_STANDARD)

    # Affichage du total
    print("-" * 59)
    print(f"Valeur Totale du Stock (TTC) : {somme_valeurs_stock_ttc:10.2f}€")