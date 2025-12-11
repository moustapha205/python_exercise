# td11_ex3.py

# Utilisation d'un dictionnaire centralisé pour l'état (les scores)
# Les fonctions prendront l'état en paramètre et le retourneront si modification.

def ajouter_points(scores, nom_joueur, points):
    """
    Ajoute des points à un joueur spécifié dans le dictionnaire des scores.
    Retourne le dictionnaire des scores mis à jour.
    """
    if nom_joueur in scores:
        scores[nom_joueur] += points
    else:
        # Gestion simple si le joueur n'existe pas encore
        scores[nom_joueur] = points
        
    return scores # Renvoyer le dictionnaire mis à jour

def afficher_scores(scores):
    """Affiche tous les scores contenus dans le dictionnaire."""
    print("--- Scores Actuels ---")
    for joueur, score in scores.items():
        # Utilisation de .title() pour formater le nom
        print(f"{joueur.title()} : {score}")
    print("----------------------")


# --- Bloc Principal : Gestion de l'état ---

# 1. Initialisation de l'état (le dictionnaire)
scores = {
    "joueur1": 0,
    "joueur2": 0,
}

print("--- Début du jeu ---")
afficher_scores(scores) # Joueur 1 : 0, Joueur 2 : 0

# Scénario de jeu (l'état est mis à jour par réassignation dans le bloc principal)
print("\n--- Scénario : J1(+10), J2(+5), J1(+7) ---")

scores = ajouter_points(scores, "joueur1", 10)
scores = ajouter_points(scores, "joueur2", 5)
scores = ajouter_points(scores, "joueur1", 7)

# Affichage final
afficher_scores(scores) # Joueur 1 : 17, Joueur 2 : 5


# --- Explication pour l'évolutivité (dans un commentaire) ---

"""""
Explication sur l'évolutivité (Ajout d'un Joueur 3) :
Avec le design basé sur le dictionnaire, l'ajout d'un troisième joueur (ex: "joueur3") 
est extrêmement simple. Il ne nécessite AUCUNE modification des fonctions 'ajouter_points' 
ou 'afficher_scores'.

Il suffit d'agir sur le dictionnaire :
1. Initialisation : scores["joueur3"] = 0 (ou modification de l'initialisation de base).
2. Ajout de points : scores = ajouter_points(scores, "joueur3", 15).

Les fonctions sont génériques et agissent sur n'importe quelle clé du dictionnaire, 
ce qui rend le code beaucoup plus évolutif et "scalable" par rapport à l'approche 'global' 
où il fallait créer une nouvelle fonction par joueur.
"""

# Démonstration de l'évolutivité (sans modifier les fonctions !)
scores = ajouter_points(scores, "joueur3", 15)
scores = ajouter_points(scores, "joueur1", 3)
print("\n--- Scores après l'ajout d'un 3e joueur ---")
afficher_scores(scores)