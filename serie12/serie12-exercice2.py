# td12_ex2.py
import logging
import sys # Utile pour gérer le logging vers la console/stderr

# Configuration avancée pour le logging
logging.basicConfig(
    level=logging.INFO,
    # Format incluant la date/heure, niveau et nom du logger
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    
    # Écriture dans un fichier de log
    filename="commande.log",
    filemode="a", # 'a' pour append (ajouter), 'w' pour write (écraser)
    
    # En plus du fichier, nous configurons un handler pour la console
    # Note: Dans un environnement réel, on utiliserait le module 'handlers'
    # Mais basicConfig enverra par défaut sur la console si aucun 'stream' n'est précisé
)

logger = logging.getLogger(__name__)

# La fonction métier reste la même que dans l'exercice 1
def traiter_commande(commande):
    logger.debug("Commande reçue : %s", commande)
    
    if not commande:
        logger.error("Commande vide détectée.")
        return

    logger.info("Vérification du stock...")
    
    if commande.get("quantite", 0) <= 0:
        # Ceci générera une ERROR dans le fichier commande.log
        logger.error("Quantité invalide ou manquante dans la commande.")
        return

    client_name = commande.get("client", "Inconnu")
    logger.info("Commande validée pour le client : %s", client_name)


if __name__ == "__main__":
    # Test 1 : Commande valide (écrit INFO)
    traiter_commande({"id": 10, "client": "Eva", "quantite": 2})
    
    # Test 2 : Commande invalide pour générer un ERROR dans le log
    traiter_commande({"id": 11, "client": "Frank", "quantite": -5}) 
    
    print("Vérifiez le fichier 'commande.log' pour voir les résultats.")