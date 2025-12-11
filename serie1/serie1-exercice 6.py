
def est_pair(n):
    return n % 2 == 0


def calculer_tva(prix_ht, taux):
    return prix_ht * (1 + taux / 100)


def moyenne(liste_nombres):
    if len(liste_nombres) == 0:
        return 0  
    return sum(liste_nombres) / len(liste_nombres)

if __name__ == "__main__":
    
    print("Test est_pair :")
    for i in range(1, 6):
        print(f"{i} est pair ? {est_pair(i)}")
    
    print("Test calculer_tva :")
    prix_ht_list = [100, 50, 23.5]
    taux_tva = 20  
    for prix_ht in prix_ht_list:
        print(f"Prix HT {prix_ht}€, prix TTC : {calculer_tva(prix_ht, taux_tva)}€")
    
    print("Test moyenne :")
    listes = [
        [10, 20, 30],
        [5, 7, 9, 11],
        []
    ]
    for l in listes:
        print(f"Moyenne de {l} : {moyenne(l)}")
