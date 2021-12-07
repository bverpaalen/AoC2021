from typing import cast, TextIO

from days.day_7 import day_7_1 as d1
from days.day_7 import day_7_2 as d2

test_crabs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def test_d1_d2_readfile():
    answer = test_crabs

    test_file = cast(TextIO, MockTextIO)

    result_d1 = d1.readfile(test_file)
    result_d2 = d2.readfile(test_file)

    assert result_d1 == answer and result_d2 == answer


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


def test_brute_d2_force_minimal_fuel():
    answer_x = 5
    answer_fuel = 168

    result_x, result_fuel = d2.brute_force_minimal_fuel(test_crabs)

    assert answer_x == result_x and result_fuel == answer_fuel


class MockTextIO:

    @staticmethod
    def read():
        return "16,1,2,0,4,2,7,1,2,14\n"
