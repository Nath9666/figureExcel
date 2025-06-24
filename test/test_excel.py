import pytest
import pandas as pd
import tempfile
import os
from app import excel

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "Date": ["2024-01-01", "2024-01-02", "2024-01-03"],
        "Valeur": [1.1, 2.2, 3.3]
    })

def test_lire_donnees_excel_reads_valid_file(tmp_path, sample_df):
    file_path = tmp_path / "test.xlsx"
    sample_df.to_excel(file_path, index=False)
    df = excel.lire_donnees_excel(str(file_path))
    assert df is not None
    assert list(df.columns) == ["Date", "Valeur"]
    assert len(df) == 3

def test_lire_donnees_excel_empty_file(tmp_path, capsys):
    file_path = tmp_path / "empty.xlsx"
    pd.DataFrame().to_excel(file_path, index=False)
    with pytest.raises(SystemExit):
        excel.lire_donnees_excel(str(file_path))
    captured = capsys.readouterr()
    assert "Le fichier Excel est vide" in captured.out

def test_lire_donnees_excel_file_not_found(capsys):
    df = excel.lire_donnees_excel("non_existent_file.xlsx")
    assert df is None
    captured = capsys.readouterr()
    assert "Erreur lors de la lecture du fichier" in captured.out

def test_inserer_courbe_xlwings_creates_file(tmp_path, sample_df, monkeypatch):
    # Patch xlwings to avoid opening Excel during tests
    class DummyApp:
        def __init__(self, visible):
            self.books = self
        def add(self):
            return DummyBook()
        def quit(self):
            pass
    class DummyBook:
        def __init__(self):
            self.sheets = [DummySheet()]
            self.api = DummyAPI()
        def save(self, path): pass
        def close(self): pass
    class DummySheet:
        def __init__(self):
            self.name = ""
            self._range = DummyRange()
        def range(self, _):
            return self._range
    class DummyRange:
        def __init__(self):
            self.value = None
        def expand(self):
            return self
        @property
        def api(self):
            return object()
    class DummyAPI:
        def __init__(self):
            self.Charts = self
        def Add(self):
            return DummyChart()
    class DummyChart:
        def __init__(self):
            self.ChartType = None
            self.HasTitle = False
            self.ChartTitle = type("obj", (), {"Text": ""})()
            self.Axes = lambda idx: type("obj", (), {"HasTitle": False, "AxisTitle": type("obj", (), {"Text": ""})()})()
            self.SeriesCollection = lambda idx: type("obj", (), {"Format": type("obj", (), {"Line": type("obj", (), {"ForeColor": type("obj", (), {"RGB": 0})()})()})()})()
            self.Name = ""
        def SetSourceData(self, api): pass

    monkeypatch.setattr(excel.xw, "App", DummyApp)
    monkeypatch.setattr(excel.xw, "constants", type("obj", (), {"ChartType": type("obj", (), {"xlLine": 4})()})())
    monkeypatch.setattr(excel.xw, "utils", type("obj", (), {"rgb_to_int": lambda c: 123456})())

    out_xlsx = tmp_path / "output.xlsx"
    # Should not raise
    excel.inserer_courbe_xlwings(sample_df.copy(), str(out_xlsx), arrondi=2, couleur_ligne=(0, 128, 255))