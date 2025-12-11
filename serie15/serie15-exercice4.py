# td15_ex4.py
from datetime import datetime

# =========================================================
# PARTIE 1 : Héritage (Relation "est un" - is-a)
# =========================================================

class Logger:
    """Classe de base pour le logging."""
    def log(self, message):
        print(f"[INFO] {message}")

class TimestampLogger(Logger):
    """Hérite de Logger et ajoute un horodatage."""
    def log(self, message):
        # Utilisation de super() pour réutiliser la logique d'affichage de base
        timestamp = datetime.now().isoformat(timespec='seconds')
        super().log(f"{timestamp} - {message}")

class UppercaseLogger(Logger):
    """Hérite de Logger et convertit le message en majuscules."""
    def log(self, message):
        # Surcharge et modification avant d'appeler le log de base
        message_upper = message.upper()
        super().log(message_upper)


# PARTIE 2 : Composition (Relation "a un" - has-a)


class Application:
    """
    Utilise la composition : 'a un' objet logger.
    """
    def __init__(self, logger):
        # Composition : l'attribut self.logger est une instance de la classe Logger 
        # ou de n'importe quelle sous-classe (TimestampLogger, etc.).
        self.logger = logger
        
    def executer(self, action_name):
        # Le code de l'application utilise le logger sans se soucier de son type exact
        self.logger.log(f"Début de l'action : {action_name}")
        # ... traitements ...
        self.logger.log(f"Fin de l'action : {action_name}")


# --- Bloc principal ---
if __name__ == "__main__":
    
    # 1. Test de l'héritage (Comportement spécifique)
    print("--- Test d'Héritage (Polymorphisme) ---")
    Logger().log("Message de base")
    TimestampLogger().log("Message horodaté")
    UppercaseLogger().log("Message en majuscules")
    
    # 2. Test de la composition (Flexibilité)
    print("\n--- Test de Composition (Flexibilité) ---")
    
    # Création d'une application A avec un logger horodaté
    app_A = Application(TimestampLogger())
    app_A.executer("Initialisation du système A")
    
    # Création d'une application B avec un logger majuscule
    app_B = Application(UppercaseLogger())
    app_B.executer("Sauvegarde des données B")
    
    
    # COMMENTAIRES sur Héritage vs Composition
    """
    1. Classes liées par héritage :
       - TimestampLogger et UppercaseLogger héritent de Logger (Logger est le parent).
       - Ils modélisent la relation : "Un TimestampLogger est un Logger".
       
    2. Classe qui utilise la composition :
       - La classe Application utilise la composition. Elle modélise la relation : 
         "Une Application a un Logger" (self.logger).
         
    3. Pourquoi la composition est plus flexible ici :
       - La classe Application n'a pas été modifiée du tout entre app_A et app_B. 
         Elle ne dépend que de l'interface (la méthode 'log()').
       - Si nous devions ajouter un nouveau type de logger (ex: JsonLogger), 
         il suffirait de créer cette nouvelle classe et de l'injecter à l'Application, 
         sans toucher au code interne d'Application.
       - Si nous avions utilisé l'héritage (ex: class AppliTimestamp(Application):), 
         nous aurions dû créer une nouvelle classe d'Application pour chaque nouveau 
         style de logging.
    """