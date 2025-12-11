# Fichier : exercice_4_histogramme.py

import matplotlib.pyplot as plt
import random

# 1. Données (25 jours de revenus journaliers)
random.seed(42) 
revenus = [random.randint(1500, 3500) for _ in range(15)] + \
          [random.randint(3500, 5500) for _ in range(10)]
random.shuffle(revenus) # Mélanger les données

# --- Tracer l'histogramme ---
plt.figure(figsize=(8, 6))

# Nombre de bacs (bins) adapté : 7
bins = 7 
plt.hist(revenus, bins=bins, edgecolor='black', color='dodgerblue')

# Ajout des éléments de lisibilité
plt.title(f"Distribution des revenus journaliers (Bins = {bins})")
plt.xlabel("Revenu (€)")
plt.ylabel("Fréquence (Nombre de jours)")
plt.grid(axis='y', linestyle='--')
plt.show()

# Lecture : L'histogramme montrera probablement une concentration de jours
# dans la tranche faible (1500-3500) et une autre dans la tranche moyenne-forte (3500-5500).
#