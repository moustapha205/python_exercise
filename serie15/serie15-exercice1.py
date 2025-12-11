# td15_ex1.py

class Animal:
    """Classe de base pour tous les animaux."""
    
    def __init__(self, nom):
        # Attribut d'instance hérité
        self.nom = nom
        
    def parler(self):
        """Méthode de base à surcharger."""
        print(f"{self.nom} (type Animal) fait un bruit.")

class Chien(Animal):
    """Classe dérivée de Animal."""
    
    def __init__(self, nom):
        # Appel du constructeur de la classe parente (Animal)
        super().__init__(nom)
        
    def parler(self):
        """Surcharge de la méthode : comportement spécifique au Chien."""
        print(f"{self.nom} aboie : Wouf ! Wouf !")

class Chat(Animal):
    """Classe dérivée de Animal."""
    
    def __init__(self, nom):
        # Appel du constructeur de la classe parente (Animal)
        super().__init__(nom)
        
    def parler(self):
        """Surcharge de la méthode : comportement spécifique au Chat."""
        print(f"{self.nom} miaule : Miaou ! Grrr...")


# --- Bloc principal ---
if __name__ == "__main__":
    
    # Création des instances
    a1 = Animal("Bête Sauvage")
    c1 = Chien("Rex")
    c2 = Chat("Félix")

    # Mise dans une liste (Polymorphisme : la liste contient des objets de types différents)
    animaux = [a1, c1, c2]
    
    print("--- Démonstration du Polymorphisme (Surcharge) ---")
    
    for animal in animaux:
        # Le même appel de méthode produit un comportement différent
        animal.parler()

    # COMMENTAIRES
    """
    Explication des concepts :
    
    1. Héritage : C'est le mécanisme par lequel une classe (enfant/dérivée, ex: Chien) 
       acquiert les attributs et méthodes d'une autre classe (parent/base, ex: Animal). 
       On modélise une relation "est un" (un Chien est un Animal).
       
    2. Surcharge (Overriding) : C'est le fait de redéfinir une méthode héritée 
       (ici 'parler') dans la classe enfant pour lui donner un comportement 
       spécifique (Wouf, Miaou).
       
    3. Polymorphisme : C'est la capacité d'écrire du code uniforme (ici, la boucle 
       'animal.parler()') qui se comporte différemment selon le type réel de l'objet 
       traité (Chien, Chat ou Animal).
    """