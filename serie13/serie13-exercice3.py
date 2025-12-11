


# VERSION 1 : FONCTIONS "LIBRES" (Fonctionnelle)

def creer_panier():
    return []

def ajouter_article(panier, article):
    # Modifie la liste 'panier' passée en argument
    panier.append(article)

def total_articles(panier):
    # Lit la liste 'panier' passée en argument
    return len(panier)

print("--- VERSION 1 : Fonctionnelle ---")
panier_a = creer_panier()
ajouter_article(panier_a, "Livre POO")
ajouter_article(panier_a, "Clé USB")
print(f"Panier A articles: {panier_a}")
print(f"Total Panier A: {total_articles(panier_a)}")
print("-" * 30)


# VERSION 2 : CLASSE Panier (POO)


class Panier:
    """
    Gère un panier d'achat avec l'état stocké dans self.articles.
    """
    def __init__(self):
        # self.articles est l'attribut d'instance qui stocke l'état (la liste)
        self.articles = []

    def ajouter_article(self, article):
        """Ajoute un article à l'état interne de l'objet (self.articles)."""
        # self représente l'instance (panier_alice ou panier_bob) sur laquelle la méthode est appelée.
        self.articles.append(article)

    def total_articles(self):
        """Renvoie le nombre d'articles dans l'état interne de l'objet."""
        # self permet d'accéder aux données propres à cette instance.
        return len(self.articles)

# --- Bloc principal (POO) ---
print("--- VERSION 2 : Orientée Objets ---")

# Création de deux objets indépendants
panier_alice = Panier()
panier_bob = Panier()

# Modification de l'état d'Alice
panier_alice.ajouter_article("Théière")
panier_alice.ajouter_article("Tasse")

# Modification de l'état de Bob
panier_bob.ajouter_article("Jeu Vidéo")

print(f"Panier Alice (Total {panier_alice.total_articles()}): {panier_alice.articles}")
print(f"Panier Bob (Total {panier_bob.total_articles()}): {panier_bob.articles}")

# COMMENTAIRES sur self et la transformation :
"""
1. Rôle de self :
   - self est le premier argument de toute méthode d'instance.
   - Il représente l'OBJET INSTANCIÉ ACTUEL.
   - Lorsque nous appelons panier_alice.ajouter_article(...), Python traduit 
     l'appel en Panier.ajouter_article(panier_alice, ...). 
     'self' est donc l'objet 'panier_alice'.
     
2. Changement par rapport à la version fonctionnelle :
   - Dans la version fonctionnelle, l'état (la liste 'panier') devait être 
     passé manuellement en argument à chaque appel (ex: ajouter_article(panier, article)).
   - Dans la version POO, l'état est stocké dans l'attribut d'instance (self.articles). 
     Il est passé implicitement via self, ce qui rend les appels plus courts 
     et le code plus clair : l'objet porte son propre état.
"""