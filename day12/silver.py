from collections import defaultdict


def walk(current, visited):

    if current == 'end':
        return 1

    neighbors = network[current] - visited

    if not neighbors:
        return 0

    paths = 0

    for n in neighbors:
        this_visited = set(visited | {n}) if not n.isupper() else set(visited)
        paths += walk(n, this_visited)

    return paths


def solve(data):

    global network
    network = defaultdict(set)

    for path, path_ in data:
        network[path].add(path_)
        network[path_].add(path)

    return walk('start', {'start'})


def main():

    with open('input') as in_f:
        data = [row.strip().split('-') for row in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
