import re

REAL_DATAFILE = "input_data.txt"
TEST_DATAFILE = "test_input_data.txt"
REAL_Y = 2000000
TEST_Y = 10
REAL_MAX_GRID = 4000000
TEST_MAX_GRID = 20

DATAFILE = REAL_DATAFILE
# DATAFILE = TEST_DATAFILE
USE_Y = REAL_Y
# USE_Y = TEST_Y
MAX_GRID = REAL_MAX_GRID
# MAX_GRID = TEST_MAX_GRID


def dist(ax, ay, bx, by):
    return abs(bx - ax) + abs(by - ay)


def make_sensors_beacons_set(sensors_beacons):
    sensors = set()
    beacons = set()
    for item in sensors_beacons:
        sx, sy, bx, by = item
        sensors.add((sx, sy))
        beacons.add((bx, by))
    return sensors, beacons


def calc_no_beacons(sensors_beacons, sensors, beacons, y_value, limit_to_max_grid=False):
    grid = set()
    index = 0
    for item in sensors_beacons:
        index += 1
        # print(f'Processing line {index}: {item}')
        sx, sy, bx, by = item
        d = dist(sx, sy, bx, by)
        if limit_to_max_grid:
            min_x = max(0, sx - d)
            max_x = min(sx + d, MAX_GRID)
        else:
            max_x = sx + d
            min_x = sx - d
        # print(f'min/max x: {min_x}, {max_x}')
        for ii in range(min_x, max_x + 1):
            if dist(ii, y_value, sx, sy) <= d:
                spot = (ii, y_value)
                if spot not in sensors and spot not in beacons:
                    grid.add(spot)
                    # print(f'added spot: {spot} {item}, {d}, {dist(ii, y_value, sx, sy)}')
                    # print('.', end='')
    # print('', flush=True)
    return grid


def is_within(sensors_beacons, x, y):
    for item in sensors_beacons:
        sx, sy, bx, by = item
        d = dist(bx, by, sx, sy)
        if dist(x, y, sx, sy) <= d:
            return True
    return False


def is_in_bounds(x, y):
    if 0 <= x <= MAX_GRID and 0 <= y <= MAX_GRID:
        return True
    return False


def calc_part2_2(sensors_beacons):
    for index in range(0, len(sensors_beacons)):
        # print(f'Checking line {index+1} of {len(sensors_beacons)+1}')
        item = sensors_beacons[index]
        sx, sy, bx, by = item
        d = dist(bx, by, sx, sy)
        d1 = d + 1
        d1a = d1
        d1b = 0
        while d1a > d1b:
            if is_in_bounds(sx + d1a, sy + d1b) and not is_within(sensors_beacons, sx + d1a, sy + d1b):
                return sx + d1a, sy + d1b
            elif is_in_bounds(sx + d1a, sy - d1b) and not is_within(sensors_beacons, sx + d1a, sy - d1b):
                return sx + d1a, sy - d1b
            elif is_in_bounds(sx - d1a, sy + d1b) and not is_within(sensors_beacons, sx - d1a, sy + d1b):
                return sx - d1a, sy + d1b
            elif is_in_bounds(sx - d1a, sy - d1b) and not is_within(sensors_beacons, sx - d1a, sy - d1b):
                return sx - d1a, sy - d1b
            else:
                d1a -= 1
                d1b += 1


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
    sensors, beacons = make_sensors_beacons_set(sensors_beacons)
    grid = calc_no_beacons(sensors_beacons, sensors, beacons, USE_Y)
    use_y = len([x for x in grid if x[1] == USE_Y])
    print(f'Part1: for y = 10, there are {use_y} spaces that cannot have a beacon')
    spot = calc_part2_2(sensors_beacons)
    print(f'Empty Spot: {spot}')
    print(f'Part2: Frequency: {4000000 * spot[0] + spot[1]}')


if __name__ == '__main__':
    day15(DATAFILE)
