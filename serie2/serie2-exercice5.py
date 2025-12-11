notes = []


with open("/Users/mac/Desktop/python/serie2/notes.txt", "r") as f:
    for ligne in f:
        ligne = ligne.strip()
        if ligne:  # ignorer lignes vides
            notes.append(float(ligne))


note_min = min(notes)
note_max = max(notes)
moyenne = sum(notes) / len(notes)
reussites = sum(1 for n in notes if n >= 10)


print("=== STATISTIQUES DES NOTES ===")
print("Notes :", notes)
print("Note minimale :", note_min)
print("Note maximale :", note_max)
print("Moyenne :", round(moyenne, 2))     
print("Nombre de notes >= 10 :", reussites)
