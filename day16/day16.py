import re

REAL_DATAFILE = "input_data.txt"
TEST_DATAFILE = "test_input_data.txt"

# DATAFILE = REAL_DATAFILE
DATAFILE = TEST_DATAFILE


def calc_part1(nodes):
    return 0


def process_input(input_data):
    nodes = list()
    for line in input_data:
        data = re.split('Valve | has flow rate=|; .*valves* ', line)
        # print(f'data: {data}')
        nodes.append((data[1], data[2], list(data[3].split(', '))))
    # print(f'network: {nodes}')
    return nodes


def day16(filename):
    with open(filename, 'r') as f:
        input_data = f.read().split('\n')
    # print(f'Input: {input_data}')
    nodes = process_input(input_data)
    print(f'nodes: {nodes}')
    part1_total = calc_part1(nodes)
    print(f'Part1: Total = {part1_total}')
    print(f'Part2: Not Implemented')


if __name__ == '__main__':
    day16(DATAFILE)
