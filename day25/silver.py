
def sim(data):

    size_x = max(x[0] for x in data) + 1
    size_y = max(x[1] for x in data) + 1

    # east first
    can_move = set()

    for (i, j), v in data.items():

        if v != '>':
            continue

        jj = (j+1) % size_y

        if data[(i, jj)] == '.':
            can_move.add((i, i, j, jj))

    for (i, ii, j, jj) in can_move:
        data[(i, j)] = '.'
        data[(ii, jj)] = '>'

    change = len(can_move) > 0

    # the south
    can_move = set()

    for (i, j), v in data.items():

        if v != 'v':
            continue

        ii = (i + 1) % size_x

        if data[(ii, j)] == '.':
            can_move.add((i, ii, j, j))

    for (i, ii, j, jj) in can_move:
        data[(i, j)] = '.'
        data[(ii, jj)] = 'v'

    change = change or (len(can_move) > 0)

    return change


def solve(data):

    steps = 1

    while sim(data):
        steps += 1
    print_map(data)

    return steps


def print_map(data):

    size_x = max(x[0] for x in data) + 1
    size_y = max(x[1] for x in data) + 1

    print('*' * size_y)
    for i in range(size_x):
        row = []
        for j in range(size_y):
            row.append(data[(i, j)])
        print(''.join(row))


def main():

    data = {}
    with open('input') as in_f:
        for i, row in enumerate(in_f):
            r = row.strip()
            for j, x in enumerate(r):
                data[(i, j)] = x

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
