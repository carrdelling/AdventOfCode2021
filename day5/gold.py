
MAX = 1000


def solve(data):

    ocean = [[0] * MAX for _ in range(MAX)]

    for (x1, y1), (x2, y2) in data:

        if x1 == x2:
            a, b = min(y1, y2), max(y1, y2)
            for i in range(a, b+1):
                ocean[x1][i] += 1
            continue

        if y1 == y2:
            a, b = min(x1, x2), max(x1, x2)
            for i in range(a, b+1):
                ocean[i][y1] += 1
            continue

        # diagonals
        x_change = 1 if x1 < x2 else -1
        y_change = 1 if y1 < y2 else -1
        steps = abs(x1 - x2)

        for i in range(steps+1):
            ocean[x1+(i*x_change)][y1+(i*y_change)] += 1

    dangerous = sum(1 if x > 1 else 0 for row in ocean for x in row)

    return dangerous


def main():

    def _point(s):
        return tuple(map(int, s.split(',')))

    with open('input') as in_f:
        data = [(_point(x), _point(y)) for x, y in [list(row.strip().split(' -> ')) for row in in_f]]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
