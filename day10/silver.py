

pairs = {
    '<': '>',
    '{': '}',
    '[': ']',
    '(': ')'
}

values = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


def parse(s, stack):

    if not s:
        return 0

    if s[0] in pairs:
        stack.append(s[0])
        return parse(s[1:], stack)
    elif stack and s[0] == pairs[stack[-1]]:
        stack.pop()
        return parse(s[1:], stack)
    else:
        # syntax error! corrupted!
        return values[s[0]]


def solve(data):

    return sum(parse(row, []) for row in data)


def main():

    with open('input') as in_f:
        data = [row.strip() for row in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
