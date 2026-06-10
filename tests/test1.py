from src import add,sub



def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-2, -3) == -5


def test_add_zero():
    assert add(10, 0) == 10


def test_add_float_values():
    assert add(2.5, 1.5) == 4.0


def test_sub_positive_numbers():
    assert sub(10, 4) == 6


def test_sub_negative_numbers():
    assert sub(-5, -2) == -3


def test_sub_zero():
    assert sub(10, 0) == 10


def test_sub_float_values():
    assert sub(5.5, 2.0) == 3.5