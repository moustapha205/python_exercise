# td11_ex4.py

class ScoreBoard:
    """
    Gère l'état des scores pour plusieurs joueurs à l'aide d'un attribut d'instance (self.scores).
    """
    def __init__(self):
        """Initialise le tableau des scores comme un dictionnaire vide."""
        # self.scores est un attribut d'instance qui stocke l'état interne de l'objet
        self.scores = {}

    def ajouter_points(self, nom_joueur, points):
        """
        Ajoute des points à un joueur. Crée le joueur s'il n'existe pas.
        """
        # Utilisation de la méthode .get() du dictionnaire pour gérer les joueurs qui n'existent pas
        # scores.get(nom_joueur, 0) retourne le score actuel, ou 0 si le joueur est nouveau.
        score_actuel = self.scores.get(nom_joueur, 0)
        self.scores[nom_joueur] = score_actuel + points
        print(f"-> {nom_joueur.title()} gagne {points} points.")

    def afficher(self):
        """
        Affiche tous les joueurs et leurs scores actuels.
        """
        print("\n=== CLASSEMENT ACTUEL ===")
        
        # Pour une meilleure lisibilité, nous allons trier les scores par valeur
        # Tri basé sur le score (la valeur du dictionnaire)
        scores_tries = sorted(
            self.scores.items(), 
            key=lambda item: item[1], 
            reverse=True
        )

        for nom, score in scores_tries:
            print(f"| {nom.title():10} : {score:4} points |")
        print("=========================")


# --- Bloc Principal : Scénario de test ---
if __name__ == "__main__":
    
    # 1. Création de l'objet ScoreBoard
    jeu_de_cartes = ScoreBoard()
    print("Tableau de bord de scores créé.")

    # 2. Scénario de jeu
    jeu_de_cartes.ajouter_points("joueur1", 10)
    jeu_de_cartes.ajouter_points("joueur2", 5)
    jeu_de_cartes.ajouter_points("joueur1", 7) # Joueur 1 passe à 17

    # 3. Ajout d'un troisième joueur ("invité")
    jeu_de_cartes.ajouter_points("invité", 20)
    jeu_de_cartes.ajouter_points("joueur2", 3) # Joueur 2 passe à 8

    # 4. Affichage des scores
    jeu_de_cartes.afficher()