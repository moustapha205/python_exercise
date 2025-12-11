prix_HT= float(input("donnez moi un prix"))
taux_TVA=float(input("donnez moi le taux"))
tva = prix_HT * taux_TVA / 100
print ("le taux TVA est :",tva)
prix_ttc = prix_HT + tva
print("le Prix TTC est :",prix_ttc)
print (f"Pour un prix HT de {prix_HT}€ et une TVA de {taux_TVA}%, le prix TTC est de {prix_ttc}€.")