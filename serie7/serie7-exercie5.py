# Fichier : exercice_5_csv_courbe.py

import matplotlib.pyplot as plt
import csv

# 1. Lecture du fichier CSV
dates = []
revenus = []
trafic = [] # Ajout pour le Bonus

try:
    with open("ventes_journalieres.csv", "r", encoding="utf-8") as f:
        lecteur = csv.reader(f)
        next(lecteur)  # Saute la ligne d'en-tête

        for ligne in lecteur:
            # S'assurer que le fichier CSV a les bonnes colonnes
            if len(ligne) >= 4:
                dates.append(ligne[0])
                # Conversion des données numériques
                trafic.append(int(ligne[1]))
                revenus.append(float(ligne[3]))
            
except FileNotFoundError:
    print("❌ Erreur : Le fichier 'ventes_journalieres.csv' est introuvable. Veuillez le créer.")
    exit()

# --- Tracer la courbe des revenus ---
plt.figure(figsize=(10, 6))

# Courbe des revenus
plt.plot(dates, revenus, marker="o", linestyle="-", color="green", label="Revenu Quotidien")

# Ajout des éléments de lisibilité
plt.title("Revenu Quotidien sur 15 jours")
plt.xlabel("Date")
plt.ylabel("Revenu (€)")
plt.xticks(rotation=45, ha='right') # Incliner les dates
plt.legend()
plt.grid(True, axis='y')
plt.tight_layout() # Ajuster les marges pour que tout tienne
plt.show()

# --- Bonus : Tracer le trafic sur un second axe (y2) ---
plt.figure(figsize=(10, 6))

# Axe 1 (Revenu)
ax1 = plt.gca() # Récupère l'axe courant
ax1.plot(dates, revenus, marker="o", color="green", label="Revenu (€)")
ax1.set_ylabel("Revenu (€)", color="green")
ax1.tick_params(axis='y', labelcolor="green")

# Axe 2 (Trafic) - Création d'un second axe partageant l'axe X
ax2 = ax1.twinx() 
ax2.plot(dates, trafic, marker="s", linestyle="--", color="blue", label="Trafic (Visites)")
ax2.set_ylabel("Trafic (Visites)", color="blue")
ax2.tick_params(axis='y', labelcolor="blue")

# Finalisation
plt.title("Revenu et Trafic Quotidien (Double Axe Y)")
plt.xticks(rotation=45, ha='right')
ax1.grid(True, axis='y', linestyle='--')
plt.tight_layout()
plt.show()
#