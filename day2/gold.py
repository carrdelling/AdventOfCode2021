def solve(ins):

    a, h, d = [0] * 3

    for x, y in ins:
        v = int(y)
        a += {'up': -1, 'down': 1}.get(x, 0) * v
        h += {'forward': 1}.get(x, 0) * v
        d += {'forward': 1}.get(x, 0) * v * a

    return h * d


def main():

    with open('input') as in_f:
        data = [row.strip().split() for row in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()