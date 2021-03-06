from typing import TextIO
import numpy as np


def main(input_path: str = "input.txt") -> None:
    input_file = open(input_path)
    crabs_x = readfile(input_file)

    best_x, lowest_difference = brute_force_minimal_fuel(crabs_x)

    print()
    print(f"Horizontal line: {best_x}")
    print(f"Fuel used: {lowest_difference}")


def readfile(input_file: TextIO) -> list:
    int_crabs_x = []
    str_crabs_x = input_file.read().replace("\n", "").split(",")
    for crab_x in str_crabs_x:
        int_crabs_x.append(int(crab_x))
    return int_crabs_x


def calc_distance(crabs: list, x: int) -> int:
    fuel = 0
    for crab in crabs:
        difference = abs(x - crab)
        fuel += sum(range(1, int(difference)+1))
    return fuel


def brute_force_minimal_fuel(crabs_x: list) -> (int, int):
    lowest_difference = np.inf
    best_x = None

    min_crab = min(crabs_x)
    max_crab = max(crabs_x)

    for x in range(min_crab, max_crab):
        fuel = calc_distance(crabs_x, x)
        if fuel < lowest_difference:
            lowest_difference = fuel
            best_x = x
    return best_x, lowest_difference


if __name__ == '__main__':
    main()
