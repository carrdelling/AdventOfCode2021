
TARGET = 1000
ROLLS_TURN = 3


def dtd100():

    current = 1
    while True:
        yield current
        current += 1 if current < 100 else -99


dice = dtd100()


def throw():
    return sum(next(dice) for _ in range(ROLLS_TURN))


def solve(data):

    a, b = data
    a_score = 0
    b_score = 0
    turns = 0

    while a_score < TARGET and b_score < TARGET:
        a += throw()
        turns += 1
        a = a % 10
        a = 10 if a == 0 else a
        a_score += a

        if a_score >= TARGET:
            break

        b += throw()
        turns += 1
        b = b % 10
        b = 10 if b == 0 else b
        b_score += b

    rolls = turns * ROLLS_TURN
    losing_score = min(a_score, b_score)

    return rolls * losing_score


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
