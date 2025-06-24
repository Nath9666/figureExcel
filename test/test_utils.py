import pytest
from app.utils import HexToRGB

def test_hex_to_rgb_basic():
    assert HexToRGB("#FFFFFF") == (255, 255, 255)
    assert HexToRGB("#000000") == (0, 0, 0)
    assert HexToRGB("#FF0000") == (255, 0, 0)
    assert HexToRGB("#00FF00") == (0, 255, 0)
    assert HexToRGB("#0000FF") == (0, 0, 255)

def test_hex_to_rgb_without_hash():
    assert HexToRGB("FFFFFF") == (255, 255, 255)
    assert HexToRGB("000000") == (0, 0, 0)

def test_hex_to_rgb_mixed_case():
    assert HexToRGB("#fFfFfF") == (255, 255, 255)
    assert HexToRGB("aBc123") == (171, 193, 35)

def test_hex_to_rgb_invalid_length():
    with pytest.raises(ValueError):
        HexToRGB("#FFF")
    with pytest.raises(ValueError):
        HexToRGB("#FFFFF")
    with pytest.raises(ValueError):
        HexToRGB("#FFFFFFFF")

def test_hex_to_rgb_invalid_characters():
    with pytest.raises(ValueError):
        HexToRGB("#GGGGGG")
    with pytest.raises(ValueError):
        HexToRGB("ZZZZZZ")