from collections import Counter


def solve(data):

    oxygen = list(data)

    step = 0
    while len(oxygen) > 1:
        keys = Counter(list(map(list, zip(*oxygen)))[step]).most_common()
        oxygen_key = '1' if keys[0][1] == keys[1][1] else str(keys[0][0])
        oxygen = [x for x in oxygen if x[step] == oxygen_key]
        step += 1
    oxygen_r = int("".join(oxygen[0]), 2)

    co2 = list(data)

    step = 0
    while len(co2) > 1:
        keys = Counter(list(map(list, zip(*co2)))[step]).most_common()
        co2_key = '0' if keys[0][1] == keys[1][1] else str(keys[1][0])
        co2 = [x for x in co2 if x[step] == co2_key]
        step += 1
    co2_r = int("".join(co2[0]), 2)

    return oxygen_r * co2_r


def main():

    with open('input') as in_f:
        data = [list(row.strip()) for row in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
