REAL_DATAFILE = "input_data.txt"
TEST_DATAFILE = "test_input_data.txt"
INDICES = {"1": 1, "2": 5, "3": 9, "4": 13, "5": 17, "6": 21, "7": 25, "8": 29, "9": 33}

# DATAFILE = TEST_DATAFILE
DATAFILE = REAL_DATAFILE


def stack_push(stacks, stack, crate):
    crates = stacks[stack]
    crates.append(crate)
    stacks.update({stack: crates})
    return stacks


def stack_pop(stacks, stack):
    crates = stacks[stack]
    crate = crates.pop()
    stacks.update({stack: crates})
    return crate


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
                stacks = stack_push(stacks, x, line[index])
    # print(f'stacks setup: {stacks}')
    return stacks


def part1(stacks, lines):
    for line in lines:
        words = line.split()
        count = words[1]
        from_stack = words[3]
        to_stack = words[5]
        for x in range(0, int(count)):
            crate = stack_pop(stacks, from_stack)
            stacks = stack_push(stacks, to_stack, crate)
    return_value = ""
    for stack in stacks.keys():
        return_value += stacks[stack][-1]
    return return_value


def part2(stacks, lines):
    for line in lines:
        words = line.split()
        count = words[1]
        from_stack = words[3]
        to_stack = words[5]
        hopper = []
        for x in range(0, int(count)):
            hopper.append(stack_pop(stacks, from_stack))
        for x in range(0, int(count)):
            stacks = stack_push(stacks, to_stack, hopper.pop())
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
    stacks_part2 = setup_stacks(setup_lines)
    # print(f'Stacks2: {stacks_part2}')
    part1_movements = part1(stacks_part1, movement_lines)
    print(f'Part 1 output: {part1_movements}')
    part2_movements = part2(stacks_part2, movement_lines)
    print(f'Part 2 output: {part2_movements}')


if __name__ == '__main__':
    day05(DATAFILE)
