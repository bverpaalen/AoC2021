from matrix import Matrix
from typing import TextIO


def main():
    input_path = "input.txt"
    input_file = open(input_path, 'r')

    field = Matrix(1000)

    commands = read_file(input_file)

    for command in commands:
        source = command[0]
        target = command[1]

        field.horizontal_row(source, target)
        field.vertical_row(source, target)

    result = field.count_min_x(2)
    print(f"Results: {result}")


def read_file(f: TextIO):
    line = f.readline()
    commands = []
    while line:
        source, target = line.split(" -> ")
        source_x, source_y = source.split(",")
        target_x, target_y = target.split(",")

        new_source = (int(source_x), int(source_y))
        new_target = (int(target_x), int(target_y))

        commands.append((new_source, new_target))
        line = f.readline()
    return commands


if __name__ == '__main__':
    main()