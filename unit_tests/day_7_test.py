import pytest
from typing import cast, TextIO

from days.day_7 import day_7_1 as d1
from days.day_7 import day_7_2 as d2

test_crabs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


@pytest.fixture
def nothing():
    d1.main("../days/day_7/input.txt")
    d2.main("../days/day_7/input.txt")


def test_readfile():
    test_file = cast(TextIO, MockTextIO)
    d1_result = d1.readfile(test_file)
    d2_result = d2.readfile(test_file)

    assert d1_result == test_crabs and d2_result == test_crabs


def test_d1_calc_distance():
    answer = 37

    test_x = 2

    result = d1.calc_distance(test_crabs, test_x)
    assert result == answer


def test_d2_calc_distance():
    answer = 168

    test_x = 5

    result = d2.calc_distance(test_crabs, test_x)
    assert result == answer


class MockTextIO:

    @staticmethod
    def read():
        return "16,1,2,0,4,2,7,1,2,14\n"
