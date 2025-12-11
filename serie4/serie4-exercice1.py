while True:
    try:
        age = int(input("Entrez votre âge : "))
        
        if age < 0:
            print("L'âge ne peut pas être négatif.")
            continue   
        break   

    except ValueError:
        print("Erreur : vous devez entrer un nombre entier.")

print(f"Vous avez {age} ans.")
