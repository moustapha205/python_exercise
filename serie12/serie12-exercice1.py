# td12_ex1.py
import logging

# Configuration de base pour le logging
# Level=logging.INFO signifie que seuls les messages INFO, WARNING, ERROR et CRITICAL seront affichés.
# Les messages DEBUG seront ignorés.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def traiter_commande(commande):
    # Remplacé par logging.DEBUG (ne s'affichera pas avec level=logging.INFO)
    logger.debug("Commande reçue : %s", commande)
    
    if not commande:
        logger.error("Commande vide détectée.")
        return

    # Remplacé par logging.INFO
    logger.info("Vérification du stock...")
    
    # Utilisation de .get() pour éviter KeyError si la clé est manquante
    if commande.get("quantite", 0) <= 0:
        logger.error("Quantité invalide ou manquante dans la commande.")
        return

    # Remplacé par logging.INFO
    client_name = commande.get("client", "Inconnu")
    logger.info("Commande validée pour le client : %s", client_name)
    # ... autres traitements ...


if __name__ == "__main__":
    # Test 1 : Commande valide (INFO affiché, DEBUG masqué)
    traiter_commande({"id": 1, "client": "Alice", "quantite": 3})
    
    print("-" * 20)
    
    # Test 2 : Commande invalide (ERROR affiché)
    traiter_commande(None)
    
    print("-" * 20)
    
    # Test 3 : Quantité invalide (ERROR affiché)
    traiter_commande({"id": 2, "client": "Bob", "quantite": 0})