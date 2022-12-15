import re

REAL_DATAFILE = "input_data.txt"
TEST_DATAFILE = "test_input_data.txt"
REAL_Y=2000000
TEST_Y=10

DATAFILE = REAL_DATAFILE
# DATAFILE = TEST_DATAFILE
USE_Y = REAL_Y
# USE_Y = TEST_Y


def dist(ax, ay, bx, by):
    return abs(bx - ax) + abs(by - ay)


def calc_no_beacons(sensors_beacons):
    sensors = []
    beacons = []
    grid = []
    for item in sensors_beacons:
        sx, sy, bx, by = item
        sensors.append((sx, sy))
        beacons.append((bx, by))
    for item in sensors_beacons:
        sx, sy, bx, by = item
        d = dist(sx, sy, bx, by)
        max_x = sx + d
        min_x = sx - d
        max_y = sy + d
        min_y = sy - d
        for ii in range(min_x, max_x + 1):
            for jj in range(min_y, max_y + 1):
                if dist(ii, jj, sx, sy) <= d:
                    spot = (ii, jj)
                    if spot not in sensors and spot not in beacons and spot not in grid:
                        grid.append(spot)
                        # print(f'added spot: {spot} {item}, {d}, {dist(ii, jj, sx, sy)}')
    return sensors, beacons, grid


def process_input(input_data):
    sensors_beacons = []
    for line in input_data:
        data = re.split('Sensor at x=|, y=|: closest beacon is at x=', line)
        sensors_beacons.append((int(data[1]), int(data[2]), int(data[3]), int(data[4])))
    # print(f'sensors and closest beacons: {sensors_beacons}')
    return sensors_beacons


def day15(filename):
    with open(filename, 'r') as f:
        input_data = f.read().split('\n')
    # print(f'Input: {input_data}')
    sensors_beacons = process_input(input_data)
    sensors, beacons, grid = calc_no_beacons(sensors_beacons)
    use_y = len([x for x in grid if x[1] == USE_Y])
    print(f'Part1: for y = 10, there are {use_y} spaces that cannot have a beacon')
    print(f'Part2: Not Implemented')


if __name__ == '__main__':
    day15(DATAFILE)
