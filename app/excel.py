import pandas as pd
from colorama import Fore, Style
import xlwings as xw

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