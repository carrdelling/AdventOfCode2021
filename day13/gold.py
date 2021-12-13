from collections import defaultdict


def print_grid(grid):

    max_x = max(x[0] for x in grid)+1
    max_y = max(x[1] for x in grid)+1

    # x and y are switched
    for y in range(max_y):
        row = []
        for x in range(max_x):
            row.append(grid[(x, y)])

        print(''.join(row))


def solve(data, folds):

    grid = defaultdict(lambda: '.')

    for x, y in data:
        grid[(x, y)] = '*'

    # all folds
    while folds:
        direction, point = folds.pop(0)

        new_grid = defaultdict(lambda: '.')

        if direction == 'x':
            for (x, y), v in grid.items():
                if x < point:
                    new_grid[(x, y)] = v
                if x > point:
                    real_x = point + point - x
                    new_grid[(real_x, y)] = v

        if direction == 'y':
            for (x, y), v in grid.items():
                if y < point:
                    new_grid[(x, y)] = v
                if y > point:
                    real_y = point + point - y
                    new_grid[(x, real_y)] = v

        # save the grid for next step
        grid = new_grid

    print_grid(grid)


def main():

    with open('input') as in_f:
        data = []
        fold = []

        for row in in_f:
            if 'fold' in row:
                if 'x' in row:
                    number = int(row.strip().split('=')[-1])
                    fold.append(('x', number))
                if 'y' in row:
                    number = int(row.strip().split('=')[-1])
                    fold.append(('y', number))
                continue
            if ',' in row:
                data.append(tuple(map(int, row.strip().split(','))))

    solve(data, fold)


if __name__ == "__main__":

    main()
