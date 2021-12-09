from itertools import product


def solve(data):

    max_x, max_y = len(data), len(data[0])

    def _ismin(_x, _y, v):

        left = _y-1 < 0 or data[_x][_y-1] > v
        right = _y+1 >= max_y or data[_x][_y+1] > v
        up = _x-1 < 0 or data[_x-1][_y] > v
        down = _x+1 >= max_x or data[_x+1][_y] > v

        return up and down and left and right

    return sum(data[x][y] + 1 for x, y in product(range(max_x), range(max_y)) if _ismin(x, y, data[x][y]))


def main():

    with open('input') as in_f:
        data = [list(map(int, row.strip())) for row in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
