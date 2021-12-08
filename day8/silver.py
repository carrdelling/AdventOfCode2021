

def solve(ins):

    return sum(1 if len(n) in {2, 3, 4, 7} else 0 for _, nn in ins for n in nn)


def main():

    with open('input') as in_f:
        data = []
        for row in in_f:
            signals, numbers = row.strip().split('|')
            data.append((signals.split(), numbers.split()))

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
