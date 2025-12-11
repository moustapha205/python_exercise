
notes = [12, 5.5, 17, 9, 13, 8, 10]


note_min = min(notes)
print("Note minimale :", note_min)

note_max = max(notes)
print("Note maximale :", note_max)


moyenne = sum(notes) / len(notes)
print("Moyenne de la classe :", moyenne)


reussites = sum(1 for n in notes if n >= 10)
print("Nombre de réussites :", reussites)


pourcentage = (reussites / len(notes)) * 100
print(f"Pourcentage de réussite : {pourcentage:}%")
