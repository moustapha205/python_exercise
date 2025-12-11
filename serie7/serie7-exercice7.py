# Fichier : exercice_7_barres_periodes.py

import matplotlib.pyplot as plt
import csv

# Lecture des revenus (basée sur le CSV de 28 jours ci-dessus)
revenus = []
try:
    with open("ventes_journalieres.csv", "r", encoding="utf-8") as f:
        lecteur = csv.reader(f)
        next(lecteur)
        for ligne in lecteur:
            if len(ligne) >= 4:
                revenus.append(float(ligne[3]))
except FileNotFoundError:
    print("❌ Erreur : Le fichier 'ventes_journalieres.csv' est introuvable. Veuillez le créer avec au moins 28 lignes de données.")
    exit()

# 1. Calcul du total de revenu par semaine
totaux_semaines = []
taille_semaine = 7
labels_semaines = []

for i in range(0, len(revenus), taille_semaine):
    bloc = revenus[i:i+taille_semaine]
    
    # S'assurer d'avoir une semaine complète ou l'appeler "Semaine X (partielle)"
    if len(bloc) == taille_semaine:
        totaux_semaines.append(sum(bloc))
        labels_semaines.append(f"S{i//taille_semaine + 1}")
    elif len(bloc) > 0:
        # Gérer la dernière semaine incomplète si nécessaire, ici on l'ignore pour l'exercice 7
        pass 

# 2. Tracer le diagramme en barres
plt.figure(figsize=(8, 6))

plt.bar(labels_semaines, totaux_semaines, color='darkorange')

# Ajout des éléments de lisibilité
plt.title("Chiffre d'affaires Total par Semaine")
plt.xlabel("Semaine")
plt.ylabel("CA Total (€)")
plt.grid(axis='y', linestyle='--')

# Bonus : Afficher la valeur sur les barres (comme Ex. 2)
for i, total in enumerate(totaux_semaines):
    plt.text(labels_semaines[i], total + 500, f'{total:,.0f}€', ha='center', va='bottom', fontsize=10)

plt.ylim(0, max(totaux_semaines) * 1.1)
plt.show()
#