# td13_ex2.py

class StockProduit:
    """
    Gère le stock d'un produit avec encapsulation pour garantir
    que le stock reste cohérent (non négatif).
    """
    def __init__(self, nom, stock_initial=0):
        self.nom = nom
        # Attribut interne (convention : _ devant pour signaler de ne pas modifier directement)
        if stock_initial < 0:
             raise ValueError("Le stock initial ne peut pas être négatif.")
        self._stock = stock_initial

    def ajouter(self, qte):
        """Ajoute une quantité au stock, si qte > 0."""
        if qte <= 0:
            raise ValueError("La quantité à ajouter doit être positive.")
        self._stock += qte
        print(f" Ajout de {qte} unités. Nouveau stock : {self._stock}")

    def retirer(self, qte):
        """Retire une quantité du stock, avec vérification des règles métier."""
        if qte <= 0:
            raise ValueError("La quantité à retirer doit être positive.")
        
        if qte > self._stock:
            # Règle métier : ne pas retirer plus que ce qui est disponible
            raise ValueError(f"Stock insuffisant. Disponible : {self._stock}, Demande : {qte}")
            
        self._stock -= qte
        print(f" Retrait de {qte} unités. Nouveau stock : {self._stock}")

    def afficher_stock(self):
        """Affiche le nom du produit et le stock courant."""
        print(f"\nProduit : {self.nom} | Stock Courant : {self._stock}")


# --- Bloc principal ---
if __name__ == "__main__":
    
    clavier_stock = StockProduit("Clavier Mécanique", 10)
    clavier_stock.afficher_stock() # Stock Courant : 10

    # 1. Scénario valide
    clavier_stock.ajouter(5)
    clavier_stock.retirer(3)
    clavier_stock.afficher_stock() # Stock Courant : 12

    # 2. Scénario d'erreurs (utilisation de try/except)
    print("\n--- Tests des règles métier ---")
    try:
        clavier_stock.retirer(50) # Tente de retirer trop
    except ValueError as e:
        print(f" ERREUR interceptée (Retrait) : {e}")

    try:
        clavier_stock.ajouter(-2) # Tente d'ajouter une quantité négative
    except ValueError as e:
        print(f"ERREUR interceptée (Ajout) : {e}")

    # 3. Illustration du danger de la modification directe
    print("\n--- Danger de la modification directe ---")
    
    # COMMENTAIRE :
    # Il est dangereux de modifier directement _stock car cela contourne la 
    # validation métier de la méthode retirer().
    
    clavier_stock._stock = -100 
    
    # COMMENTAIRE :
    # Le code a permis un état illégal (stock négatif) sans lever d'exception.
    # Si on utilisait la méthode retirer(), cette opération aurait été bloquée.
    
    clavier_stock.afficher_stock() # Stock Courant : -100 (invalide)