from src.math import sum, sub

def test_add():
    assert sum(2, 3) == 5
    assert sum(3, 7) == 11

def test_sub():
    assert sub(-1, -2) == 1
    assert sub(7, 7) == 0


