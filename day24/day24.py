REAL_DATAFILE = "input_data.txt"
TEST_DATAFILE = "test_input_data.txt"

# DATAFILE = REAL_DATAFILE
DATAFILE = TEST_DATAFILE


def day24(filename):
    with open(filename, 'r') as f:
        input_data = f.read().split('\n')
    print(f'Input: {input_data}')
    print(f'Part1: Not Implemented')
    print(f'Part2: Not Implemented')


if __name__ == '__main__':
    day24(DATAFILE)
