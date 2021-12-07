import statistics


def solve(ins):

    m = int(statistics.median(ins))
    cost = sum(abs(x - m) for x in ins)

    return cost


def main():

    with open('input') as in_f:
        data = list(map(int, in_f.readline().strip().split(',')))

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
