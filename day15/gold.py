import heapq
from itertools import product
from collections import defaultdict


class AStar:

    def __init__(self, graph):

        self.graph = defaultdict(int)

        size_x = len(graph)
        size_y = len(graph[0])

        # the graph is way bigger now!
        for idx, row in enumerate(graph):
            for iidx, v in enumerate(row):
                for i, j in product(range(5), repeat=2):
                    vv = v + i + j
                    vv = vv % 9 if vv > 9 else vv
                    x = (i * size_x) + idx
                    y = (j * size_y) + iidx
                    self.graph[(x, y)] = vv

        self.max_x = len(graph) * 5
        self.max_y = len(graph[0]) * 5

        self.best_cost = {(0, 0): 0}
        self.neighbors = [(0, (0, 0))]
        self.visited = set()

    def search(self):

        target = (self.max_x - 1, self.max_y -1)
        while self.neighbors:

            t, next_node = heapq.heappop(self.neighbors)
            if t >= self.best_cost.get(target, 9E99):
                break
            if next_node in self.visited:
                continue
            self._visit_node(next_node)

        return self.best_cost[target]

    def _visit_node(self, node):

        self.visited.add(node)

        for _x, _y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            x = node[0] + _x
            y = node[1] + _y

            if any([(x < 0), (y < 0), (x >= self.max_x), (y >= self.max_y)]):
                continue
            g = self.best_cost[node] + self.graph[(x, y)]
            h = self._heuristic(x, y)
            t = g + h

            self.best_cost[(x, y)] = min(g, self.best_cost.get((x, y), 9E99))

            if (x, y) not in self.visited:
                new_node = (t, (x, y))
                heapq.heappush(self.neighbors, new_node)

    def _heuristic(self, x, y):
        return self.max_x - x + self.max_y - y


def solve(data):

    cave = AStar(data)

    sol = cave.search()

    return sol


def main():

    with open('input') as in_f:
        data = [list(map(int, list(row.strip()))) for row in in_f if len(row) > 1]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
