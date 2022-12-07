REAL_DATAFILE = "input_data.txt"
TEST_DATAFILE = "test_input_data.txt"
DATAFILE = REAL_DATAFILE


def day01(filename):
    with open(filename, 'r') as f:
        input_data = f.read().split('\n')
    elfs = []
    sum_total = 0
    for line in input_data:
        if line == '':
            elfs.append(sum_total)
            sum_total = 0
        else:
            sum_total += int(line)
    elfs.sort(reverse=True)
    # print(f'elfs: {elfs}')
    top_three = elfs[0:3]
    print(f'Top Three: {top_three}')
    print(f'sum: {sum(top_three)}')


if __name__ == '__main__':
    day01(DATAFILE)
