from twttr import shorten

def test_accuurate():
    assert shorten("Ayomide") == "ymd"

def test_inaccurate():
    assert shorten("David") != "David"

def test_no():
    assert shorten("CS50") == "CS50"

def test_punct():
    assert shorten("Hll,wrld") == "Hll,wrld"
