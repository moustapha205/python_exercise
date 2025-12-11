# Fichier : exercice_3_scatter.py

import matplotlib.pyplot as plt
import random

# 1. Données (8 à 10 jours)
# Génération de données avec une légère corrélation
random.seed(42) # Pour rendre les résultats reproductibles
jours = list(range(1, 11))
trafic = [random.randint(800, 1800) for _ in jours]
# Le revenu est basé sur le trafic + un peu d'aléatoire pour la dispersion
revenu = [(t * 3) + random.randint(-500, 500) for t in trafic]

# --- Tracer le nuage de points ---
plt.figure(figsize=(8, 6))

# Bonus : alpha=0.7 pour la transparence
plt.scatter(trafic, revenu, color='teal', marker='o', alpha=0.7, s=100) # s=taille des points

# Ajout des éléments de lisibilité
plt.title("Nuage de points : Relation entre Trafic (Visites) et Revenu (€)")
plt.xlabel("Trafic (visites)")
plt.ylabel("Revenu (€)")
plt.grid(True)
plt.show()
#