from calculator import add, subtract

def test_add():
    assert add(5, 5) == 10
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -5
