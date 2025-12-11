# Fichier : exercice_8_boxplot.py
import matplotlib.pyplot as plt
import csv

# Lecture des revenus (basée sur le CSV de 28 jours)
revenus = []
try:
    with open("ventes_journalieres.csv", "r", encoding="utf-8") as f:
        lecteur = csv.reader(f)
        next(lecteur)
        for ligne in lecteur:
            if len(ligne) >= 4:
                revenus.append(float(ligne[3]))
except FileNotFoundError:
    print(" Erreur : Le fichier 'ventes_journalieres.csv' est introuvable.")
    exit()

# --- Boxplot simple des revenus journaliers ---
plt.figure(figsize=(6, 8))

plt.boxplot(revenus, patch_artist=True, boxprops=dict(facecolor='lightblue'))

# Ajout des éléments de lisibilité
plt.title("Boxplot de la Distribution des Revenus Journaliers")
plt.ylabel("Revenu (€)")
plt.xticks([1], ['Tous les jours']) # Label personnalisé pour l'axe X
plt.grid(axis='y', linestyle='--')
plt.show()

# --- Bonus : Comparaison de 2 périodes ---
# Séparation des données en deux blocs (Semaines 1-2 et Semaines 3-4)
semaines_1_2 = revenus[:14]
semaines_3_4 = revenus[14:28]

if len(semaines_3_4) > 0:
    plt.figure(figsize=(8, 8))
    
    # Tracer 2 boxplots côte à côte
    data_a_comparer = [semaines_1_2, semaines_3_4]
    labels_comparaison = ["Semaines 1-2", "Semaines 3-4"]
    
    plt.boxplot(data_a_comparer, labels=labels_comparaison, patch_artist=True, 
                boxprops=dict(facecolor='lightgreen'), 
                medianprops=dict(color='red'))
    
    plt.title("Comparaison de la Variabilité du Revenu (Périodes)")
    plt.ylabel("Revenu (€)")
    plt.grid(axis='y', linestyle='--')
    plt.show()
    #