import pytest
import os
from unittest import mock
from app import params

def test_insufficient_params():
    argv = ["main.py", "file.xlsx"]
    errors, data_list = params.check_params(argv)
    assert errors
    assert "Nombre de paramètres insuffisant" in errors[0]
    assert data_list is None

def test_invalid_excel_path():
    argv = ["main.py", "notfound.xlsx", "Date", "[[Nom, 1, 2]]"]
    with mock.patch("os.path.exists", return_value=False):
        errors, data_list = params.check_params(argv)
    assert any("Le chemin du fichier Excel est requis." in e for e in errors)

def test_invalid_column_name():
    argv = ["main.py", "file.xlsx", "123", "[[Nom, 1, 2]]"]
    with mock.patch("os.path.exists", return_value=True):
        errors, data_list = params.check_params(argv)
    assert any("Le nom de la colonne de référence doit être une chaîne de caractères" in e for e in errors)

def test_invalid_data_list_syntax():
    argv = ["main.py", "file.xlsx", "Date", "[[Nom, 1, 2]"]
    with mock.patch("os.path.exists", return_value=True):
        errors, data_list = params.check_params(argv)
    assert any("Erreur lors de la conversion de la liste des données" in e for e in errors)
    assert isinstance(data_list, list)

def test_empty_data_list():
    argv = ["main.py", "file.xlsx", "Date", "[]"]
    with mock.patch("os.path.exists", return_value=True):
        errors, data_list = params.check_params(argv)
    assert any("La liste des données doit être une liste non vide." in e for e in errors)

def test_data_list_element_too_short():
    argv = ["main.py", "file.xlsx", "Date", "[[Nom, 1]]"]
    with mock.patch("os.path.exists", return_value=True):
        errors, data_list = params.check_params(argv)
    assert any("Chaque élément de la liste des données doit être une liste de 3 éléments minimum" in e for e in errors)

def test_valid_params_minimal(monkeypatch, tmp_path):
    # Create a dummy file
    file_path = tmp_path / "file.xlsx"
    file_path.write_text("dummy")
    argv = ["main.py", str(file_path), "Date", "[['Nom', 1, 2]]"]
    errors, data_list = params.check_params(argv)
    assert errors == []
    assert data_list == [['Nom', 1, 2]]

def test_valid_params_with_title_and_color(tmp_path):
    file_path = tmp_path / "file.xlsx"
    file_path.write_text("dummy")
    argv = ["main.py", str(file_path), "Date", "[['Nom', 1, 2, 'Titre', '#FF0000']]"]
    errors, data_list = params.check_params(argv)
    assert errors == []
    assert data_list == [['Nom', 1, 2, 'Titre', '#FF0000']]