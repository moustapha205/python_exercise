def division_securisee():
    

    try:
        numerateur=int(input("donnez moi un numerateur"))
        denominateur=int(input("donnez moi un denominateur"))
        division=numerateur/denominateur
        return division
    except ValueError:
        print("veuillez saisir un entier ")
        return None
    except ZeroDivisionError:
        print("la division par zero est impossible")
        return None
    except Exception as e :
        print("Erreur inaattendu:",e)
        return None
    
division_securisee()
resultat = division_securisee()

if resultat is not None:
    print(f"Résultat : {resultat}")
else:
    print("La division a échoué.")

