class Bingo:

    def __init__(self, size: int):
        self.size = size
        self.card = []*size
        self.has_bingo = False

        self.mask = []
        # Old: self.mask = [[0]*size]*size
        # To prevent same reference memory problem
        # TODO: find better work around
        for index_y in range(self.size):
            mask_row = []
            for index_x in range(self.size):
                mask_row.append(0)
            self.mask.append(mask_row)

    def print_card(self) -> None:
        print(self.card)

    def print_mask(self) -> None:
        print(self.mask)

    def add_row(self, row: list) -> None:
        new_row = []
        for number in row:
            new_row.append(int(number))
        row = new_row

        row_added = False
        for row_index in range(self.size):
            if not self.card[row_index]:
                self.card[row_index] = row
                row_added = True
                break

        if not row_added:
            print(f"Row not added: {row}")

    def has_number(self, number: int) -> None:
        number = int(number)

        has_bingo = False
        for row_index in range(self.size):
            for column_index in range(self.size):
                if self.card[row_index][column_index] == number:
                    self.mask[row_index][column_index] = 1

                    if self.row_has_bingo(row_index) or self.column_has_bingo(column_index):
                        has_bingo = True

        if has_bingo:
            self.has_bingo = True
            print("bingo!")
            self.print_card()
            self.print_mask()

    def row_has_bingo(self, row_index: int) -> bool:
        if sum(self.mask[row_index]) == self.size:
            return True
        else:
            return False

    def column_has_bingo(self, column_index: int) -> bool:
        column_masks = []
        for row_index in range(self.size):
            column_masks.append(self.mask[row_index][column_index])

        if sum(column_masks) == self.size:
            return True
        else:
            return False

    def row_sum(self, row_index: int) -> int:
        return sum(self.card[row_index])

    def column_sum(self, column_index: int) -> int:
        column_numbers = []
        for row_index in range(self.size):
            column_numbers.append(self.card[row_index][column_index])

        return sum(column_numbers)

    def winning_sums(self) -> dict:
        winnings_sums = {}
        for index in range(self.size):
            if self.row_has_bingo(index):
                winning_sum = self.row_sum(index)
                winnings_sums.update({f"row_{index}": winning_sum})
            if self.column_has_bingo(index):
                winning_sum = self.column_sum(index)
                winnings_sums.update({f"column_{index}": winning_sum})
        return winnings_sums

    def sum_unmarked(self) -> int:
        counter = 0
        for row_index in range(self.size):
            for column_index in range(self.size):
                if self.mask[row_index][column_index] == 0:
                    counter += self.card[row_index][column_index]
        return counter


if __name__ == '__main__':
    card = Bingo(9)
