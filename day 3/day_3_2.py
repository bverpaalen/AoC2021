import _io
from typing import Callable


def main(input_path: str = "input.txt"):
    input_file = open(input_path, 'r')

    bytes = read_bytes(input_file)

    oxygen_gen_byte = bit_criteria(bytes, common_bit)
    co2_scrub_byte = bit_criteria(bytes, uncommon_bit)

    oxygen_gen = int(oxygen_gen_byte, 2)
    co2_scrub = int(co2_scrub_byte, 2)

    print(f"Oxygen: {oxygen_gen}")
    print(f"CO2: {co2_scrub}")

    life_sup_rat = oxygen_gen * co2_scrub

    print(f"Life support rating: {life_sup_rat}")


def bit_criteria(bytes: list, criteria: Callable[[list, int], str]) -> str:
    pos = 0
    while len(bytes) > 1:
        c_bit = criteria(bytes, pos)

        new_bytes = []
        for byte in bytes:
            bit = (byte)[pos]
            if bit == c_bit:
                new_bytes.append(byte)
        bytes = new_bytes
        pos += 1
    return bytes[0]


def bit_count(bytes_list: list, pos: int) -> dict:
    pos_count = {0: 0, 1: 0}
    for byte in bytes_list:
        bit = byte[pos]
        pos_count[int(bit)] += 1
    return pos_count


def common_bit(bytes_list: list, pos: int) -> str:
    pos_count = bit_count(bytes_list, pos)
    if pos_count[0] > pos_count[1]:
        return "0"
    else:
        return "1"


def uncommon_bit(bytes_list: list, pos: int) -> str:
    pos_count = bit_count(bytes_list, pos)
    if pos_count[0] <= pos_count[1]:
        return "0"
    else:
        return "1"


def read_bytes(f: _io.TextIOWrapper) -> list:
    bytes = []
    line = f.readline()
    while(line):
        bytes.append(line)
        line = f.readline()
    return bytes


if __name__ == '__main__':
    main()

