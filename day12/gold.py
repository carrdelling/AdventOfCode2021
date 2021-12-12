from collections import defaultdict


def walk(current, visited, drill, history):

    if current == 'end':
        return 1

    neighbors = (network[current] - visited) if not drill else network[current]
    neighbors -= {'start'}

    if not neighbors:
        return 0

    paths = 0

    for n in neighbors:
        drill_breaks = (not n.isupper()) and (n in visited)
        this_drill = drill and (not drill_breaks)
        this_visited = set(visited | {n}) if not n.isupper() else set(visited)
        paths += walk(n, this_visited, this_drill, history + [n])

    return paths


def solve(data):

    global network
    network = defaultdict(set)

    for path, path_ in data:
        network[path].add(path_)
        network[path_].add(path)

    return walk('start', {'start'}, True, ['start'])


def main():

    with open('input') as in_f:
        data = [row.strip().split('-') for row in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
