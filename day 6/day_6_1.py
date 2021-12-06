from typing import TextIO
from lanternfish import Lanternfish


# Brute force method
def main() -> None:
    days = 80
    f = open("input.txt")
    ages = read_file(f)

    shoal = []
    for age in ages:
        lanternfish = Lanternfish(age)
        shoal.append(lanternfish)

    for day in range(days):
        n_shoal = []
        for lanternfish in shoal:
            baby = lanternfish.tick()
            n_shoal.append(lanternfish)
            if baby:
                n_shoal.append(baby)
        shoal = n_shoal
    num_fish = len(shoal)
    print(f"Lanternfish: {num_fish}")


def read_file(f: TextIO) -> list:
    int_ages = []
    str_ages = f.readlines()[0].replace("\n", "").split(",")
    for char in str_ages:
        int_ages.append(int(char))
    return int_ages


if __name__ == '__main__':
    main()
