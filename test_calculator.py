import pytest
import calculator

def test_square_root():
    assert calculator.square_root(9) == 3
    assert calculator.square_root(16) == 4
    assert calculator.square_root(25) == 5
    with pytest.raises(ValueError):  # Negative test case
        calculator.square_root(-4)

def test_factorial():
    assert calculator.factorial(5) == 120
    assert calculator.factorial(0) == 1
    assert calculator.factorial(3) == 6
    with pytest.raises(ValueError):  # Negative test case
        calculator.factorial(-3)

def test_natural_log():
    assert round(calculator.natural_log(1), 2) == 0.00
    assert round(calculator.natural_log(2.718), 2) == 1.00
    assert round(calculator.natural_log(10), 2) == 2.30
    with pytest.raises(ValueError):  # Negative test case
        calculator.natural_log(0)
    with pytest.raises(ValueError):
        calculator.natural_log(-1)

def test_power():
    assert calculator.power(2, 3) == 8
    assert calculator.power(5, 0) == 1
    assert calculator.power(3, 2) == 9
    with pytest.raises(ValueError):  # Negative base with fractional exponent
        calculator.power(-4, 0.5)

if __name__ == "__main__":
    pytest.main()

