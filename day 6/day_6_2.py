from typing import TextIO
from copy import deepcopy


# Smarter method
def main():
    days = 256
    max_age = 8
    f = open("input.txt")
    ages = read_file(f)
    fish_counter = {}

    for day in range(max_age + 1):
        fish_counter.update({day: 0})

    for age in ages:
        fish_counter[age] += 1

    shoal = loop(fish_counter, days, max_age)
    print(f"Lanternfish: {shoal}")


def loop(fish_counter, days, max_age):
    n_fish_counter = {}

    for day in range(max_age + 1):
        n_fish_counter.update({day: 0})

    for day in range(days):
        n_fish_counter[6] = fish_counter[0] + fish_counter[7]
        n_fish_counter[8] = fish_counter[0]

        for n_fish in range(1, max_age + 1):
            if n_fish != 7:
                n_fish_counter[n_fish - 1] = fish_counter[n_fish]

        fish_counter = deepcopy(n_fish_counter)

    end_shoal = sum(fish_counter.values())
    return end_shoal


def read_file(f: TextIO) -> list:
    int_ages = []
    str_ages = f.readlines()[0].replace("\n", "").split(",")
    for char in str_ages:
        int_ages.append(int(char))
    return int_ages


if __name__ == '__main__':
    main()
