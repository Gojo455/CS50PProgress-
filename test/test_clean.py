from fuel import clean_date
def test_clean_date():
    assert clean_date("N/A") == None
    assert clean_date("ab/cd/2023") == None
    assert clean_date("32/90/2004") == None
def test_correct_year():
    assert clean_date("23/10/2005") == "2005-10-23"
def test_invalid_year():
    assert clean_date("22/09/abbs") == None
def test_lower_year_limit():
    assert clean_date("22/09/1940") == None
    assert clean_date("22/09/1990") == "1990-09-22"
