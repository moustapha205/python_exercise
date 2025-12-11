
class CommandeInvalideError(Exception):
    pass


def valider_commande(montant):
    if montant <= 0:
        raise CommandeInvalideError("Montant invalide : doit être supérieur à 0.")
    if montant > 10_000:
        raise CommandeInvalideError("Montant suspect : ne peut pas dépasser 10 000.")
    return True


try:
    montant = float(input("Saisissez le montant de la commande : "))
    if valider_commande(montant):
        print("Commande valide")

except ValueError:
    print("Erreur : vous devez saisir un nombre.")

except CommandeInvalideError as e:
    print(f"Commande invalide : {e}")
