

# Fonctions sans effet de bord : elles sont pures, car elles ne font que calculer et retourner.

def ajouter_bonus(score):
    """Retourne le score après l'ajout du bonus (+5)."""
    return score + 5

def ajouter_malus(score):
    """Retourne le score après l'ajout du malus (-3)."""
    return score - 3

# --- Bloc principal (Gestion de l'état) ---

score = 0 # Variable d'état initiale
print(f"Score initial : {score}") # 0

# Scénario de test : l'état est mis à jour par réassignation (score = fonction(score))

# 1. Ajouter bonus
score = ajouter_bonus(score)
print(f"Score après bonus 1 : {score}") # 5

# 2. Ajouter bonus
score = ajouter_bonus(score)
print(f"Score après bonus 2 : {score}") # 10

# 3. Ajouter malus
score = ajouter_malus(score)
print(f"Score après malus : {score}")  # 7

print("-" * 30)
print(f"Score final : {score}")        # 7