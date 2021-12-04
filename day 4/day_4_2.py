from typing import TextIO

from bingo_card import Bingo


def main():
    input_path = "input.txt"
    input_file = open(input_path, 'r')

    drawn, bingo_cards = read_file(input_file)
    last_bingo, last_number = play_bingo(drawn, bingo_cards)

    unmarked_sum = last_bingo.sum_unmarked()

    print(f"Last number: {last_number}")
    print(f"Unmarked sum: {unmarked_sum}")
    answer = int(last_number) * int(unmarked_sum)
    print(f"Answer: {answer}")


def read_file(input_file: TextIO, size: int = 5) -> (list, list):
    bingo_cards = []
    line = input_file.readline()
    drawn = line.split(",")

    line = input_file.readline()

    bingo = None
    while line:
        if line == "\n" and not bingo:
            bingo = Bingo(size)
        elif line == "\n":
            bingo_cards.append(bingo)
            bingo = Bingo(size)
        else:
            row = read_row(line)
            bingo.add_row(row)
        line = input_file.readline()

    return drawn, bingo_cards


def read_row(line: str) -> list:
    row = []
    line = line.replace("\n", "")

    current_num = ""
    for char in line:
        if char != " ":
            current_num += char
        elif char == " ":
            if current_num != "":
                row.append(current_num)
                current_num = ""
    row.append(current_num)
    return row


def play_bingo(drawn: list, bingo_cards: list) -> (list, int):
    not_winners = bingo_cards
    i = -1
    winners = []
    number = None
    while len(not_winners) > 0:
        i += 1
        number = drawn[i]
        print(f"Number drawn: {number}")

        new_not_winners = []
        for index in range(len(not_winners)):
            bingo = not_winners[index]
            bingo.has_number(number)

            if not bingo.has_bingo:
                new_not_winners.append(bingo)
            else:
                winners.append(bingo)

        not_winners = new_not_winners
    last_bingo = winners[-1]
    return last_bingo, number


if __name__ == '__main__':
    main()
