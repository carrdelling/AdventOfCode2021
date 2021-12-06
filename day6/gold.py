from collections import Counter


def solve(ins):

    state = Counter(ins)

    for _ in range(256):
        current = sorted(state.items(), reverse=True)
        state.clear()
        for t, c in current:
            if t > 0:
                state[t-1] = c
            else:
                state[8] = c
                state[6] += c

    return sum(state.values())


def main():

    with open('input') as in_f:
        data = list(map(int, in_f.readline().strip().split(',')))

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
