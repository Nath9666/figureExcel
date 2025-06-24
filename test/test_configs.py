import pytest
import configparser
from unittest import mock
from app.configs import lire_config

@pytest.fixture
def mock_hex_to_rgb():
    with mock.patch("app.configs.HexToRGB") as hex_mock:
        hex_mock.side_effect = lambda x: f"rgb({x})"
        yield hex_mock

def make_config_file(tmp_path, content):
    config_path = tmp_path / "test.ini"
    config_path.write_text(content, encoding="utf-8")
    return str(config_path)

def test_lire_config_valid_all_params(tmp_path, mock_hex_to_rgb):
    config_content = """
[Graphique]
arrondi = 3
couleur_fond = #123456
couleur_axes = #654321
largeur_ligne = 5
hauteur_ligne = 7
quadrillage = oui
marqueur = oui
"""
    config_path = make_config_file(tmp_path, config_content)
    result = lire_config(config_path)
    assert result == (
        3,
        "rgb(#123456)",
        "rgb(#654321)",
        5,
        7,
        True,
        True,
    )

def test_lire_config_defaults(tmp_path, mock_hex_to_rgb):
    config_content = """
[Graphique]
"""
    config_path = make_config_file(tmp_path, config_content)
    result = lire_config(config_path)
    # Defaults: arrondi=1, couleur_fond=#FFFFFF, couleur_axes=#CCCCCC, largeur_ligne=2, hauteur_ligne=2, quadrillage=oui, marqueur=non
    assert result == (
        1,
        "rgb(#FFFFFF)",
        "rgb(#CCCCCC)",
        2,
        2,
        True,
        False,
    )

def test_lire_config_quadrillage_marqueur_variants(tmp_path, mock_hex_to_rgb):
    config_content = """
[Graphique]
quadrillage = non
marqueur = oui
"""
    config_path = make_config_file(tmp_path, config_content)
    result = lire_config(config_path)
    assert result[5] is False  # quadrillage
    assert result[6] is True   # marqueur

def test_lire_config_missing_section(tmp_path):
    config_content = """
[AutreSection]
arrondi = 2
"""
    config_path = make_config_file(tmp_path, config_content)
    with pytest.raises(ValueError, match="La section 'Graphique' est manquante"):
        lire_config(config_path)