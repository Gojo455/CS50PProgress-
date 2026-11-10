from fuel import extractor, unpack

def test_correct():
    assert extractor("2023-10-21") == (2023,10,21)
    assert extractor("03/10/2021") == (2021,10,3)
    assert extractor("December 7 2012") == (2012,12,7)



def test_var_with_space():
    assert extractor("2023-10-") == None
    assert extractor("03/10/") == None
    assert extractor("Decembers 7 2012") == None
    assert extractor("December 2012") == None



