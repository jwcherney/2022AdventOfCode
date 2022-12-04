REAL_DATAFILE = "input_data.txt"
TEST_DATAFILE = "test_input_data.txt"


# DATAFILE = TEST_DATAFILE
DATAFILE = REAL_DATAFILE


def is_fully_overlapping(range1, range2):
    # print(f'range1 = ')
    # for i in range1:
    #    print(i)
    # print(f'range2 = ')
    # for i in range2:
    #    print(i)
    if (
            (range2[0] >= range1[0] and range2[len(range2) - 1] <= range1[len(range1) - 1])
            or
            (range1[0] >= range2[0] and range1[len(range1) - 1] <= range2[len(range2) - 1])
    ):
        return True
    return False


def is_any_overlapping(range1, range2):
    for i in range1:
        if i in range2:
            return True
    return False


def part1_part2(lines):
    full_overlap = 0
    any_overlap = 0
    for line in lines:
        line = line.strip()
        assignments = line.split(',')
        assignment1 = assignments[0].split('-')
        assignment2 = assignments[1].split('-')
        range1 = range(int(assignment1[0]), int(assignment1[1]) + 1)
        range2 = range(int(assignment2[0]), int(assignment2[1]) + 1)
        if is_fully_overlapping(range1, range2):
            full_overlap += 1
        if is_any_overlapping(range1, range2):
            any_overlap += 1
    print(f'Part 1: Full Overlaps = {full_overlap}')
    print(f'Part 2:  Any Overlaps = {any_overlap}')


def day04(filename):
    with open(filename, 'r') as f:
        input_data = f.readlines()
    part1_part2(input_data)


if __name__ == '__main__':
    day04(DATAFILE)
