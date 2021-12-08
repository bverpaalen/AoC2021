from typing import TextIO
import json


def main(to_count: list, input_path: str = "input.txt", display_path: str = "./display_lengths") -> int:
    display = json.load(open(display_path))

    number_length = {}
    for number in to_count:
        display_set = display[str(number)]
        number_length.update({len(display_set): number})

    f = open(input_path)
    rows = read_file(f)

    total_counter = 0
    for row in rows:
        identifications, output = row
        temp_counter = count_length_based(list(number_length.keys()), output)
        total_counter += temp_counter

    print(total_counter)
    return total_counter


def read_file(f: TextIO) -> list:
    rows = []

    line = f.readline()
    while line:
        line_identification, line_output = line.replace("\n", "").split(" | ")

        split_id = line_identification.split(" ")
        outputs = line_output.split(" ")
        rows.append((split_id, outputs))
        line = f.readline()
    return rows


def find_number_combination(identifications: list, number_length: dict):
    identifier = {}
    for identification in identifications:
        if len(identification) in number_length.keys():
            identifier.update({identification: number_length[len(identification)]})
    return identifier


def count_length_based(number_combination: list, output: list) -> int:
    counter = 0
    for signal in output:
        if len(signal) in number_combination:
            counter += 1
    return counter


if __name__ == '__main__':
    main([1, 4, 7, 8], "input.txt")
