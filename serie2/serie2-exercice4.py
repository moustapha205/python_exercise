commandes = [
    {"id": 1, "client": "alice@gmail.com",  "montant": 49.90, "statut": "payee"},
    {"id": 2, "client": "bob@gmail.com",    "montant": 15.00, "statut": "annulee"},
    {"id": 3, "client": "alice@gmail.com",  "montant": 19.90, "statut": "payee"},
    {"id": 4, "client": "charlie@gmail.com","montant": 120.0, "statut": "en_attente"},
    {"id": 5, "client": "bob@gmail.com",    "montant": 35.0,  "statut": "payee"},
]


def calculer_ca(commandes):
    ca = 0
    for cmd in commandes:
        if cmd["statut"] == "payee":
            ca += cmd["montant"]
    return ca


def compter_commandes_par_statut(commandes):
    stats = {"payee": 0, "annulee": 0, "en_attente": 0}
    for cmd in commandes:
        statut = cmd["statut"]
        stats[statut] += 1
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

if __name__ == "__main__":
    ca = calculer_ca(commandes)
    stats = compter_commandes_par_statut(commandes)
    totaux_clients = totaux_par_client(commandes)

    print("=== CHIFFRE D’AFFAIRES (commandes payées) ===")
    print(f"{ca} €\n")

    print("=== NOMBRE DE COMMANDES PAR STATUT ===")
    for statut, nombre in stats.items():
        print(f"{statut} : {nombre}")
    print()

    print("=== TOTAL DÉPENSÉ PAR CLIENT ===")
    for client, total in totaux_clients.items():
        print(f"{client} : {total} €")
