from bank import value

def test_hello():
    assert value("Hello") == 0
def test_h():
    assert value("How you doing") == 20
def test_else():
    assert value("what's good?") == 100
