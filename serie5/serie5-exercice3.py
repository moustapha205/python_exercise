from typing import List


def calculer_moyenne(notes: List[float]) -> float:
    """
    Calcule la moyenne d'une liste de notes.
    """
    return sum(notes) / len(notes)


def filtrer_notes_suffisantes(notes: List[float], seuil: float) -> List[float]:
    """
    Filtre et renvoie toutes les notes >= seuil.
    """
    result = []
    for n in notes:
        if n >= seuil:
            result.append(n)
    return result


def formater_message(nom: str, moyenne: float) -> str:
    """
    Formate un message contenant le nom et la moyenne.
    """
    return f"Étudiant {nom} : moyenne = {moyenne:.2f}"


#test
if __name__ == "__main__":

    notes = [12.5, 9.0, 14.25, 7.5, 16.0]

    moyenne = calculer_moyenne(notes)
    notes_valides = filtrer_notes_suffisantes(notes, 10)

    print("Notes :", notes)
    print("Moyenne :", moyenne)
    print("Notes >= 10 :", notes_valides)

    message = formater_message("Alice", moyenne)
    print(message)
