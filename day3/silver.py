from collections import Counter


def solve(data):

    gamma_s = "".join(Counter(c).most_common(1)[0][0] for c in list(map(list, zip(*data))))
    return (int(gamma_s, 2)) * (int(gamma_s, 2) ^ int('1' * len(gamma_s), 2))


def main():

    with open('input') as in_f:
        data = [list(row.strip()) for row in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
