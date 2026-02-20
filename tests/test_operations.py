import pytest
from app.operations import add, subtract, multiply, divide, power, root
from app.exceptions import DivisionByZeroError

@pytest.mark.parametrize("a, b, expected", [
    (5, 5, 10), (-2, 3, 1), (0, 0, 0),
    (2.5, 2.5, 5.0), (-5.5, -4.5, -10.0), (1000000, 2000000, 3000000)
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 5), (0, 5, -5), (-5, -5, 0),
    (5.5, 2.2, 3.3)
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == pytest.approx(expected)

@pytest.mark.parametrize("a, b, expected", [
    (5, 5, 25), (10, 0, 0), (-2, 3, -6),
    (1.5, 2.0, 3.0), (-0.5, -0.5, 0.25)
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5), (5, 2, 2.5), (-10, 2, -5),
    (1, 3, 0.3333333333333333), (-5.5, 1.1, -5.0)
])
def test_divide(a, b, expected):
    assert divide(a, b) == pytest.approx(expected)

@pytest.mark.parametrize("a, b", [(10, 0), (5.5, 0), (0, 0)])
def test_divide_by_zero(a, b):
    with pytest.raises(DivisionByZeroError):
        divide(a, b)

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 8), (5, 0, 1), (9, 0.5, 3),
    (2, -1, 0.5), (-2, 3, -8)
])
def test_power(a, b, expected):
    assert power(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (8, 3, 2), (9, 2, 3), (6.25, 2, 2.5)
])
def test_root(a, b, expected):
    assert root(a, b) == expected

@pytest.mark.parametrize("a, b", [(10, 0), (5, 0.0)])
def test_root_by_zero(a, b):
    with pytest.raises(DivisionByZeroError):
        root(a, b)