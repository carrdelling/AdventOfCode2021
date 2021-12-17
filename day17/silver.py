
def solve(xmin, xmax, ymin, ymax):

    y_speed = abs(ymin + 1)
    max_height = int((y_speed * (y_speed + 1)) / 2)

    return max_height


def main():

    with open('input') as in_f:
        data = in_f.readline().strip()
        rest, yy = data.split('y=')
        ymin, ymax = yy.split('..')
        ymin, ymax = int(ymin), int(ymax)
        xx = data.split('x=')[-1].split(',')[0]
        xmin, xmax = xx.split('..')
        xmin, xmax = int(xmin), int(xmax)

    solution = solve(xmin, xmax, ymin, ymax)

    print(solution)


if __name__ == "__main__":

    main()

