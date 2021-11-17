from logic import calculate_correct_percent, count_points


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


def test_count_points_negative_1():
    result = count_points(-1)
    assert result == 0


def test_count_points_positive_1():
    result = count_points(0)
    assert result == 5


def test_count_points_positive_2():
    result = count_points(1)
    assert result == 5


def test_count_points_positive_3():
    result = count_points(10)
    assert result == 5


def test_count_points_positive_4():
    result = count_points(11)
    assert result == 4


def test_count_points_positive_5():
    result = count_points(20)
    assert result == 4


def test_count_points_positive_6():
    result = count_points(21)
    assert result == 3


def test_count_points_positive_7():
    result = count_points(30)
    assert result == 3


def test_count_points_positive_8():
    result = count_points(31)
    assert result == 2


def test_count_points_positive_9():
    result = count_points(40)
    assert result == 2


def test_count_points_positive_10():
    result = count_points(1000)
    assert result == 1
