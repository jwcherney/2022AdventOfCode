REAL_DATAFILE = "input_data.txt"
TEST_DATAFILE = "test_input_data.txt"
DATAFILE = REAL_DATAFILE


def day01(filename):
    with open(filename, 'r') as f:
        input_data = f.readlines()
    elfs = []
    sum = 0
    highest = 0
    second = 0
    third = 0
    for line in input_data:
        if line == "\n":
            elfs.append(sum)
            if highest < sum:
                third = second
                second = highest
                highest = sum
            elif second < sum:
                third = second
                second = sum
            elif third < sum:
                third = sum
            sum = 0
        else:
            sum += int(line)
    print(f'Highest = {highest}')
    print(f'Second Highest = {second}')
    print(f'Third Highest = {third}')
    print(f'Sum of three highest = {highest + second + third}')

if __name__ == '__main__':
    day01(DATAFILE)
