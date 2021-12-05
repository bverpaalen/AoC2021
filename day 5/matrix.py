class Matrix:

    def __init__(self, size: int) -> None:
        self.size = size
        self.field = []

        for row_index in range(size):
            row = []
            for column_index in range(size):
                row.append(0)
            self.field.append(row)

    def print_field(self) -> None:
        for row_index in range(self.size):
            print(self.field[row_index])

    def row(self, source: tuple, target:tuple) -> bool:
        source_x, source_y = source
        target_x, target_y = target

        if source_x == target_x:
            return self.vertical_row(source, target)
        elif source_y == target_y:
            return self.horizontal_row(source, target)
        else:
            return self.diagonal_row(source, target)

    def vertical_row(self, source: tuple, target: tuple) -> bool:
        source_x, source_y = source
        target_x, target_y = target

        if source_x != target_x:
            return False

        difference = target_y - source_y

        if difference > 0:
            difference += 1
            for index in range(difference):
                self.field[source_y + index][source_x] += 1
            return True
        elif difference < 0:
            difference -= 1
            for index in range(difference * -1):
                self.field[source_y - index][source_x] += 1
            return True
        elif difference == 0:
            self.field[source_y][source_x] += 1
            return True

    def horizontal_row(self, source: tuple, target: tuple) -> bool:
        source_x, source_y = source
        target_x, target_y = target

        if source_y != target_y:
            return False

        row = self.field[source_y]

        difference = target_x - source_x

        if difference > 0:
            difference += 1
            for index in range(difference):
                row[source_x + index] += 1
            return True
        elif difference < 0:
            difference -= 1
            for index in range(difference * -1):
                row[source_x - index] += 1
            return True
        elif difference == 0:
            row[source_x] += 1
            return True

    def diagonal_row(self, source: tuple, target:tuple) -> bool:
        source_x, source_y = source
        target_x, target_y = target

        difference_x = target_x - source_x
        difference_y = target_y - source_y

        if not (source_x == target_x or source_y or target_y) or (abs(difference_x) != abs(difference_y)):
            return False

        if difference_x < 0:
            x_negative = -1
        else:
            x_negative = 1

        if difference_y < 0:
            y_negative = -1
        else:
            y_negative = 1

        for index in range(abs(difference_x)+1):
            x = source_x + index * x_negative
            y = source_y + index * y_negative

            self.field[y][x] += 1
        return True

    def count_min_x(self, x: int) -> int:
        counter = 0
        for row_index in range(self.size):
            for column_index in range(self.size):
                if self.field[row_index][column_index] >= x:
                    counter += 1
        return counter
