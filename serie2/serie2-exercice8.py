import json

def calculer_ca(commandes):
    """Calcule le chiffre d'affaires total des commandes payées"""
    return sum(c["montant"] for c in commandes if c["statut"] == "payee")

def compter_commandes_par_statut(commandes):
    """Compte le nombre de commandes par statut"""
    stats = {"payee": 0, "annulee": 0, "en_attente": 0}
    for c in commandes:
        stats[c["statut"]] += 1
    return stats

def totaux_par_client(commandes):
    """Calcule le montant total dépensé par chaque client"""
    totaux = {}
    for c in commandes:
        client = c["client"]
        totaux[client] = totaux.get(client, 0) + c["montant"]
    return totaux



if __name__ == "__main__":
    
    try:
        with open("/Users/mac/Desktop/python/serie2/commandes.json", "r", encoding="utf-8") as f:
            commandes = json.load(f)
    except FileNotFoundError:
        print("Erreur : le fichier commandes.json est introuvable.")
        exit(1)

    
    ca = calculer_ca(commandes)
    stats = compter_commandes_par_statut(commandes)
    totaux_clients = totaux_par_client(commandes)

    
    print("=== Tableau de bord commandes ===\n")
    print(f"Chiffre d'affaires (commandes payées) : {ca:.2f} €\n")

    print("Nombre de commandes par statut :")
    for statut, nombre in stats.items():
        print(f"  - {statut:<10} : {nombre}")
    print()

    print("Top clients :")
    
    top_clients = sorted(totaux_clients.items(), key=lambda x: x[1], reverse=True)
    for client, total in top_clients:
        print(f"  - {client:<20} : {total:.2f} €")
