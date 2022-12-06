REAL_DATAFILE = "input_data.txt"
TEST_DATAFILE = "test_input_data.txt"

# DATAFILE = TEST_DATAFILE
DATAFILE = REAL_DATAFILE


START_OF_MARKER = 4
START_OF_MESSAGE = 14


def part1(s_line, buffer_length):
    # print(f'line: {s_line}')
    for i in range(buffer_length, len(s_line)):
        marker = s_line[i-buffer_length:i]
        # print(f'marker = {marker}')
        chars = list(marker)
        # print(f'chars = {chars}')
        found_marker = True
        for j in range(0, len(chars)):
            if chars.count(chars[j]) > 1:
                found_marker = False
                break
        if found_marker:
            return i
    return -1


def part2():
    print("part 2 output")


def day06(filename):
    with open(filename, 'r') as f:
        input_data = f.readlines()
    for line in input_data:
        marker_index = part1(line.strip(), START_OF_MARKER)
        message_index = part1(line.strip(), START_OF_MESSAGE)
        print(f' Marker index: {marker_index}')
        print(f'Message index: {message_index}')
    part2()


if __name__ == '__main__':
    day06(DATAFILE)
