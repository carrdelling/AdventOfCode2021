import statistics


def solve(ins):

    m = int(statistics.mean(ins))
    cost = sum(
        (abs(x - m) + 1) * abs(x - m)
        / 2
        for x in ins)

    return int(cost)


def main():

    with open('input') as in_f:
        data = list(map(int, in_f.readline().strip().split(',')))

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
