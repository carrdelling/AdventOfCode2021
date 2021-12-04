

class Bingo:

    def __init__(self, raw_data):

        self.rows = []
        self.cols = []

        data = [line.split() for line in raw_data]

        self.rows = [set(r) for r in data]
        data_t = list(map(list, zip(*data)))
        self.cols = [set(r) for r in data_t]

    def __str__(self):
        return f"BINGO with rows {self.rows} and cols {self.cols}"

    def _score(self, n):
        return sum(sum(map(int, r)) for r in self.rows) * int(n)

    def number(self, n):

        for i in range(len(self.rows)):

            # win in rows?
            self.rows[i].discard(n)
            if len(self.rows[i]) < 1:
                return self._score(n)

            # win in cols?
            self.cols[i].discard(n)
            if len(self.cols[i]) < 1:
                return self._score(n)

        return -1


def solve(numbers, boards):

    for n in numbers:
        for board in boards:
            solution = board.number(n)

            if solution > -1:
                return solution


def main():

    with open('input') as in_f:
        sequence = in_f.readline().strip().split(',')
        in_f.readline()

        buffer = []
        boards = []
        for row in in_f:
            if len(row) > 2:
                buffer.append(row.strip())
            else:
                board = Bingo(buffer)
                boards.append(board)
                buffer = []

    solution = solve(sequence, boards)

    print(solution)


if __name__ == "__main__":

    main()
