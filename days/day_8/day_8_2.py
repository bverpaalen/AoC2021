from typing import TextIO
import json


def main(can_count=None, input_path: str = "input.txt", display_path: str = "./display_lengths") -> int:
    if can_count is None:
        can_count = [1, 4, 7, 8]

    display_segments = json.load(open(display_path))

    reverse_number_length = {}
    number_length = {}
    for number in range(0, 10):
        display_set = display_segments[str(number)]
        if number in can_count:
            number_length.update({len(display_set): number})
        reverse_number_length.update({number: len(display_set)})

    str_display_segments = {}
    for display_value in display_segments.keys():
        display_str = ""
        for chars in display_segments[display_value]:
            display_str += chars[0]
        display_str = "".join(sorted(display_str))
        str_display_segments.update({display_value: display_str})

    f = open(input_path)
    rows = read_file(f)

    sum_output_number = 0
    for row in rows:
        identifications, output = row

        coding = extract_coding(identifications, number_length)

        output_number = ""
        for signal in output:
            sorted_signal = "".join(sorted(signal))
            number = coding[sorted_signal]
            output_number += str(number)
        output_number = int(output_number)
        sum_output_number += output_number
    print(sum_output_number)
    return sum_output_number


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


def extract_coding(identifications: list, number_length: dict) -> dict:
    compare = {}
    for identification in identifications:
        if len(identification) in number_length.keys():
            display_number = number_length[len(identification)]
            compare.update({display_number: identification})

    segments_n_6 = segments_with_length_n(identifications, 6)

    for segment in segments_n_6:
        if all_of_a_in_b(compare[4], segment):
            compare[9] = segment
        elif all_of_a_in_b(compare[1], segment):
            compare[0] = segment
        else:
            compare[6] = segment

    segments_n_5 = segments_with_length_n(identifications, 5)

    for segment in segments_n_5:
        if all_of_a_in_b(compare[1], segment):
            compare[3] = segment
        elif len(remove_b_from_a(compare[6], segment)) == 1:
            compare[5] = segment
        else:
            compare[2] = segment

    reverse_sorted_compare = {}
    for key in compare.keys():
        value = compare[key]
        value = "".join(sorted(value))
        reverse_sorted_compare.update({value: key})
    return reverse_sorted_compare


def remove_b_from_a(a: str, b: str) -> str:
    to_keep = ""
    for char in a:
        if char not in b:
            to_keep += char
    return to_keep


def all_of_a_in_b(a: str, b: str) -> bool:
    overlap = True
    for char in a:
        if char not in b:
            overlap = False
    return overlap


def segments_with_length_n(identifications: list, n: int) -> list:
    n_identifications = []
    for identification in identifications:
        if len(identification) == n:
            n_identifications.append(identification)
    return n_identifications


if __name__ == '__main__':
    main(input_path="input.txt")
