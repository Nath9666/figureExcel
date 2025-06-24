import pandas as pd
import sys
import os
import colorama
from colorama import Fore, Style
import ast

from app.configs import lire_config
from app.utils import HexToRGB
from app.excel import lire_donnees_excel, inserer_courbe_xlwings
from app.params import check_params
from app.logs import log_error, log_info, setup_logger


if __name__ == "__main__":
    is_terminal = len(sys.argv) > 1 and sys.argv[1] == "-t"
    if not is_terminal:
        setup_logger("../logs/app.log")
    argv = sys.argv[1:] if is_terminal else sys.argv
    if is_terminal:
        argv = [sys.argv[0]] + sys.argv[2:]
    errors, data_list = check_params(argv)
    messageHelp = "Faite --help si vous avez besoin d'aide."
    colorama.init(autoreset=True)
    if (is_terminal and len(sys.argv) > 2 and sys.argv[2] in ["--help", "-h"]) or (not is_terminal and sys.argv[1] in ["--help", "-h"]):
        print(Fore.GREEN + Style.BRIGHT + "Aide :")
        print(
            Fore.YELLOW
            + Style.BRIGHT
            + "Ce script permet de générer un graphique à partir d'un fichier Excel.\n"
            "Usage : python main.py <chemin_fichier_excel> <Nom de la colonne de référence> [[<Nom de la donnée>, <Min>, <Max>, ?Titre, ?Couleur], ...]\n"
            + "Exemple : python main.py ./data/Classeur1.xlsx Date [['Données 1', 10, 15, 'Titre 1', '#FF0000'], ['Données 2', 4, 15, 'Titre 2', '#00FF00']]"
        )
        sys.exit(0)

    if errors:
        for error in errors:
            if is_terminal:
                print(error)
            else:
                log_error(error)
        if is_terminal:
            print(Fore.CYAN + "Veuillez corriger les erreurs et réessayer.\n" + messageHelp)
        else:
            log_info("Veuillez corriger les erreurs et réessayer. " + messageHelp)
        sys.exit(1)
    else:
        if is_terminal:
            print(Fore.MAGENTA + "Paramètres valides, traitement en cours...")
        else:
            log_info("Paramètres valides, traitement en cours...")
        chemin_excel = argv[1]
        chemin_config = "config.ini"
        out_xlsx = "out.xlsx"
        (
            arrondi_graphique,
            couleur_fond,
            couleur_axes,
            largeur_ligne,
            hauteur_ligne,
            quadrillage,
            marqueur,
        ) = lire_config(chemin_config)
        df = lire_donnees_excel(chemin_excel)
        if df is not None:
            inserer_courbe_xlwings(df, out_xlsx, arrondi_graphique)
            if is_terminal:
                print(f"Courbe Excel (feuille graphique) générée dans {out_xlsx}")
            else:
                log_info(f"Courbe Excel (feuille graphique) générée dans {out_xlsx}")
        else:
            if is_terminal:
                print(Fore.RED + "Erreur lors de la génération de la courbe.")
            else:
                log_error("Erreur lors de la génération de la courbe.")
