REAL_DATAFILE = "input_data.txt"
TEST_DATAFILE = "test_input_data.txt"

DATAFILE = REAL_DATAFILE
# DATAFILE = TEST_DATAFILE


def to_elevation(letter):
    if letter == 'S':
        return 0
    elif letter == 'E':
        return 25
    return ord(letter) - ord('a')


def to_value(area, coord):
    return area[coord[0]][coord[1]]


def is_in_area(area, coord):
    x, y = coord
    if 0 <= x < len(area) and 0 <= y < len(area[0]):
        return True
    return False


def is_valid_step(area, from_coord, to_coord):
    from_el = to_elevation(to_value(area, from_coord))
    to_el = to_elevation(to_value(area, to_coord))
    # print(f'is_valid_step: from: {from_el}, to: {to_el}')
    if to_el <= from_el + 1:
        return True
    else:
        return False


def get_valid_neighbors(area, from_here):
    valid_neighbors = []
    x, y = from_here
    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    for to_there in neighbors:
        if is_in_area(area, to_there) and is_valid_step(area, from_here, to_there):
            valid_neighbors.append(to_there)
    return valid_neighbors


def part1(area, s_coord, e_coord):
    # print(f'In part1: S: {s_coord}, E: {e_coord}')
    paths = [[s_coord]]
    already_been = [s_coord]
    active_paths = True
    while active_paths:
        new_paths = []
        active_paths = False
        for path in paths:
            if path[-1] == e_coord:
                new_paths.append(path)
                continue
            neighbors = get_valid_neighbors(area, path[-1])
            for n in neighbors:
                if n not in path and n not in already_been:
                    already_been.append(n)
                    new_path = path.copy()
                    new_path.append(n)
                    new_paths.append(new_path)
                    active_paths = True
        if active_paths:
            paths = new_paths
        # print(f'Active path count: {len(paths)}')
    if len(paths) > 0:
        paths.sort(key=len)
        shortest = paths[0]
        # pathlengths = [len(path) for path in paths]
        # print(f'Path lengths: {pathlengths}')
        # print(f'short0: {paths[0]}')
        # print(f'short1: {paths[1]}')
        # print(f'long1: {paths[-1]}')
        # print(f'long2: {paths[-2]}')
        if shortest[0] == s_coord and shortest[-1] == e_coord:
            # print(f'shortest({len(shortest)}): {shortest}')
            return shortest
        else:
            return []
    else:
        return []


def part2(area, e_coord):
    a_tags = find_all_tags(area, 'a')
    a_tags.append(find_first_tag(area, 'S'))
    # print(f'Found {len(a_tags)} starting points')
    shortest_path = []
    for s_coord in a_tags:
        path = part1(area, s_coord, e_coord)
        if len(shortest_path) == 0 or 0 < len(path) < len(shortest_path):
            shortest_path = path
            # print(f'Path length: {len(shortest_path)}')
            # print(f'short0: {shortest_path}')
    return shortest_path


def find_first_tag(area, tag):
    for x in range(0, len(area)):
        if tag in area[x]:
            y = area[x].index(tag)
            return x, y
    return None


def find_all_tags(area, tag):
    tags = []
    for x in range(0, len(area)):
        for y in range(0, len(area[0])):
            if area[x][y] == tag:
                tags.append((x, y))
    return tags


def process_input(input_data):
    area = []
    for line in input_data:
        line_list = list(line.strip())
        area.append(line_list)
    return area


def day12(filename):
    with open(filename, 'r') as f:
        input_data = f.read().split('\n')
    # print(f'Input: {input_data}')
    area = process_input(input_data)
    # print(f'Area: {area}')
    s_coord = find_first_tag(area, 'S')
    e_coord = find_first_tag(area, 'E')
    # print(f'Start at {s_coord}, End at {e_coord}')
    part1_shortest = part1(area, s_coord, e_coord)
    print(f'Part 1: Shortest path: {len(part1_shortest) - 1}')
    part2_shortest = part2(area, e_coord)
    print(f'Part 2: Shortest path: {len(part2_shortest) - 1}')


if __name__ == '__main__':
    day12(DATAFILE)
