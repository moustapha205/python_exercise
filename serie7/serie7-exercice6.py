# Fichier : exercice_6_subplots.py

import matplotlib.pyplot as plt
import csv

# Lecture du fichier (identique à l'Exercice 5)
dates = []
trafic = []
revenus = []
try:
    with open("ventes_journalieres.csv", "r", encoding="utf-8") as f:
        lecteur = csv.reader(f)
        next(lecteur)
        for ligne in lecteur:
            if len(ligne) >= 4:
                dates.append(ligne[0])
                trafic.append(int(ligne[1]))
                revenus.append(float(ligne[3]))
except FileNotFoundError:
    print("❌ Erreur : Le fichier 'ventes_journalieres.csv' est introuvable. Veuillez le créer.")
    exit()


# --- Création des Subplots (2 lignes, 1 colonne) ---
plt.figure(figsize=(12, 8)) # Figure plus grande pour plus de clarté

# 1er subplot (Haut) : Courbe du Trafic
plt.subplot(2, 1, 1)
plt.plot(dates, trafic, marker="o", color="blue")
plt.title("Trafic Quotidien")
plt.ylabel("Visites")
plt.xticks(rotation=45, ha='right')
plt.grid(True, axis='y', linestyle='--')

# 2e subplot (Bas) : Courbe du Revenu
plt.subplot(2, 1, 2)
plt.plot(dates, revenus, marker="o", color="green")
plt.title("Revenu Quotidien")
plt.xlabel("Date")
plt.ylabel("Revenu (€)")
plt.xticks(rotation=45, ha='right')
plt.grid(True, axis='y', linestyle='--')

plt.tight_layout() # Assurer que les titres et labels ne se chevauchent pas
plt.show()
#