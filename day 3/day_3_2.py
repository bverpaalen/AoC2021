from typing import Callable, TextIO


def main(input_path: str = "input.txt"):
    input_file = open(input_path, 'r')

    bytes_list = read_bytes(input_file)

    oxygen_gen_byte = bit_criteria(bytes_list, common_bit)
    co2_scrub_byte = bit_criteria(bytes_list, uncommon_bit)

    oxygen_gen = int(oxygen_gen_byte, 2)
    co2_scrub = int(co2_scrub_byte, 2)

    print(f"Oxygen: {oxygen_gen}")
    print(f"CO2: {co2_scrub}")

    life_sup_rat = oxygen_gen * co2_scrub

    print(f"Life support rating: {life_sup_rat}")


def bit_criteria(bytes_list: list, criteria: Callable[[list, int], str]) -> str:
    pos = 0
    while len(bytes_list) > 1:
        c_bit = criteria(bytes_list, pos)

        new_bytes = []
        for byte in bytes_list:
            bit = byte[pos]
            if bit == c_bit:
                new_bytes.append(byte)
        bytes_list = new_bytes
        pos += 1
    return bytes_list[0]


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


def read_bytes(f: TextIO) -> list:
    list_bytes = []
    line = f.readline()
    while line:
        list_bytes.append(line)
        line = f.readline()
    return list_bytes


if __name__ == '__main__':
    main()
