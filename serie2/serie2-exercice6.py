

def calculer_ca(commandes):
    ca = 0
    for cmd in commandes:
        if cmd["statut"] == "payee":
            ca += cmd["montant"]
    return ca


def compter_commandes_par_statut(commandes):
    stats = {"payee": 0, "annulee": 0, "en_attente": 0}
    for cmd in commandes:
        stats[cmd["statut"]] += 1
    return stats


def totaux_par_client(commandes):
    totaux = {}
    for cmd in commandes:
        client = cmd["client"]
        montant = cmd["montant"]
        if client not in totaux:
            totaux[client] = 0
        totaux[client] += montant
    return totaux





commandes = []

with open("/Users/mac/Desktop/python/serie2/commandes.txt", "r") as f:
    for ligne in f:
        ligne = ligne.strip()   
        if ligne == "":
            continue
        
        champs = ligne.split(";") 
        
        commande = {
            "id": int(champs[0]),
            "client": champs[1],
            "montant": float(champs[2]),
            "statut": champs[3]
        }
        
        commandes.append(commande)





if __name__ == "__main__":
    
    print("\n=== Fichier chargé ===")
    print(commandes)

    ca = calculer_ca(commandes)
    stats = compter_commandes_par_statut(commandes)
    totaux = totaux_par_client(commandes)

    print("\n=== Chiffre d'affaires (payé) ===")
    print(ca, "€")

    print("\n=== Commandes par statut ===")
    for statut, nb in stats.items():
        print(f"{statut} : {nb}")

    print("\n=== Dépenses par client ===")
    for client, montant in totaux.items():
        print(f"{client} : {montant} €")
