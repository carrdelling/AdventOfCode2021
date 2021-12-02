from itertools import groupby


def solve(ins):

    a = [sum(int(yy) for _, yy in y) for _, y in groupby(sorted(ins), lambda x: x[0])]
    return (a[0] - a[-1]) * a[1]


def main():

    with open('input') as in_f:
        data = [row.strip().split() for row in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()