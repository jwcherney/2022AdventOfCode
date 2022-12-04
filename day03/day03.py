REAL_DATAFILE = "input_data.txt"
TEST_DATAFILE = "test_input_data.txt"
DATAFILE = REAL_DATAFILE


def get_value(char):
    value = ord(char)
    if value >= ord("a"):
        value -= ord("a")
        value += 1
    elif value >= ord("A"):
        value -= ord("A")
        value += 27
    #print(f'char = {char}, value = {value}')
    return value


def get_repeated_item(line):
    length = len(line)
    half = int(length/2)
    left = line[0:half]
    right = line[half:]
    #print(f'left = {left}, right = {right}')
    for char in left:
        if char in right:
            #print(f'char = {char}')
            return char
    return ''


def get_badge(elf1, elf2, elf3):
    for char in elf1:
        if char in elf2 and char in elf3:
            return char
    return ''


def part1(lines):
    priorities = 0
    for line in lines:
        line = line.strip()
        #print(f'line = {line}')
        char = get_repeated_item(line)
        if len(char) > 0:
            priorities += get_value(char)
    print(f'Part 1: Priorities = {priorities}')


def part2(lines):
    priorities = 0
    for i in range(0, len(lines), 3):
        char = get_badge(lines[i].strip(), lines[i+1].strip(), lines[i+2].strip())
        if len(char) > 0:
            priorities += get_value(char)
    print(f'Part 2: Priorities = {priorities}')


def day03(filename):
    with open(filename, 'r') as f:
        input_data = f.readlines()
    part1(input_data)
    part2(input_data)


if __name__ == '__main__':
    day03(DATAFILE)
