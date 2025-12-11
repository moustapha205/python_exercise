age_client= int(input("donnez moi votre age"))
print("votre age est :",age_client,"ans")
if age_client < 12:
    print("Le tarif est de 5€")
elif age_client<=17:
    print("le tarif est de 7€")
elif age_client<=25:
    print("Le tarif est de 8,5€ ")
else :
    print("Tarif plein")