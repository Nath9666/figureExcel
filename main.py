import pandas as pd
import sys
import configparser
import xlwings as xw
import os
import colorama
from colorama import Fore, Style
import ast


def lire_config(chemin_config):
    config = configparser.ConfigParser()
    config.read(chemin_config, encoding="utf-8")

    # ? parametre concernant le graphique
    if "Graphique" not in config:
        raise ValueError(
            "La section 'Graphique' est manquante dans le fichier de configuration."
        )
    params = config["Graphique"]
    arrondi = int(params.get("arrondi", 1))

    # ? Couleur
    couleur_fond = params.get("couleur_fond", "#FFFFFF")
    couleur_fond = HexToRGB(couleur_fond)
    couleur_axes = params.get("couleur_axes", "#CCCCCC")
    couleur_axes = HexToRGB(couleur_axes)

    largeur_ligne = int(params.get("largeur_ligne", 2))
    hauteur_ligne = int(params.get("hauteur_ligne", 2))
    quadrillage = params.get("quadrillage", "oui").lower() == "oui"
    marqueur = params.get("marqueur", "non").lower() == "oui"

    return (
        arrondi,
        couleur_fond,
        couleur_axes,
        largeur_ligne,
        hauteur_ligne,
        quadrillage,
        marqueur,
    )


def HexToRGB(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def lire_donnees_excel(chemin_fichier):
    try:
        df = pd.read_excel(chemin_fichier)
        if df.empty:
            print(Fore.RED + "Le fichier Excel est vide ou ne contient pas de données.")
            exit(1)
        print(Fore.CYAN + "Nom des colonnes : " + str(df.columns.tolist()))
        return df
    except Exception as e:
        print(Fore.RED + f"Erreur lors de la lecture du fichier : {e}")
        return None


def inserer_courbe_xlwings(df, out_xlsx, arrondi, couleur_ligne):
    # Arrondi et tri
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")

    # Création du classeur
    app = xw.App(visible=False)
    wb = app.books.add()
    ws_data = wb.sheets[0]
    ws_data.name = "Données"
    ws_data.range("A1").value = df[1:].columns.tolist()  # En-têtes
    ws_data.range("A2").value = df[0:].values.tolist()

    # Ajout d'une feuille de graphique (chart sheet via COM)
    chart_obj = wb.api.Charts.Add()
    chart_obj.ChartType = xw.constants.ChartType.xlLine
    chart_obj.SetSourceData(ws_data.range("A1").expand().api)
    chart_obj.HasTitle = True
    chart_obj.ChartTitle.Text = (
        "Courbe XY allant du "
        + df["Date"].min().strftime("%d/%m/%Y")
        + " au "
        + df["Date"].max().strftime("%d/%m/%Y")
    )
    chart_obj.Axes(1).HasTitle = True
    chart_obj.Axes(1).AxisTitle.Text = "Date"
    chart_obj.Axes(2).HasTitle = True
    chart_obj.Axes(2).AxisTitle.Text = "Données"

    try:
        couleur = (0, 128, 255)  # bleu clair
        chart_obj.SeriesCollection(1).Format.Line.ForeColor.RGB = xw.utils.rgb_to_int(
            couleur
        )
    except Exception:
        print(
            "Erreur lors de la définition de la couleur de la ligne, utilisation de la couleur par défaut."
        )

    chart_obj.Name = "Graphique"
    wb.save(out_xlsx)
    wb.close()
    app.quit()


def read_parameters():
    data = {
        "RefName": "Date",
        "DataName1": "Données 1",
        "MinValue1": 0,
        "MaxValue1": 100,
        "DataName2": "Données 2",
        "MinValue2": 0,
        "MaxValue2": 100,
    }
    # $ python main.py ./data/Classeur1.xlsx Date [[Donne1, 10, 15,?Titre, ?#0000],[Donne2,4,15, ?Titre, ?#0000]]


if __name__ == "__main__":
    errors = []
    messageHelp = "Faite --help si vous avez besoin d'aide."
    colorama.init(autoreset=True)
    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        print(Fore.GREEN + Style.BRIGHT + "Aide :")
        print(
            Fore.YELLOW
            + Style.BRIGHT
            + "Ce script permet de générer un graphique à partir d'un fichier Excel.\n"
            "Usage : python main.py <chemin_fichier_excel> <Nom de la colonne de référence> [[<Nom de la donnée>, <Min>, <Max>, ?Titre, ?Couleur], ...]\n"
            + "Exemple : python main.py ./data/Classeur1.xlsx Date [['Données 1', 10, 15, 'Titre 1', '#FF0000'], ['Données 2', 4, 15, 'Titre 2', '#00FF00']]"
        )
        sys.exit(0)

    if len(sys.argv) < 4:
        errors.append(
            Fore.RED
            + Style.BRIGHT
            + "Erreur : Nombre de paramètres insuffisant 3 demandé"
        )
        errors.append(
            Fore.YELLOW
            + Style.BRIGHT
            + "Veuillez fournir le chemin du fichier Excel, le nom de la colonne de référence et la liste des données."
        )
        errors.append(
            Fore.CYAN
            + Style.BRIGHT
            + "Exemple : python main.py ./data/Classeur1.xlsx Date [[Données 1, 10, 15, Titre 1, #FF0000], [Données 2, 4, 15, Titre 2, #00FF00]]"
        )
        errors.append(Fore.CYAN + Style.BRIGHT + messageHelp)
        for error in errors:
            print(error)
        exit(1)

    if (
        sys.argv[1] is None
        or sys.argv[1] == ""
        or not sys.argv[1].endswith(".xlsx")
        or not os.path.exists(sys.argv[1])
    ):
        errors.append(
            Fore.RED + Style.BRIGHT + "Le chemin du fichier Excel est requis."
        )

    if (
        sys.argv[2] is None
        or sys.argv[2] == ""
        or not isinstance(sys.argv[2], str)
        or sys.argv[2].isdigit()
    ):
        errors.append(
            Fore.RED
            + Style.BRIGHT
            + "Le nom de la colonne de référence doit être une chaîne de caractères non vide soit un string"
        )

    # Ajoute ceci pour parser l'argument en liste
    try:
        data_list = ast.literal_eval(sys.argv[3])
    except Exception as e:
        errors.append(
            Fore.RED
            + Style.BRIGHT
            + f"Erreur lors de la conversion de la liste des données : {e}"
        )
        data_list = []

    if not isinstance(data_list, list) or len(data_list) < 1:
        errors.append(
            Fore.RED
            + Style.BRIGHT
            + "La liste des données doit être une liste non vide."
        )

    if not all(isinstance(item, list) and len(item) >= 3 for item in data_list):
        errors.append(
            Fore.RED
            + Style.BRIGHT
            + "Chaque élément de la liste des données doit être une liste de 3 éléments minimum : [Nom, Min, Max]. Si un titre ou une couleur est fourni, il doit être ajouté à la fin de la liste."
        )

    if len(errors) > 0:
        for error in errors:
            print(error)
        print(Fore.CYAN + "Veuillez corriger les erreurs et réessayer.\n" + messageHelp)
        sys.exit(1)
    else:
        print(Fore.MAGENTA + "Paramètres valides, traitement en cours...")

        chemin_excel = sys.argv[1]
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
            inserer_courbe_xlwings(df, out_xlsx, arrondi_graphique, couleur_ligne)
            print(f"Courbe Excel (feuille graphique) générée dans {out_xlsx}")
        else:
            print(Fore.RED + "Erreur lors de la génération de la courbe.")
