
commandes = [
    {"id": 1, "client": "alice@gmail.com.com",  "montant": 49.90, "statut": "payee"},
    {"id": 2, "client": "bob@gmail.com.com",    "montant": 15.00, "statut": "annulee"},
    {"id": 3, "client": "alice@gmail.com",  "montant": 19.90, "statut": "payee"},
    {"id": 4, "client": "charlie@gmail.com","montant": 120.0, "statut": "en_attente"},
    {"id": 5, "client": "bob@gmail.com",    "montant": 35.0,  "statut": "payee"},
]


ca_total = sum(c["montant"] for c in commandes if c["statut"] == "payee")
print("Chiffre d'affaires total :", ca_total)


commandes_par_statut = {"payee": 0, "annulee": 0, "en_attente": 0}
for c in commandes:
    commandes_par_statut[c["statut"]] += 1

print("Nombre de commandes par statut :", commandes_par_statut)


depenses_par_client = {}
for c in commandes:
    client = c["client"]
    montant = c["montant"]
    if client in depenses_par_client:
        depenses_par_client[client] += montant
    else:
        depenses_par_client[client] = montant

print("Montant total dépensé par client :", depenses_par_client)
