entier = int(input("donnez moi un entier : "))

for i in range(1, 11):
    print("la table de multiplication de n est :", entier * i)
somme =0
i=1
while i <= entier:
    Somme=somme+i
    i+=1
print("La somme des entiers de 1 à", entier, "est :", Somme)