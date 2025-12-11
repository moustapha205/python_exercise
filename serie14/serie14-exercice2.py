# td14_ex2.py
from dataclasses import dataclass, field
# Importe Produit depuis l'exercice 1 (ou le recopier ici pour l'exécution directe)
from td14_ex1 import Produit 

@dataclass
class LigneFacture:
    """
    Représente une ligne de facture, total_ht et total_ttc sont calculés
    automatiquement dans __post_init__.
    """
    produit: Produit
    quantite: int
    
    # Champs dérivés, non passés au constructeur
    total_ht: float = field(init=False)
    total_ttc: float = field(init=False)

    def __post_init__(self):
        """
        Vérifie la quantité et calcule les totaux.
        """
        # 1. Validation : quantité positive
        if self.quantite <= 0:
            raise ValueError(f"La quantité doit être strictement positive (reçue: {self.quantite}).")
            
        # 2. Calcul des champs dérivés
        self.total_ht = self.quantite * self.produit.prix_ht
        self.total_ttc = self.quantite * self.produit.prix_ttc() # Utilise la méthode prix_ttc() du Produit

    def __str__(self) -> str:
        """
        Redéfinit l'affichage de la ligne de facture.
        """
        ht_formate = f"{self.total_ht:.2f}"
        ttc_formate = f"{self.total_ttc:.2f}"
        
        # Réutilise le __str__ du Produit, ou affiche juste son nom
        return (f"{self.quantite} x {self.produit.nom} (unité : {self.produit.prix_ht:.2f}€ HT) "
                f"– {ht_formate} € HT – {ttc_formate} € TTC")

# --- Bloc principal ---
if __name__ == "__main__":
    
    # Création des produits nécessaires (réutilise Produit de td14_ex1)
    p_clavier = Produit("Clavier Mécanique", 120.0, 0.2)
    p_souris = Produit("Souris", 35.50)

    print("--- Affichage des Lignes de Facture Valides ---")
    
    # 1. Création des lignes valides
    l1 = LigneFacture(produit=p_clavier, quantite=2)
    l2 = LigneFacture(produit=p_souris, quantite=5)

    print(l1)
    print(l2)
    
    # Vérification des calculs
    print(f"\nVerification L1 HT: {l1.total_ht} (Attendu: 2 * 120.0 = 240.0)")
    print(f"Verification L1 TTC: {l1.total_ttc} (Attendu: 2 * 144.0 = 288.0)")
    
    # 2. Test d'un cas invalide
    print("\n--- Test d'une quantité invalide ---")
    try:
        LigneFacture(produit=p_souris, quantite=0) 
    except ValueError as e:
        print(f" ERREUR interceptée : {e}")