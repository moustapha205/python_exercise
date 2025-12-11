# td13_ex4.py
from dataclasses import dataclass
import datetime

# Classe initiale (Version 1) :
# class Client:
#     def __init__(self, nom, email, actif=True):
#         self.nom = nom
#         self.email = email
#         self.actif = actif
#     def __repr__(self):
#         return f"Client(nom={self.nom!r}, email={self.email!r}, actif={self.actif!r})"



# VERSION REFACTORISÉE (Dataclass)


@dataclass
class Client:
    """
    Classe Client refactorisée en dataclass.
    __init__ et __repr__ sont générés automatiquement.
    """
    # Déclaration des champs avec annotations de type
    nom: str
    email: str
    actif: bool = True  # Valeur par défaut
    
    # Ajout d'une méthode d'instance (méthode métier)
    def desactiver(self):
        """Passe l'attribut actif à False."""
        self.actif = False
        print(f"⚠️ {self.nom.title()} a été désactivé.")
        
    def afficher_statut(self):
        return "Actif" if self.actif else "Inactif"


# --- Bloc principal ---
if __name__ == "__main__":
    
    # Création des instances (dataclass utilise l'__init__ généré)
    c1 = Client("Émile Dupont", "emile@mail.com")
    c2 = Client(nom="Sophie Martin", email="sophie@mail.com", actif=False)

    print("--- Affichage des Clients (via __repr__ automatique) ---")
    print(c1)
    print(c2)
    
    print("\n--- Utilisation de la méthode métier ---")
    print(f"Statut de Émile avant : {c1.afficher_statut()}")
    c1.desactiver()
    print(f"Statut de Émile après : {c1.afficher_statut()}")


# COMMENTAIRE sur l'économie de code :
"""
Les dataclasses nous ont évité d'écrire à la main :
1. Le constructeur (__init__): Toutes les lignes self.nom = nom, self.email = email, etc., 
   ont été générées automatiquement à partir des annotations de type.
2. La représentation textuelle de l'objet (__repr__): La méthode qui affiche l'objet 
   proprement (Client(nom='...', email='...', ...)) est générée.
3. Les méthodes de comparaison (par exemple __eq__): Non utilisées ici, mais elles 
   sont également générées par défaut, permettant de comparer directement deux 
   instances de Client.
"""