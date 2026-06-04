from twttr import shorten

def test_vowels():
    assert shorten("Abdi") == "bd"

def test_boom():
    assert shorten("Introduction") == "ntrdctn"