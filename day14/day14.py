import re

REAL_DATAFILE = "input_data.txt"
TEST_DATAFILE = "test_input_data.txt"

DATAFILE = REAL_DATAFILE
# DATAFILE = TEST_DATAFILE


def part1(rocks, max_y, has_floor):
    sands = []
    keep_going = True
    active_sand = None
    while keep_going:
        if active_sand is None:
            active_sand = (500, 0)
        if active_sand in sands:
            keep_going = False
            continue
        x, y = active_sand
        if has_floor:
            if y == max_y - 1:
                print(f'Sand stopped at (floor) {active_sand}')
                if active_sand in sands or active_sand in rocks:
                    print('THATS ODD (floor)')
                    keep_going = False
                else:
                    sands.append(active_sand)
                active_sand = None
                continue
        else:
            if y > max_y:
                keep_going = False
                continue
        keep_going = True
        if (x, y + 1) not in rocks and (x, y + 1) not in sands:
            active_sand = (x, y + 1)
        elif (x - 1, y + 1) not in rocks and (x - 1, y + 1) not in sands:
            active_sand = (x - 1, y + 1)
        elif (x + 1, y + 1) not in rocks and (x + 1, y + 1) not in sands:
            active_sand = (x + 1, y + 1)
        else:
            print(f'Sand stopped at (else) {active_sand}')
            if active_sand in sands or active_sand in rocks:
                print('THATS ODD (else)')
                keep_going = False
            else:
                sands.append(active_sand)
            active_sand = None
    min_x = min([s[0] for s in sands])
    max_x = max([s[0] for s in sands])
    print(f'spans from {min_x} to {max_x}')
    return len(sands)


def cmp(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


def process_input(input_data):
    rocks = []
    for line in input_data:
        coords = re.split(' -> |,', line)
        # print(f'coords: {coords}')
        for i in range(0, len(coords) - 2, 2):
            x1 = int(coords[i])
            y1 = int(coords[i + 1])
            x2 = int(coords[i + 2])
            y2 = int(coords[i + 3])
            if x1 == x2:
                for j in range(y1, y2 + cmp(y2, y1), cmp(y2, y1)):
                    rock = (x1, j)
                    if rock not in rocks:
                        rocks.append(rock)
                        # print(f'adding rock: {rock}')
            elif y1 == y2:
                for j in range(x1, x2 + cmp(x2, x1), cmp(x2, x1)):
                    rock = (j, y1)
                    if rock not in rocks:
                        rocks.append(rock)
                        # print(f'adding rock: {rock}')
            else:
                print('BAD INPUT')
    # print(f'Rocks: {rocks}')
    return rocks


def day14(filename):
    with open(filename, 'r') as f:
        input_data = f.read().split('\n')
    # print(f'Input: {input_data}')
    rocks = process_input(input_data)
    max_y = max([r[1] for r in rocks])
    print(f'max_y = {max_y}')
    print(f'Part1: Total: {part1(rocks, max_y, False)}')
    # print(f'Part2: Total: {part1(rocks, max_y + 2, True)}')


if __name__ == '__main__':
    day14(DATAFILE)
