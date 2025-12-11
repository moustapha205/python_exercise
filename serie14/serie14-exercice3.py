# td14_ex3.py
from dataclasses import dataclass

@dataclass
class Produit:
    """
    Produit enrichi de méthodes statiques pour validation et formatage.
    """
    nom: str
    prix_ht: float
    taux_tva: float = 0.2

    # --- Méthodes Statiques ---

    @staticmethod
    def est_prix_valide(prix: float) -> bool:
        """Renvoie True si le prix est non-négatif."""
        return prix >= 0

    @staticmethod
    def format_euro(montant: float) -> str:
        """Formate un montant en chaîne de caractères avec 2 décimales et '€'."""
        return f"{montant:,.2f} €"

    # --- Méthodes d'Instance ---

    def __post_init__(self):
        """
        Normalisation et validation utilisant la méthode statique.
        """
        self.nom = self.nom.strip()

        # Utilisation de la méthode statique pour la validation
        if not Produit.est_prix_valide(self.prix_ht):
            raise ValueError(f"Le prix HT du produit '{self.nom}' doit être positif.")

        if not (0 <= self.taux_tva <= 1):
            raise ValueError(f"Le taux de TVA (valeur: {self.taux_tva}) doit être entre 0 et 1.")

    def prix_ttc(self) -> float:
        """Calcule et renvoie le prix TTC du produit."""
        return self.prix_ht * (1 + self.taux_tva)

    def __str__(self) -> str:
        """
        Redéfinit l'affichage lisible en utilisant la méthode statique pour le formatage.
        """
        prix_ht_str = Produit.format_euro(self.prix_ht)
        prix_ttc_str = Produit.format_euro(self.prix_ttc())
        tva_pourcentage = f"{self.taux_tva * 100:.0f}%"
        
        return f"Produit {self.nom} – {prix_ht_str} HT ({tva_pourcentage} TVA) – {prix_ttc_str} TTC"

# --- Bloc principal ---
if __name__ == "__main__":
    
    # Test direct des méthodes statiques
    print("--- Test des méthodes statiques ---")
    print(f"Validation d'un prix : {Produit.est_prix_valide(15.5)}")
    print(f"Formatage d'un montant : {Produit.format_euro(1234.5678)}") # Affiche 1 234,57 €
    
    # Création et affichage des produits (vérification du formatage dans __str__)
    p1 = Produit(" Bureau ", 499.99, 0.2)
    p2 = Produit("Licence Logiciel", 99.0, 0.055)

    print("\n--- Affichage des Produits formatés ---")
    print(p1)
    print(p2)
    
    # Vérification que la validation via méthode statique fonctionne toujours
    try:
        Produit("Erreur", -10, 0.2) 
    except ValueError as e:
        print(f"\n ERREUR interceptée : {e}")