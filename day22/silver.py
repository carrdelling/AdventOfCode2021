from collections import Counter

MAX_V = 50
MIN_V = -50


def intercept(a, b):

    ixl = max(a[0], b[0])
    ixh = min(a[1], b[1])
    iyl = max(a[2], b[2])
    iyh = min(a[3], b[3])
    izl = max(a[4], b[4])
    izh = min(a[5], b[5])

    if all([(ixl <= ixh), (iyl <= iyh), (izl <= izh)]):
        return ixl, ixh, iyl, iyh, izl, izh
    return None


def solve(ins):

    cubes = Counter()

    for m, (xl, xh), (yl, yh), (zl, zh) in ins:
        key = (xl, xh, yl, yh, zl, zh)

        # reverse everything intercepted by the new one
        intercepts = Counter()

        for inner_cube, v in cubes.items():
            ki = intercept(key, inner_cube)
            if ki is not None:
                intercepts[ki] -= v

        cubes.update(intercepts)
        # light on the new cube if positive
        if m:
            cubes[key] += 1

    # add all the intercepts
    solution = 0
    for (xl, xh, yl, yh, zl, zh), v in cubes.items():
        sxl = max(xl, MIN_V)
        sxh = min(xh, MAX_V)
        syl = max(yl, MIN_V)
        syh = min(yh, MAX_V)
        szl = max(zl, MIN_V)
        szh = min(zh, MAX_V)
        if all([(sxl <= sxh), (syl <= syh), (szl <= szh)]):
            size = (sxh - sxl + 1) * (syh - syl + 1) * (szh - szl + 1)
            solution += size * v

    return solution


def main():

    with open('input') as in_f:
        data = []
        for row in in_f:
            tags = row.strip().split()
            command = [tags[0] == "on"]
            tags = tags[1].split(',')

            for i in range(3):
                l, h = map(int, tags[i].split('=')[-1].split('..'))
                command.append((l, h))
            data.append(command)

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
