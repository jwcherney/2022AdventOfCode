REAL_DATAFILE = "input_data.txt"
TEST_DATAFILE = "test_input_data.txt"

DATAFILE = REAL_DATAFILE
# DATAFILE = TEST_DATAFILE


def get_signal_strength(cycle, x_register):
    if (cycle - 20) % 40 == 0 and cycle <= 220:
        # print(f'Cycle: {cycle}, register: {x_register}: Total: {cycle * x_register}')
        return cycle * x_register
    return 0


def calc_pixel(pixels, cycle, x_register):
    pixel_setting = '.'
    if abs(x_register - ((cycle-1) % 40)) <= 1:
        pixel_setting = '#'
    # print(f'cycle: {cycle-1}, mod: {(cycle-1) % 40}, x_register: {x_register}, pixel: {pixel_setting}')
    pixels.insert(cycle-1, pixel_setting)


def process_input(input_data):
    cycle = 0
    x_register = 1
    signal_strength = 0
    pixels = list()
    for line in input_data:
        command = line.split()
        cycle += 1
        signal_strength += get_signal_strength(cycle, x_register)
        calc_pixel(pixels, cycle, x_register)
        if command[0] == "addx":
            cycle += 1
            signal_strength += get_signal_strength(cycle, x_register)
            calc_pixel(pixels, cycle, x_register)
            x_register += int(command[1])
    return signal_strength, pixels


def day10(filename):
    with open(filename, 'r') as f:
        input_data = f.read().split('\n')
    # print(f'Input: {input_data}')
    signal_strength, pixels = process_input(input_data)
    print(f'Part 1: Signal Strenth: {signal_strength}')
    print(f'Part 2:')
    for i in range(0, len(pixels), 40):
        row = ''.join(pixels[i:i+40])
        print(f'{row}')


if __name__ == '__main__':
    day10(DATAFILE)
