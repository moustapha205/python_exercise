import json



def calculer_ca(commandes):
    return sum(cmd["montant"] for cmd in commandes if cmd["statut"] == "payee")

def compter_commandes_par_statut(commandes):
    stats = {"payee": 0, "annulee": 0, "en_attente": 0}
    for cmd in commandes:
        stats[cmd["statut"]] += 1
    return stats

def totaux_par_client(commandes):
    totaux = {}
    for cmd in commandes:
        client = cmd["client"]
        totaux[client] = totaux.get(client, 0) + cmd["montant"]
    return totaux




with open("/Users/mac/Desktop/python/serie2/commandes.json", "r", encoding="utf-8") as f:
    commandes = json.load(f)

print("Fichier JSON chargé ✔️\n")




print("=== Chiffre d’affaires ===")
print(calculer_ca(commandes), "€\n")

print("=== Commandes par statut ===")
for statut, nb in compter_commandes_par_statut(commandes).items():
    print(statut, ":", nb)
print()

print("=== Dépenses par client ===")
for client, total in totaux_par_client(commandes).items():
    print(client, ":", total, "€")
