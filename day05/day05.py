REAL_DATAFILE = "input_data.txt"
TEST_DATAFILE = "test_input_data.txt"
INDICES = {"1": 1, "2": 5, "3": 9, "4": 13, "5": 17, "6": 21, "7": 25, "8": 29, "9": 33}

# DATAFILE = TEST_DATAFILE
DATAFILE = REAL_DATAFILE


def setup_stacks(setup_lines):
    stack_line = setup_lines[0].split()
    stacks = {}
    for x in stack_line:
        stacks.update({x: []})
    for line_number in range(1, len(setup_lines)):
        line = setup_lines[line_number]
        length = len(line)
        for x in INDICES.keys():
            index = INDICES[x]
            if index < length and line[index] != ' ':
                stacks[x].append(line[index])
    # print(f'stacks setup: {stacks}')
    return stacks


def part1(stacks, lines):
    for line in lines:
        words = line.split()
        s_count = words[1]
        count = int(s_count)
        from_stack = stacks[words[3]]
        to_stack = stacks[words[5]]
        for x in range(0, count):
            crate = from_stack.pop()
            to_stack.append(crate)
    return_value = ""
    for stack in stacks.keys():
        return_value += stacks[stack][-1]
    return return_value


def part2(stacks, lines):
    for line in lines:
        words = line.split()
        s_count = words[1]
        count = int(s_count)
        from_stack = stacks[words[3]]
        to_stack = stacks[words[5]]
        hopper = from_stack[-count:]
        to_stack.extend(hopper)
        del from_stack[-count:]
    # print(f'stacks: {stacks}')
    return_value = ""
    for stack in stacks.keys():
        return_value += stacks[stack][-1]
    return return_value


def day05(filename):
    with open(filename, 'r') as f:
        input_data = f.readlines()
    setup_lines = []
    movement_lines = []
    in_setup = True
    for line in input_data:
        cooked_line = line.strip()
        if len(cooked_line) == 0:
            in_setup = False
        else:
            if in_setup:
                setup_lines.append(line)
            else:
                movement_lines.append(cooked_line)
    setup_lines.reverse()
    stacks_part1 = setup_stacks(setup_lines)
    # print(f'Stacks1: {stacks_part1}')
    stacks_part2 = {}
    for x in stacks_part1.keys():
        stacks_part2.update({x: stacks_part1[x].copy()})
    # print(f'Stacks2: {stacks_part2}')
    part1_movements = part1(stacks_part1, movement_lines)
    print(f'Part 1 output: {part1_movements}')
    part2_movements = part2(stacks_part2, movement_lines)
    print(f'Part 2 output: {part2_movements}')


if __name__ == '__main__':
    day05(DATAFILE)
