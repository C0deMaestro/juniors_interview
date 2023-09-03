import pytest
from solution import sum_two, divide, concat_strings, logical_and

# Тесты для sum_two
def test_sum_two():
    result = sum_two(1, 2)
    assert result == 3

    with pytest.raises(TypeError):
        sum_two(1, 2.4)

# Тесты для divide
def test_divide():
    result = divide(6.0, 2.0)
    assert result == 3.0

    with pytest.raises(TypeError):
        divide(6.0, '2.0')

# Тесты для concat_strings
def test_concat_strings():
    result = concat_strings("Hello, ", "world!")
    assert result == "Hello, world!"

    with pytest.raises(TypeError):
        concat_strings("Hello, ", 42)

# Тесты для logical_and
def test_logical_and():
    result = logical_and(True, False)
    assert result is False

    with pytest.raises(TypeError):
        logical_and(True, 1)
