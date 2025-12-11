
prix = [9.99, 14.5, 3.2, 29.0]


print("Liste des prix :")
for p in prix:
    print(p)


total = 0
for p in prix:
    total += p

print("Total des prix :", total)


moyenne = total / len(prix)
print("Prix moyen :", moyenne)


for p in prix:
    if p > 10:
        print("Prix > 10€ :",p)
