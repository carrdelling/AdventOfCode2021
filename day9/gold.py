from itertools import product
from functools import reduce
from collections import Counter
import operator


def get_basins(data):

    max_x, max_y = len(data), len(data[0])

    def _ismin(_x, _y, v):
        left = _y - 1 < 0 or data[_x][_y - 1] > v
        right = _y + 1 >= max_y or data[_x][_y + 1] > v
        up = _x - 1 < 0 or data[_x - 1][_y] > v
        down = _x + 1 >= max_x or data[_x + 1][_y] > v

        return up and down and left and right

    return ((x, y) for x, y in product(range(max_x), range(max_y)) if _ismin(x, y, data[x][y]))


def solve(data):

    max_x, max_y = len(data), len(data[0])

    # tag basins and maximums
    surface = []
    for x in range(max_x):
        surface.append([0 if data[x][y] < 9 else -1 for y in range(max_y)])

    for idx, (x, y) in enumerate(get_basins(data), 1):
        surface[x][y] = idx

    # the flow, bro
    changed = True
    while changed:
        changed = False

        for x, y in product(range(max_x), range(max_y)):
            if surface[x][y] != 0:
                continue
            if x > 0 and surface[x-1][y] > 0:
                surface[x][y] = surface[x-1][y]
                changed = True
            if x < max_x - 1 and surface[x+1][y] > 0:
                surface[x][y] = surface[x+1][y]
                changed = True
            if y > 0 and surface[x][y-1] > 0:
                surface[x][y] = surface[x][y-1]
                changed = True
            if y < max_y - 1 and surface[x][y+1] > 0:
                surface[x][y] = surface[x][y+1]
                changed = True

    sizes = Counter(surface[x][y] for x, y in product(range(max_x), range(max_y)) if surface[x][y] != -1)

    return reduce(operator.mul, (x[1] for x in sizes.most_common(3)))


def main():

    with open('input') as in_f:
        data = [list(map(int, row.strip())) for row in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
