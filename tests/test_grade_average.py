import pytest
from grade_average import calculate_average


def test_two_marks_returns_average():
    #arrange
    mark_one = 80
    mark_two = 90
    #act
    result = calculate_average(mark_one, mark_two)
    #assert
    assert result == 85


def test_50_and_51_returns_50_5():
    #arrange
    mark_one = 50
    mark_two = 51
    #act
    result = calculate_average(mark_one, mark_two)
    #assert
    assert result == 50.5


def test_zero_marks_returns_zero():
    #arrange
    mark_one = 0
    mark_two = 0
    #act
    result = calculate_average(mark_one, mark_two)
    #assert
    assert result == 0


def test_100_marks_returns_100():
    #arrange
    mark_one = 100
    mark_two = 100
    #act
    result = calculate_average(mark_one, mark_two)
    #assert
    assert result == 100


def test_60_and_80_returns_70():
    #arrange
    mark_one = 60
    mark_two = 80
    #act
    result = calculate_average(mark_one, mark_two)
    #assert
    assert result == 70


def test_first_mark_as_string_raises_type_error():
    with pytest.raises(TypeError):
        calculate_average("50", 60)


def test_second_mark_as_string_raises_type_error():
    with pytest.raises(TypeError):
        calculate_average(50, "60")


def test_first_mark_as_float_raises_type_error():
    with pytest.raises(TypeError):
        calculate_average(50.5, 60)


def test_second_mark_as_float_raises_type_error():
    with pytest.raises(TypeError):
        calculate_average(50, 60.5)


def test_first_mark_as_boolean_raises_type_error():
    with pytest.raises(TypeError):
        calculate_average(True, 60)


def test_second_mark_as_boolean_raises_type_error():
    with pytest.raises(TypeError):
        calculate_average(50, False)


def test_first_mark_as_none_raises_type_error():
    with pytest.raises(TypeError):
        calculate_average(None, 60)


def test_second_mark_as_none_raises_type_error():
    with pytest.raises(TypeError):
        calculate_average(50, None)


def test_first_mark_below_zero_raises_value_error():
    with pytest.raises(ValueError):
        calculate_average(-1, 60)


def test_second_mark_below_zero_raises_value_error():
    with pytest.raises(ValueError):
        calculate_average(50, -1)


def test_first_mark_above_100_raises_value_error():
    with pytest.raises(ValueError):
        calculate_average(101, 60)


def test_second_mark_above_100_raises_value_error():
    with pytest.raises(ValueError):
        calculate_average(50, 101)
