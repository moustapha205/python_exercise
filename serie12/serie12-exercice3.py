# td12_ex3_complet.py
import unittest

# CODE METIER (Module à tester)


def calculer_prix_ttc(prix_ht, taux_tva):
    """
    Calcule le prix TTC. Lève une ValueError si le prix HT est négatif.
    """
    if prix_ht < 0:
        raise ValueError("Le prix HT doit être positif")
    return prix_ht * (1 + taux_tva)



# CODE DE TEST (Unit Tests)


class TestCalculerPrixTTC(unittest.TestCase):
    
    def test_cas_simple_tva_20(self):
        """Vérifie le calcul standard (100 * 1.20 = 120)."""
        prix_ht = 100
        taux_tva = 0.20
        attendu = 120.0
        # self.assertEqual pour les résultats exacts
        self.assertEqual(calculer_prix_ttc(prix_ht, taux_tva), attendu)
        
    def test_prix_nul(self):
        """Vérifie que le prix TTC d'un article à 0 HT est 0."""
        self.assertEqual(calculer_prix_ttc(0, 0.20), 0)
        
    def test_prix_flottant_arrondi(self):
        """Utilise assertAlmostEqual pour gérer la précision des flottants."""
        prix_ht = 16.66
        taux_tva = 0.10 
        attendu = 18.326 
        # On vérifie jusqu'à 3 décimales (places=3)
        self.assertAlmostEqual(calculer_prix_ttc(prix_ht, taux_tva), attendu, places=3)

    def test_exception_prix_negatif(self):
        """Vérifie que l'exception ValueError est levée pour un prix HT négatif."""
        # On utilise with self.assertRaises(...) pour intercepter l'exception
        with self.assertRaises(ValueError):
            calculer_prix_ttc(-50, 0.20)
            
            
if __name__ == "__main__":
    # Exécute tous les tests définis dans la classe
    unittest.main()