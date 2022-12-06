REAL_DATAFILE = "input_data.txt"
TEST_DATAFILE = "test_input_data.txt"

# DATAFILE = TEST_DATAFILE
DATAFILE = REAL_DATAFILE


START_OF_PACKET = 4
START_OF_MESSAGE = 14


def find_marker(s_line, marker_length):
    # print(f'line: {s_line}')
    for i in range(marker_length, len(s_line)):
        marker = s_line[i - marker_length:i]
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


def day06(filename):
    with open(filename, 'r') as f:
        input_data = f.readlines()
    for line in input_data:
        marker_index = find_marker(line.strip(), START_OF_PACKET)
        message_index = find_marker(line.strip(), START_OF_MESSAGE)
        print(f' Marker index: {marker_index}')
        print(f'Message index: {message_index}')


if __name__ == '__main__':
    day06(DATAFILE)
