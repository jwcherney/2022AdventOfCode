REAL_DATAFILE = "input_data.txt"
TEST_DATAFILE = "test_input_data.txt"

DATAFILE = REAL_DATAFILE
# DATAFILE = TEST_DATAFILE


SNAFU_CHAR = ['2', '1', '0', '-', '=']
SNAFU_VALUE = [2, 1, 0, -1, -2]
SNAFU_CONVERSION = ['0', '1', '2', '=', '-']


def dec_to_snafu(dec):
    quot = dec
    snafu = ''
    while quot > 0:
        rem = quot % 5
        quot = quot // 5
        snafu_char = SNAFU_CONVERSION[rem]
        if snafu_char == '-' or snafu_char == '=':
            quot += 1
        snafu = snafu_char + snafu
    return snafu


def snafu_to_dec(snafu):
    dec = 0
    digit_char = ['2', '1', '0', '-', '=']
    digit_val = [2, 1, 0, -1, -2]
    for index, char in enumerate(list(snafu)):
        value = SNAFU_VALUE[SNAFU_CHAR.index(char)]
        dec *= 5
        dec += value
    return dec


def part1(input_data):
    total = 0
    for line in input_data:
        data = line.split(' ')
        if len(data) == 1:
            total += snafu_to_dec(data[0])
        elif len(data) == 2:
            num = snafu_to_dec(data[0])
            to_dec_result = 'FAIL'
            if int(data[1]) == num:
                to_dec_result = 'PASS'
            to_snafu_result = 'FAIL'
            if data[0] == dec_to_snafu(num):
                to_snafu_result = 'PASS'
            print(f'Check {data[0]} == {data[1]} : {to_dec_result}/{to_snafu_result}')
        else:
            print(f' ERROR: INVALID LINE: {line}')
    return total


def day25(filename):
    with open(filename, 'r') as f:
        input_data = f.read().split('\n')
    print(f'Input: {input_data}')
    snafu_number = dec_to_snafu(8)
    dec_total = part1(input_data)
    snafu_total = dec_to_snafu(dec_total)
    print(f'Part1: Decimal Total = {dec_total}, which in snafu is {snafu_total}')
    print(f'Part2: Not Implemented')


if __name__ == '__main__':
    day25(DATAFILE)
