import pytest

def multiply(a, b):
    if a == 5:
        raise Exception('MyException')
    return a * b

def test_1x1():
    assert multiply(1, 1) == 1

def test_2x2():
    assert multiply(2, 2) == 4

def test_3x3():
    assert multiply(3, 3) == 9

def test_exception():
    with pytest.raises(Exception):
        multiply(5, 1)
