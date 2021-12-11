

class Dumbo:

    FLASH = 10

    def __init__(self, in_data):

        self._data = {(r, c): v for r, row in enumerate(in_data) for c, v in enumerate(row)}
        self.N = len(in_data)
        self.M = len(in_data[0])
        self._energy = 0
        self._epoch = 0

    def __str__(self):

        output = []
        for n in range(self.N):
            new_row = ''.join(str(self._data[(n, m)]) for m in range(self.M))
            output.append(new_row)
        return '\n'.join(output)

    def _increase(self):
        self._data = {k: v+1 for k, v in self._data.items()}

    def _cool_down(self):
        self._data = {k: v if v < self.FLASH else 0 for k, v in self._data.items()}

    def _flash(self):

        flashed = set()
        flashing = [k for k, v in self._data.items() if v >= self.FLASH and k not in flashed]

        while flashing:
            next_flash = flashing.pop()
            x, y = next_flash

            flashed.add(next_flash)
            neighbors = [(i, j) for i in range(x-1, x+2) if -1 < i < self.N for j in range(y-1, y+2) if -1 < j < self.M]

            for i, j in neighbors:
                self._data[(i, j)] += 1

            flashing = [k for k, v in self._data.items() if v >= self.FLASH and k not in flashed]

        self._energy += len(flashed)

    @property
    def energy(self):
        return self._energy

    @property
    def current_light(self):
        return sum(self._data.values())

    @property
    def age(self):
        return self._epoch

    def step(self):

        self._increase()
        self._flash()
        self._cool_down()

        self._epoch += 1


def solve(data):

    cave = Dumbo(data)

    while cave.current_light > 0:
        cave.step()

    return cave.age


def main():

    with open('input') as in_f:
        data = [list(map(int, row.strip())) for row in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
