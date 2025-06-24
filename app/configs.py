import configparser
from utils import HexToRGB

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