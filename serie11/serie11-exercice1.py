# score = 0

# def ajouter_points(points):
#     print("Score avant :", score)
#     score = score + points
#     print("Score après :", score)

# ajouter_points(10)
# # td11_ex1_corrigé.py

score = 0 # Variable globale initiale

def ajouter_points(score_actuel, points):
    """
    Calcule le nouveau score en ajoutant des points au score actuel.
    Retourne le nouveau score sans modifier de variable globale.
    """
    nouveau_score = score_actuel + points
    return nouveau_score

# Bloc principal : Mise à jour de la variable globale 'score'
print(f"Score initial : {score}")  # Score initial : 0

# Ajout 1
points_a_ajouter = 10
score = ajouter_points(score, points_a_ajouter) # On réassigne le retour à la variable globale
print(f"Score après ajout de {points_a_ajouter} points : {score}") # Score après ajout de 10 points : 10

# Ajout 2
points_a_ajouter = 5
score = ajouter_points(score, points_a_ajouter)
print(f"Score après ajout de {points_a_ajouter} points : {score}") # Score après ajout de 5 points : 15

print(f"Score final : {score}")  # Score final : 15