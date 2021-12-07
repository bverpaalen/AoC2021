from typing import TextIO
import numpy as np


def main() -> None:
    input_file = open("input.txt")
    crabs_x = readfile(input_file)
    x = np.median(crabs_x)
    fuel = calc_distance(crabs_x, x)
    print(f"Fuel used: {fuel}")


def readfile(input_file: TextIO) -> list:
    int_crabs_x = []
    str_crabs_x = input_file.read()[:-1].split(",")
    for crab_x in str_crabs_x:
        int_crabs_x.append(int(crab_x))
    return int_crabs_x


def calc_distance(crabs: list, x: int) -> int:
    fuel = 0
    for crab in crabs:
        difference = abs(x - crab)
        fuel += difference
    return fuel


main()
