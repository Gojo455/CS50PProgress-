from clean import  clean_date
import datetime


def test_years_accepted():
    year = 1960
    assert clean_date(f"15/02/{year}") == "1960-02-15"
    
def test_hyphen_branch():
    year = 1960
    assert clean_date(f"{year}-02-15") == "1960-02-15"
    assert clean_date(f"{year}-02-32") is None

def test_monthname_branch():
    year = 2005
    assert clean_date(f"March 2 {year}") == "2005-03-02"
    assert clean_date(f"mouray 2 {year}") is None

def test_year_rejected():
    year = 1959
    assert clean_date(f"15/02/{year}") is None
def test_other_year():
    year = 2024
    assert clean_date(f"31/02/{year}") is None
    assert clean_date(f"29/02/{year}") == "2024-02-29"
    assert clean_date(f"{year}-1-5") == "2024-01-05"

def test_other_year1():
    year = 2023
    assert clean_date(f"29/02/{year}") is None

def test_invalid_input():
    assert clean_date("N/A") is None
    assert clean_date(" ") is None
    assert clean_date("") is None