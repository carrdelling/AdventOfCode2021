import statistics

pairs = {
    '<': '>',
    '{': '}',
    '[': ']',
    '(': ')'
}

values = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def parse(s, stack):

    if not s:
        return stack

    if s[0] in pairs:
        stack.append(s[0])
        return parse(s[1:], stack)
    elif stack and s[0] == pairs[stack[-1]]:
        stack.pop()
        return parse(s[1:], stack)
    else:
        # syntax error! corrupted! empty stack!
        return []


def score(s):

    acum = 0
    for c in s[::-1]:
        acum *= 5
        acum += values[pairs[c]]
    return acum


def solve(data):

    incomplete = [parse(row, []) for row in data]
    return statistics.median(score(stack) for stack in incomplete if stack)


def main():

    with open('input') as in_f:
        data = [row.strip() for row in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
