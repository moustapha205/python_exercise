# Fichier : exercice_2_barres.py

import matplotlib.pyplot as plt

# 1. Données
categories = ["Électronique", "Mode", "Maison", "Sport", "Livres"]
ca = [12000, 8000, 6000, 4000, 3500]

# --- Tracer le diagramme en barres ---
plt.figure(figsize=(9, 6))
bars = plt.bar(categories, ca, color=['skyblue', 'salmon', 'lightgreen', 'gold', 'violet'])

# Ajout des éléments de lisibilité
plt.title("Chiffre d'affaires par catégorie")
plt.xlabel("Catégorie")
plt.ylabel("CA (€)")
plt.grid(axis='y', linestyle='--') # Grille uniquement sur l'axe des ordonnées

# Bonus : Afficher la valeur au-dessus de chaque barre
for bar in bars:
    yval = bar.get_height()
    # Utilisation de f-string pour un formatage monétaire
    plt.text(bar.get_x() + bar.get_width()/2, yval + 100, f'{yval:,.0f}€', 
             ha='center', va='bottom', fontsize=10)

plt.ylim(0, max(ca) * 1.1) # Ajuster la limite Y pour laisser de la place au texte
plt.show()
#