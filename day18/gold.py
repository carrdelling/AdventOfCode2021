from itertools import product


def explode(n, level=0):
    # recursive! - return:
    # - The exploded number
    # - Flag exploded/not
    # - N to propagate left
    # - N to propagate right

    if isinstance(n, int):
        # just a number
        return n, False, 0, 0

    if level > 4:
        # level 5+ ???
        assert False, "Too many levels when exploding"

    elif level == 4:
        # base level - we need to explode it
        return 0, True, n[0], n[1]

    else:
        # first number of the pair, explode it
        exp_n, is_exploded, left, right = explode(n[0], level + 1)
        if is_exploded:
            # [n0, n1] ==> [exp0, n1 + right0]
            n = [exp_n, add_left(n[1], right)]
            return n, True, left, 0

        exp_n, is_exploded, left, right = explode(n[1], level + 1)
        if is_exploded:
            # [n0, n1] ==> [n0 + left1, exp1]
            n = [add_right(n[0], left), exp_n]
            return n, True, 0, right

        # nothing exploded so far in this branch
        return n, False, 0, 0


def add_right(n, a):
    return n + a if isinstance(n, int) else [n[0], add_right(n[1], a)]


def add_left(n, a):
    return n + a if isinstance(n, int) else [add_left(n[0], a), n[1]]


def split(n):
    # recursive! - return:
    # - The split number
    # - Flag split/not

    # split a number
    if isinstance(n, int):
        if n >= 10:
            l = n // 2
            r = l+1 if n % 2 == 1 else l
            return [l, r], True
        else:
            return n, False

    # split the left element
    split_left, is_split = split(n[0])
    if is_split:
        return [split_left, n[1]], is_split

    # split the right element
    split_right, is_split = split(n[1])
    return [n[0], split_right], is_split


def reduce_number(n):

    while True:

        # try to explode
        n, is_exploded, l, r = explode(n)

        # else try to split
        if not is_exploded:
            n, is_split = split(n)

            if not is_exploded and not is_split:
                break
    return n


def add(a, b):
    c = [a, b]
    return reduce_number(c)


def magnitude(n):
    return n if isinstance(n, int) else (3 * magnitude(n[0])) + (2 * magnitude(n[1]))


def solve(data):

    solution = max(magnitude(add(a, b)) for a, b in product(data, repeat=2) if a != b)

    return solution


def main():

    with open('input') as in_f:
        data = [eval(row) for row in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
