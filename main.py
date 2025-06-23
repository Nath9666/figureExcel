import pandas as pd
import sys
import configparser
import xlwings as xw


def lire_config(chemin_config):
    config = configparser.ConfigParser()
    config.read(chemin_config, encoding='utf-8')
    params = config['Graphique']
    largeur = int(params.get('largeur', 800))
    hauteur = int(params.get('hauteur', 600))
    arrondi = int(params.get('arrondi', 1))
    couleur_ligne = params.get('couleur_ligne', 'blue')
    return largeur, hauteur, arrondi, couleur_ligne


def lire_donnees_excel(chemin_fichier):
    try:
        df = pd.read_excel(chemin_fichier)
        return df
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return None


def inserer_courbe_xlwings(df, out_xlsx, arrondi, couleur_ligne):
    # Arrondi et tri
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')

    # Création du classeur
    app = xw.App(visible=False)
    wb = app.books.add()
    ws_data = wb.sheets[0]
    ws_data.name = 'Données'
    ws_data.range('A1').value = df[1:].columns.tolist()  # En-têtes
    ws_data.range('A2').value = df[0:].values.tolist()
    

    # Ajout d'une feuille de graphique (chart sheet via COM)
    chart_obj = wb.api.Charts.Add()
    chart_obj.ChartType = xw.constants.ChartType.xlLine
    chart_obj.SetSourceData(ws_data.range('A1').expand().api)
    chart_obj.HasTitle = True
    chart_obj.ChartTitle.Text = 'Courbe XY allant du ' + df['Date'].min().strftime('%d/%m/%Y') + ' au ' + df['Date'].max().strftime('%d/%m/%Y')
    chart_obj.Axes(1).HasTitle = True
    chart_obj.Axes(1).AxisTitle.Text = 'Date'
    chart_obj.Axes(2).HasTitle = True
    chart_obj.Axes(2).AxisTitle.Text = 'Données'

    try:
        couleur = (0, 128, 255)  # bleu clair
        chart_obj.SeriesCollection(1).Format.Line.ForeColor.RGB = xw.utils.rgb_to_int(couleur)
    except Exception:
        print("Erreur lors de la définition de la couleur de la ligne, utilisation de la couleur par défaut.")

    chart_obj.Name = 'Graphique'
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
    #$ python main.py ./data/Classeur1.xlsx Date [[Donne1, 10, 15,?Titre, ?#0000],[Donne2,4,15, ?Titre, ?#0000]]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage : python main.py <chemin_fichier_excel>")
    else:
        chemin_excel = sys.argv[1]
        chemin_config = "config.ini"
        out_xlsx = "out.xlsx"
        largeur, hauteur, arrondi, couleur_ligne = lire_config(chemin_config)
        df = lire_donnees_excel(chemin_excel)
        if df is not None:
            inserer_courbe_xlwings(df, out_xlsx, arrondi, couleur_ligne)
            print(f"Courbe Excel (feuille graphique) générée dans {out_xlsx}")
        else:
            print("Erreur lors de la génération de la courbe.")