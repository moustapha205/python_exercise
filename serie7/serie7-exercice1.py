# Fichier : exercice_1_courbe.py

import matplotlib.pyplot as plt

# 1. Données
jours = [1, 2, 3, 4, 5, 6, 7]
trafic = [1200, 1350, 900, 1500, 1700, 1600, 1800]

# --- Figure 1 : Courbe de base ---
plt.figure(figsize=(7, 5))
plt.plot(jours, trafic, marker="o", color="blue", linestyle="-")

# Ajout des éléments de lisibilité
plt.title("Trafic du site sur 7 jours (avec marqueurs ronds)")
plt.xlabel("Jour")
plt.ylabel("Nombre de visites")
plt.grid(True)
plt.show()

# --- Figure 2 : Bonus (comparaison de marqueurs) ---
plt.figure(figsize=(7, 5))
plt.plot(jours, trafic, marker="s", color="red", linestyle="--") # 's' pour carré
plt.title("Trafic du site sur 7 jours (avec marqueurs carrés)")
plt.xlabel("Jour")
plt.ylabel("Nombre de visites")
plt.grid(True)
plt.show()
#