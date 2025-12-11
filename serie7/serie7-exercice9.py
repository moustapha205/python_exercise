# Fichier : exercice_9_moyenne_mobile.py

import matplotlib.pyplot as plt
import csv
import numpy as np # Pour la fonction de moyenne mobile simple

# Lecture des revenus (basée sur le CSV de 28 jours)
dates = []
revenus = []
try:
    with open("ventes_journalieres.csv", "r", encoding="utf-8") as f:
        lecteur = csv.reader(f)
        next(lecteur)
        for ligne in lecteur:
            if len(ligne) >= 4:
                dates.append(ligne[0])
                revenus.append(float(ligne[3]))
except FileNotFoundError:
    print(" Erreur : Le fichier 'ventes_journalieres.csv' est introuvable.")
    exit()

# 1. Fonction de moyenne mobile (MM)
def calculer_moyenne_mobile(liste_valeurs, fenetre):
    resultat = []
    # Créer un tableau NumPy à partir de la liste de revenus
    np_revenus = np.array(liste_valeurs)
    
    # Calculer la moyenne mobile en utilisant une convolution (plus efficace)
    # Remplacer les premières valeurs par NaN (ou None) car il n'y a pas assez de données précédentes
    mm = np.convolve(np_revenus, np.ones(fenetre)/fenetre, mode='full')[:len(np_revenus)]
    
    # Remplacer les points initiaux non valides par None pour ne pas les tracer
    resultat = [None] * (fenetre - 1) + mm[fenetre - 1:].tolist()
    
    return resultat

# Calcul de la Moyenne Mobile sur 3 jours
mm_3jours = calculer_moyenne_mobile(revenus, fenetre=3)

# 2. Tracer les deux courbes
plt.figure(figsize=(12, 6))

# Courbe 1 : Revenus bruts (fortes variations)
plt.plot(dates, revenus, marker="o", linestyle="-", color="lightgray", label="Revenu Brut Quotidien")

# Courbe 2 : Moyenne Mobile (lisse les variations)
# On utilise la liste de dates pour les X, mais la liste de MM (avec des None au début) pour les Y
plt.plot(dates, mm_3jours, marker="None", linestyle="--", color="red", linewidth=2, label="Moyenne Mobile (3 jours)")

# Ajout des éléments de lisibilité
plt.title("Revenu Quotidien vs Moyenne Mobile (Lissage des tendances)")
plt.xlabel("Date")
plt.ylabel("Revenu (€)")
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
#