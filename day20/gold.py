from itertools import product


MASK = [(-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 0), (0, 1),
        (1, -1), (1, 0), (1, 1)]

PIX2VALUE = {'.': '0', '#': '1'}


def convolution(image, alg, round):

    # compute padding

    padding = '.'
    r = 0
    while r < round:
        v = ''.join([PIX2VALUE[padding]] * 9)
        padding = alg[int(v, 2)]
        r += 1

    new_image = {}

    min_x = min(x[0] for x in image) - 1
    min_y = min(x[1] for x in image) - 1
    max_x = max(x[0] for x in image) + 1
    max_y = max(x[1] for x in image) + 1

    for x, y in product(range(min_x, max_x+1), range(min_y, max_y+1)):

        signature = []

        for xx, yy in MASK:
            if (x+xx, y+yy) in image:
                signature.append(image[(x+xx, y+yy)])
            else:
                signature.append(padding)

        signature = ''.join(PIX2VALUE[image.get((x+m[0], (y+m[1])), padding)] for m in MASK)
        new_image[(x, y)] = alg[int(signature, 2)]

    return new_image


def solve(alg, image):

    for r in range(50):
        image = convolution(image, alg, r)

    return sum(1 if p == '#' else 0 for p in image.values())


def main():

    with open('input') as in_f:
        alg = {idx: x for idx, x in enumerate(in_f.readline().strip())}
        in_f.readline()

        image = {}
        for idx, row in enumerate(in_f):
            for idx2, char in enumerate(row.strip()):
                image[(idx, idx2)] = char

    solution = solve(alg, image)

    print(solution)


if __name__ == "__main__":

    main()
