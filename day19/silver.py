from itertools import product, permutations
from collections import defaultdict

POSSIBLE_ORIENTATIONS = [((-1) ** (i % 2), (-1) ** ((i // 2) % 2), (-1) ** ((i // 4) % 2)) for i in range(8)]
GUESSES_NEEDED = 12


class Scanner:

    def __init__(self, n):

        self.tag = n
        self.loc = None
        self.beacons = []

    @property
    def n_beacons(self):
        return len(self.beacons)

    def __str__(self):
        contents = []

        location = str(self.loc) if self.loc is not None else "Unknown"
        contents.append(f"Scanner {self.tag}; Beacons: {self.n_beacons}; Location: {location}")
        contents.append("*" * 20)
        for beacon in self.beacons:
            contents.append(str(beacon))
        contents.append('\n')

        return '\n'.join(contents)

    def add_beacon(self, beacon):
        self.beacons.append(beacon)

    def align(self, permutation, orientation):

        # we can only align a scanner if it has a position
        if self.loc is None:
            return

        aligned = []
        for b in self.beacons:
            beacon = []
            for axis, p, o in zip((0, 1, 2), permutation, orientation):
                coord = self.loc[axis] - o * b[p]
                beacon.append(coord)

            aligned.append(tuple(beacon))

        self.beacons = aligned

    def match(self, known):

        # match this scanner with another one for which we know its location

        for permutation, orientation in product(permutations((0, 1, 2)), POSSIBLE_ORIENTATIONS):
            guesses = defaultdict(int)

            for a in known.beacons:
                for b in self.beacons:
                    b_loc = tuple(aa + oo * b[pp] for aa, pp, oo in zip(a, permutation, orientation))
                    guesses[b_loc] += 1 if b_loc != (0, 0, 0) else 0

            # If 12 beacons have the same comparison, k is the absolute position of the other scanner
            valid_guesses = sorted(((votes, location) for location, votes in guesses.items()
                                    if votes >= GUESSES_NEEDED),
                                   reverse=True)
            if valid_guesses:
                return valid_guesses[0][1], permutation, orientation

        return None, None, None


def solve(data):

    scanners = []

    # build the scanners
    for idx, beacons in enumerate(data):
        scanner = Scanner(idx)
        for beacon in beacons:
            scanner.add_beacon(beacon)
        scanners.append(scanner)

    # the first scanner is in the origin
    scanners[0].loc = (0, 0, 0)

    # brute force all pairwise comparisons
    def _located():
        return sum(1 if s.loc is not None else 0 for s in scanners)

    while _located() < len(scanners):

        for x, y in product(range(len(scanners)), repeat=2):
            if (x == y) or (scanners[x].loc is None) or (scanners[y].loc is not None):
                continue

            location, permutation, orientation = scanners[y].match(scanners[x])

            if location is not None:
                scanners[y].loc = location
                scanners[y].align(permutation, orientation)
        print(f"Found {_located()}/{len(scanners)} scanners")

    real_beacons = {beacon for scanner in scanners for beacon in scanner.beacons}

    return len(real_beacons)


def main():

    data = []
    with open('input') as in_f:
        scanner = []
        for row in in_f:
            if row.startswith("---"):
                if scanner:
                    data.append(scanner)
                scanner = []
                continue
            if len(row) < 3:
                continue
            x, y, z = map(int, row.strip().split(','))
            scanner.append((x, y, z))
        else:
            data.append(scanner)

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
