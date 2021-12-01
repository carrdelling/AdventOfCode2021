

def solve(depths):

    return sum(1 if x < y else 0 for x, y in list(zip(depths, depths[1:])))


def main():

    with open('input_a') as in_f:
        data = [int(row.strip()) for row in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
