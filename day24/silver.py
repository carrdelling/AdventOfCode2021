from itertools import product


def process_candidate(c):

    # step 1
    z = int(str(c)[0]) + 8

    # step 2
    z = (z * 26) + (int(str(c)[1]) + 13)

    # step 3
    z = (z * 26) + (int(str(c)[2]) + 2)

    # step 4
    z = z // 26

    # step 5
    z = (z * 26) + (int(str(c)[4]) + 11)

    # step 6
    z = (z * 26) + (int(str(c)[5]) + 4)

    # step 7
    z = (z * 26) + (int(str(c)[6]) + 13)

    # step 8
    z = (z // 26)

    return z


def search():

    # brute force, of course!
    # for all combinations of the three first digits (3rd must be 7 or less)
    for i1, i2, i3 in product(range(9, 0, -1), range(9, 0, -1), range(7, 0, -1)):
        i4 = i3 + 2
        v1 = i1 * 1000 + i2 * 100 + i3 * 10 + i4

        # for all combinations of the next three digits (3rd must be 4 or less)
        for i5, i6, i7 in product(range(9, 0, -1), range(9, 0, -1), range(4, 0, -1)):

            i8 = i7 + 5
            p2 = i5 * 1000 + i6 * 100 + i7 * 10 + i8
            v2 = v1 * 10000 + p2

            # process the 8 digit number
            z = process_candidate(v2)

            # step 9: modulo minus 9 must be a digit; keep it if good
            i9 = (z % 26) - 9
            if not 0 < i9 < 10:
                continue
            zz = z // 26

            # step 10: for every possible digit
            for i10 in range(9, 0, -1):
                z = (zz * 26) + (i10 + 1)

                # step 11: modulo must be a digit; keep it if good
                i11 = z % 26
                if not 0 < i11 < 10:
                    continue
                z = z // 26

                # step 12: modulo minus 5 must be a digit; keep it if good
                i12 = (z % 26) - 5
                if not 0 < i12 < 10:
                    continue
                z = z // 26

                # step 13: modulo minus 6 must be a digit; keep it if good
                i13 = (z % 26) - 6

                if not 0 < i13 < 10:
                    continue
                z = z // 26

                # step 14: : modulo minus 12 must be a digit; keep it if good
                i14 = (z % 26) - 12

                if not 0 < i14 < 10:
                    continue
                z = z // 26

                # z == 0 --> We found a solution, yay!
                if z == 0:
                    v = i1 * 1E13 + i2 * 1E12 + i3 * 1E11 + i4 * 1E10 + i5 * 1E9 + i6 * 1E8 + i7 * 1E7
                    v += i8 * 1E6 + i9 * 1E5 + i10 * 1E4 + i11 * 1E3 + i12 * 1E2 + i13 * 1E1 + i14
                    return int(v)


def main():

    solution = search()
    print(solution)


if __name__ == "__main__":

    main()
