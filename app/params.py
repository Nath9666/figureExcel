from colorama import Fore, Style
import os
import ast

def check_params(argv):
    errors = []
    messageHelp = "Faite --help si vous avez besoin d'aide."
    if len(argv) < 4:
        errors.append(
            Fore.RED + Style.BRIGHT + "Erreur : Nombre de paramètres insuffisant 3 demandé"
        )
        errors.append(
            Fore.YELLOW + Style.BRIGHT + "Veuillez fournir le chemin du fichier Excel, le nom de la colonne de référence et la liste des données."
        )
        errors.append(
            Fore.CYAN + Style.BRIGHT + "Exemple : python main.py ./data/Classeur1.xlsx Date [[Données 1, 10, 15, Titre 1, #FF0000], [Données 2, 4, 15, Titre 2, #00FF00]]"
        )
        errors.append(Fore.CYAN + Style.BRIGHT + messageHelp)
        return errors, None

    if (
        argv[1] is None
        or argv[1] == ""
        or not argv[1].endswith(".xlsx")
        or not os.path.exists(argv[1])
    ):
        errors.append(
            Fore.RED + Style.BRIGHT + "Le chemin du fichier Excel est requis."
        )

    if (
        argv[2] is None
        or argv[2] == ""
        or not isinstance(argv[2], str)
        or argv[2].isdigit()
    ):
        errors.append(
            Fore.RED + Style.BRIGHT + "Le nom de la colonne de référence doit être une chaîne de caractères non vide soit un string"
        )

    try:
        data_list = ast.literal_eval(argv[3])
    except Exception as e:
        errors.append(
            Fore.RED + Style.BRIGHT + f"Erreur lors de la conversion de la liste des données : {e}"
        )
        data_list = []

    if not isinstance(data_list, list) or len(data_list) < 1:
        errors.append(
            Fore.RED + Style.BRIGHT + "La liste des données doit être une liste non vide."
        )

    if not all(isinstance(item, list) and len(item) >= 3 for item in data_list):
        errors.append(
            Fore.RED + Style.BRIGHT + "Chaque élément de la liste des données doit être une liste de 3 éléments minimum : [Nom, Min, Max]. Si un titre ou une couleur est fourni, il doit être ajouté à la fin de la liste."
        )

    return errors, data_list