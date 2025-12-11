# td12_ex4_complet.py
import unittest
import logging


# CODE METIER (Module à tester avec Logging)


# On configure le logger
logger = logging.getLogger(__name__)

def appliquer_remise(prix_ht, remise):
    """
    Applique une remise. Lève ValueError si la remise n'est pas entre 0 et 1.
    """
    if remise < 0 or remise > 1:
        # Le log d'erreur est inclus dans la fonction, mais le test se concentre sur l'exception
        logger.error("Remise invalide : %s", remise)
        raise ValueError("Remise doit être entre 0 et 1")
        
    nouveau_prix = prix_ht * (1 - remise)
    
    # Le log d'information est inclus dans la fonction, mais le test se concentre sur le résultat
    logger.info("Remise appliquée : %s -> %s", prix_ht, nouveau_prix)
    
    return nouveau_prix



# CODE DE TEST (Unit Tests)


class TestAppliquerRemise(unittest.TestCase):
    
    def test_remise_valide(self):
        """Vérifie le calcul avec une remise valide (50% de 200)."""
        prix_ht = 200
        remise = 0.50 # 50%
        attendu = 100.0
        # Le test passe même si la fonction produit un log INFO
        self.assertEqual(appliquer_remise(prix_ht, remise), attendu)
        
    def test_remise_nulle(self):
        """Vérifie que le prix reste le même pour une remise de 0%."""
        self.assertEqual(appliquer_remise(50, 0.0), 50)
        
    def test_remise_invalide_negative_leve_exception(self):
        """Vérifie qu'une remise négative lève ValueError."""
        # Le test vérifie que le code s'arrête avec l'erreur attendue
        with self.assertRaises(ValueError):
            appliquer_remise(100, -0.10)

    def test_remise_invalide_trop_elevee_leve_exception(self):
        """Vérifie qu'une remise > 100% lève ValueError."""
        with self.assertRaises(ValueError):
            appliquer_remise(100, 1.25)


if __name__ == "__main__":
    # Conseil pour les tests : Pour éviter que les logs INFO/ERROR ne s'affichent 
    # pendant l'exécution des tests, on configure le logging pour ignorer ces niveaux.
    logging.basicConfig(level=logging.CRITICAL) 
    
    unittest.main()