from collections import Counter
from math import ceil

STEPS = 10


def solve(reactions, polimer):

    pairs = Counter((a, b) for a, b in zip(polimer, polimer[1:]))

    for STEP in range(STEPS):
        new_pairs = Counter()
        for (a, b), count in pairs.items():
            react = reactions[a+b]
            new_pairs[a, react] += count
            new_pairs[react, b] += count
        else:
            pairs = new_pairs
    else:
        elements = Counter()
        for (a, b), count in pairs.items():
            elements[a] += count
            elements[b] += count

    counts = sorted(elements.items(), key=lambda x: -x[1])

    return ceil(counts[0][1]/2) - ceil(counts[-1][1]/2)


def main():

    with open('input') as in_f:
        polimer = in_f.readline().strip()
        data = [row.strip().split(' -> ') for row in in_f if len(row) > 1]
        reactions = {x: y for x, y in data}

    solution = solve(reactions, polimer)

    print(solution)


if __name__ == "__main__":

    main()
