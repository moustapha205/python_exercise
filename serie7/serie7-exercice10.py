# Fichier : exercice_10_dashboard_viz.py

import matplotlib.pyplot as plt
import csv
import numpy as np
from datetime import datetime

# --- FONCTION UTILITAIRE (Moyenne Mobile) ---
def calculer_totaux_semaines(revenus, taille_semaine=7):
    totaux_semaines = []
    labels_semaines = []
    for i in range(0, len(revenus), taille_semaine):
        bloc = revenus[i:i+taille_semaine]
        if len(bloc) > 0:
            totaux_semaines.append(sum(bloc))
            labels_semaines.append(f"S{i//taille_semaine + 1}")
    return labels_semaines, totaux_semaines

# --- LECTURE DES DONNÉES ---
dates = []
trafic = []
nb_commandes = []
revenus = []
try:
    with open("ventes_journalieres.csv", "r", encoding="utf-8") as f:
        lecteur = csv.reader(f)
        next(lecteur)
        for ligne in lecteur:
            if len(ligne) >= 4:
                dates.append(ligne[0])
                trafic.append(int(ligne[1]))
                nb_commandes.append(int(ligne[2]))
                revenus.append(float(ligne[3]))
except FileNotFoundError:
    print("Erreur : Le fichier 'ventes_journalieres.csv' est introuvable. Nécessite 28 jours de données.")
    exit()


# --- CRÉATION DU TABLEAU DE BORD (2x2 Subplots) ---
plt.figure(figsize=(14, 10)) # Grande figure

# -----------------
# (1,1) : Courbe du Trafic
# -----------------
plt.subplot(2, 2, 1)
plt.plot(dates, trafic, color='blue', marker='.')
plt.title("Trafic Quotidien (Visites)")
plt.ylabel("Visites")
# Afficher seulement quelques dates pour ne pas surcharger l'axe
plt.xticks(dates[::5], rotation=45, ha='right')
plt.grid(axis='y', linestyle='--')

# -----------------
# (1,2) : Courbe du Revenu
# -----------------
plt.subplot(2, 2, 2)
plt.plot(dates, revenus, color='green', marker='.')
plt.title("Revenu Quotidien (€)")
plt.ylabel("Revenu (€)")
plt.xticks(dates[::5], rotation=45, ha='right')
plt.grid(axis='y', linestyle='--')

# -----------------
# (2,1) : Histogramme des Revenus
# -----------------
plt.subplot(2, 2, 3)
plt.hist(revenus, bins=7, edgecolor='black', color='dodgerblue')
plt.title("Distribution des Revenus")
plt.xlabel("Tranche de Revenu (€)")
plt.ylabel("Fréquence (Jours)")
plt.grid(axis='y', linestyle='--')

# -----------------
# (2,2) : Barres du CA Hebdomadaire (Réutilise Ex. 7)
# -----------------
labels_semaines, totaux_semaines = calculer_totaux_semaines(revenus)
plt.subplot(2, 2, 4)
plt.bar(labels_semaines, totaux_semaines, color='darkorange')
plt.title("CA Total par Semaine")
plt.xlabel("Semaine")
plt.ylabel("CA (€)")
plt.grid(axis='y', linestyle='--')

# Titre global et ajustements
plt.suptitle("Tableau de bord e-commerce : Performances Clés", fontsize=16, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.96]) # Ajuster pour laisser de la place au suptitle

# Bonus : Sauvegarder la figure
plt.savefig("dashboard.png")
print("\n✅ Tableau de bord sauvegardé sous 'dashboard.png'")

plt.show()
#