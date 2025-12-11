# td14_ex1.py
from dataclasses import dataclass

@dataclass
class Produit:
    """
    Représente un produit avec validation des prix/TVA via __post_init__.
    """
    nom: str
    prix_ht: float
    taux_tva: float = 0.2  # Valeur par défaut

    def __post_init__(self):
        """
        Appelé après l'__init__ généré. Utilisé pour normaliser et valider les données.
        """
        # 1. Normalisation : supprimer les espaces avant/après le nom
        self.nom = self.nom.strip()

        # 2. Validation : prix_ht positif
        if self.prix_ht < 0:
            raise ValueError(f"Le prix HT du produit '{self.nom}' doit être positif.")

        # 3. Validation : taux_tva entre 0 et 1 (0% à 100%)
        if not (0 <= self.taux_tva <= 1):
            raise ValueError(f"Le taux de TVA (valeur: {self.taux_tva}) doit être entre 0 et 1.")

    def prix_ttc(self) -> float:
        """Calcule et renvoie le prix TTC du produit."""
        return self.prix_ht * (1 + self.taux_tva)

    def __str__(self) -> str:
        """
        Redéfinit l'affichage lisible de l'objet pour print(produit).
        """
        prix_ht_formate = f"{self.prix_ht:.2f}"
        prix_ttc_formate = f"{self.prix_ttc():.2f}"
        tva_pourcentage = f"{self.taux_tva * 100:.0f}%"
        
        return f"Produit {self.nom} – {prix_ht_formate} € HT ({tva_pourcentage} TVA) – {prix_ttc_formate} € TTC"

# --- Bloc principal ---
if __name__ == "__main__":
    
    # 1. Cas valides
    p1 = Produit(" Clavier Mécanique ", 120.0, 0.2)
    p2 = Produit("Souris", 35.50) # Utilise le taux de TVA par défaut (0.2)
    p3 = Produit("Service Conseil", 500.0, 0.055) # Taux réduit (5.5%)

    print("--- Affichage des Produits Valides ---")
    print(p1) # Vérification de .strip() dans __post_init__
    print(p2)
    print(p3)

    # 2. Test des cas invalides (validation dans __post_init__)
    print("\n--- Tests des cas invalides ---")
    
    try:
        # Prix négatif
        Produit("Moniteur", -200.0) 
    except ValueError as e:
        print(f" ERREUR interceptée : {e}")

    try:
        # Taux de TVA invalide
        Produit("Logiciel", 100.0, 1.5) 
    except ValueError as e:
        print(f" ERREUR interceptée : {e}")