import pytest
from grade_pass import has_passed


def test_score_49_returns_false():
    #arrange
    score = 49
    #act
    result = has_passed(score)
    #assert
    assert result is False


def test_score_50_returns_true():
    #arrange
    score = 50
    #act
    result = has_passed(score)
    #assert
    assert result is True


def test_score_51_returns_true():
    #arrange
    score = 51
    #act
    result = has_passed(score)
    #assert
    assert result is True


def test_score_0_returns_false():
    #arrange
    score = 0
    #act
    result = has_passed(score)
    #assert
    assert result is False


def test_score_100_returns_true():
    #arrange
    score = 100
    #act
    result = has_passed(score)
    #assert
    assert result is True


def test_string_score_raises_error():
    with pytest.raises(TypeError):
        has_passed("50")


def test_float_score_raises_error():
    with pytest.raises(TypeError):
        has_passed(50.5)


def test_boolean_score_raises_error():
    with pytest.raises(TypeError):
        has_passed(True)


def test_none_score_raises_error():
    with pytest.raises(TypeError):
        has_passed(None)


def test_negative_score_raises_error():
    with pytest.raises(ValueError):
        has_passed(-1)


def test_score_above_100_raises_error():
    with pytest.raises(ValueError):
        has_passed(101)
