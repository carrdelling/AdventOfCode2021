from collections import defaultdict, Counter


DIRAC = [3, 4, 5,
         4, 5, 6,
         5, 6, 7,
         4, 5, 6,
         5, 6, 7,
         6, 7, 8,
         5, 6, 7,
         6, 7, 8,
         7, 8, 9]

POS = Counter(DIRAC).items()

TARGET = 21


def solve(data):

    pos_a, pos_b = data

    wins = {'a': 0, 'b': 0}
    states = {(pos_a, 0, pos_b, 0): 1}

    while sum(states.values()) > 0:

        new_states = defaultdict(int)

        for (pos_a, score_a, pos_b, score_b), pre_universes in states.items():
            for roll, universes in POS:

                new_pos = (pos_a + roll) % 10
                new_pos = 10 if new_pos == 0 else new_pos
                new_score = score_a + new_pos

                if new_score >= TARGET:
                    wins['a'] += pre_universes * universes
                else:
                    s = (new_pos, new_score, pos_b, score_b)
                    new_states[s] += pre_universes * universes

        states = new_states.copy()
        new_states = defaultdict(int)

        for (pos_a, score_a, pos_b, score_b), pre_universes in states.items():
            for roll, universes in POS:

                new_pos = (pos_b + roll) % 10
                new_pos = 10 if new_pos == 0 else new_pos
                new_score = score_b + new_pos

                if new_score >= TARGET:
                    wins['b'] += pre_universes * universes
                else:
                    s = (pos_a, score_a, new_pos, new_score)
                    new_states[s] += pre_universes * universes

        states = new_states.copy()

    return max(wins.values())


def main():

    with open('input') as in_f:
        data = []
        for row in in_f:
            pos = int(row.strip().split(': ')[-1])
            data.append(pos)

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
