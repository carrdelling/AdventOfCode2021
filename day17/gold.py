from collections import defaultdict

MAX_STEPS = 1000  # cause 100 is not enough!


def tri(x):
    return int((x * (x + 1)) / 2)


def times_in_window(x_speed, xmin, xmax):

    steps = 0
    current = 0

    while current <= xmax and steps <= MAX_STEPS:
        current += x_speed
        x_speed += 1 if x_speed < 0 else (-1 if x_speed > 0 else 0)
        steps += 1

        if xmax >= current >= xmin:
            yield steps


def times_in_y(speed, min_, max_):

    steps = 0
    current = 0

    while current >= min_:
        current += speed
        speed += -1
        steps += 1

        if min_ <= current <= max_:
            yield steps


def solve(xmin, xmax, ymin, ymax):

    # get all possible x speeds
    speed_x_min = 1
    while tri(speed_x_min) < xmin:
        speed_x_min += 1
    speed_x_max = xmax

    # get all possible y speeds by time steps
    times_by_y_speed = defaultdict(set)
    speed_y_min = ymin
    speed_y_max = abs(ymin + 1)

    for y_speed in range(speed_y_min, speed_y_max+1):
        for t in times_in_y(y_speed, ymin, ymax):
            times_by_y_speed[t].add(y_speed)

    # get the intersections
    solutions = set()
    for x_speed in range(speed_x_min, speed_x_max+1):
        for t in times_in_window(x_speed, xmin, xmax):
            for y_speed in times_by_y_speed[t]:
                solutions.add((x_speed, y_speed))

    return len(solutions)


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

