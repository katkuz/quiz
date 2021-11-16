import pytest

from logic import calculate_correct_percent

def test_calculate_percent_negative_1():
    result = calculate_correct_percent(5, 1)
    assert result == -1

def test_calculate_percent_negative_2():
    result = calculate_correct_percent(11, 3)
    assert result == -1

def test_calculate_percent_zero_1():
    result = calculate_correct_percent(1, 0)
    assert result == -1

def test_calculate_percent_zero_2():
    result = calculate_correct_percent(0, 0)
    assert result == -1

def test_calculate_percent_zero_3():
    result = calculate_correct_percent(0, 1)
    assert result == 0

def test_calculate_percent_zero_4():
    result = calculate_correct_percent(0, 900)
    assert result == 0

def test_calculate_correct_percent_positive_1():
    result = calculate_correct_percent(1, 5)
    assert result == 20

def test_calculate_correct_percent_positive_2():
    result = calculate_correct_percent(150, 1000)
    assert result == 15

def test_calculate_correct_percent_positive_3():
    result = calculate_correct_percent(150, 999)
    assert result == 15

