REAL_DATAFILE = "input_data.txt"
TEST_DATAFILE = "test_input_data.txt"
P1_MAX_ROCKS = 2022
P2_MAX_ROCKS = 1000000000000

DATAFILE = REAL_DATAFILE
# DATAFILE = TEST_DATAFILE


def get_next_rock(index, height):
    if index % 5 == 0:
        return {(2, height+3), (3, height+3), (4, height+3), (5, height+3)}
    elif index % 5 == 1:
        return {(3, height+3), (2, height+4), (3, height+4), (4, height+4), (3, height+5)}
    elif index % 5 == 2:
        return {(2, height+3), (3, height+3), (4, height+3), (4, height+4), (4, height+5)}
    elif index % 5 == 3:
        return {(2, height+3), (2, height+4), (2, height+5), (2, height+6)}
    else:
        return {(2, height+3), (3, height+3), (2, height+4), (3, height+4)}


def get_moved_rock(rock, movement):
    # print(f'Movement: {movement}')
    if movement == 'v':
        return {(x, y-1) for x, y in rock}
    elif movement == '>':
        return {(x+1, y) for x, y in rock}
    elif movement == '<':
        return {(x-1, y) for x, y in rock}
    else:
        return print('ERROR: INVALID MOVEMENT')


def is_valid(rock, stopped_rocks):
    min_x = min([x for x, y in rock])
    max_x = max([x for x, y in rock])
    min_y = min([y for x, y in rock])
    if min_x >= 0 and max_x < 7 and min_y >= 0 and stopped_rocks.isdisjoint(rock):
        return True
    return False


def cut_stopped_rocks(stopped_rocks, cut_height):
    return {(x, y-cut_height) for x, y in stopped_rocks if y-cut_height >= 0 }


def get_cut_value(stopped_rocks):
    column_max = list()
    for i in range(0, 7):
        column_max.append(max([x for x, y in stopped_rocks if x == i]))
    column_max.sort()
    return column_max[-1] - column_max[0] + 1


def calc_part1(jets, max_rocks):
    height = 0
    jet_index = 0
    stopped_rocks = set()
    height, jet_index, stopped_rocks = calc_intermediate(jets, max_rocks, height, jet_index, stopped_rocks)
    return height


def calc_part2(jets, max_rocks):
    height = 0
    jet_index = 0
    stopped_rocks = set()
    chunk = 100000
    quot = max_rocks // chunk
    rem = max_rocks % chunk
    true_height = height
    for i in range(0, quot):
        height, jet_index, stopped_rocks = calc_intermediate(jets, chunk, height, jet_index, stopped_rocks)
        cut_height = height - get_cut_value(stopped_rocks)
        stopped_rocks = cut_stopped_rocks(stopped_rocks, cut_height)
        true_height += cut_height
        height -= cut_height
        print(f'Intermediate height: {true_height}')
    height, jet_index, stopped_rocks = calc_intermediate(jets, rem, height, jet_index, stopped_rocks)
    return true_height + height


def calc_intermediate(jets, max_rocks, height, jet_index, stopped_rocks):
    for rock_index in range(0, max_rocks):
        rock = get_next_rock(rock_index, height)
        # print(f'Got rock: {rock}')
        is_rock_moving = True
        while is_rock_moving:
            if jet_index % len(jets) == 0 and rock_index % 5 == 0:
                print(f'rollover at {jet_index}')
            new_rock = get_moved_rock(rock, jets[jet_index % len(jets)])
            jet_index += 1
            if is_valid(new_rock, stopped_rocks):
                rock = new_rock
            # print(f'after movement: {rock}')
            new_rock = get_moved_rock(rock, 'v')
            if is_valid(new_rock, stopped_rocks):
                rock = new_rock
                # print(f'after movement: {rock}')
            else:
                # print('rock stopped')
                is_rock_moving = False
                stopped_rocks.update(rock)
                # print(f'Stopped Rocks: {stopped_rocks}')
                _height = max([y for x, y in rock]) + 1
                if _height > height:
                    height = _height
        # print(f'Height = {height}')
    return height, jet_index, stopped_rocks


def day17(filename):
    with open(filename, 'r') as f:
        input_data = f.read().split('\n')
    # print(f'Input: {input_data}')
    jets = list(input_data[0])
    # print(f'Jets: {jets}')
    height = calc_part1(jets, P1_MAX_ROCKS)
    print(f'Part1: Height: {height}')
    height = calc_part2(jets, P2_MAX_ROCKS)
    print(f'Part2: Height: {height}')


if __name__ == '__main__':
    day17(DATAFILE)
