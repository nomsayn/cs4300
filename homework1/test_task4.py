import pytest
import task4

# the test function will need the expected result to be calculated before the test
def test_calculate_discount():
    assert task4.calculate_discount(100, 20) == 80.0
    assert task4.calculate_discount(50, 50) == 25.0
    assert task4.calculate_discount(449.99, 15) == 382.49
    assert task4.calculate_discount(0, 90) == 0.0
    assert task4.calculate_discount(1800, 15) == 1530.0
    assert task4.calculate_discount(9000, 100) == 0.0


def test_calculate_discount_invalid_values():
    # From Python docs: The with statement is used to wrap the execution of a block
    #   with methods defined by a context manager (see section With Statement Context Managers).
    #   This allows common try...except...finally usage patterns to be encapsulated for convenient reuse.
    with pytest.raises(ValueError):
        task4.calculate_discount(-100, 20)
    with pytest.raises(ValueError):
        task4.calculate_discount(100, -10)

    with pytest.raises(ValueError):
        task4.calculate_discount(100, 110)

    with pytest.raises(ValueError):
        task4.calculate_discount("100", 10)

    with pytest.raises(ValueError):
        task4.calculate_discount(100, "10")

