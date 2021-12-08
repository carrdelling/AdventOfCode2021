from collections import Counter


def solve(ins):

    solution = 0
    for wires, numbers in ins:

        two = [x for x in wires if len(x) == 2]
        three = [x for x in wires if len(x) == 3]
        four = [x for x in wires if len(x) == 4]
        five = [x for x in wires if len(x) == 5]
        six = [x for x in wires if len(x) == 6]
        seven = [x for x in wires if len(x) == 7]

        up_s = set(three[0]) - set(two[0])
        horizontals = set(five[0]) & set(five[1]) & set(five[2])
        mid_s = horizontals & set(four[0])
        down_s = horizontals - up_s - mid_s
        up_w, mid_w, down_w = up_s.pop(), mid_s.pop(), down_s.pop(),

        right = set(two[0])
        left = set(seven[0]) - horizontals - right

        up_left_s = left & set(four[0])
        down_left_s = left - up_left_s
        up_left_w, down_left_w = up_left_s.pop(), down_left_s.pop()

        c_right = Counter(x for w in six for x in w if x in right)
        up_right_w = c_right.most_common(2)[1][0]
        down_right_w = c_right.most_common(1)[0][0]

        # decipher time!
        easy = {2: 1, 3: 7, 4: 4, 7: 8}

        values = []
        for number in numbers:

            value = easy.get(len(number), len(number))

            if value == 5:
                if up_right_w in number and down_right_w in number:
                    value = 3
                elif down_left_w in number:
                    value = 2
                else:
                    pass  # already 5

            if value == 6:
                if mid_w not in number:
                    value = 0
                elif down_left_w not in number:
                    value = 9
                else:
                    value = 6
            values.append(value)
        solution += int(''.join(map(str, values)))

    return solution


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
