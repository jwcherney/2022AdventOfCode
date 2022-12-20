REAL_DATAFILE = "input_data.txt"
TEST_DATAFILE = "test_input_data.txt"

DATAFILE = REAL_DATAFILE
# DATAFILE = TEST_DATAFILE


DECRYPTION_CONSTANT = 811589153


def transform_to_real(cdata):
    sorted_mixing = sorted(cdata, key=lambda x: x.imag)
    for z in sorted_mixing:
        if z.imag < 0 or z.imag >= len(sorted_mixing):
            print(f'Invalid index: {int(z.imag)}')
    return [int(z.real) for z in sorted_mixing]


def transform_to_complex(rdata):
    return [complex(value, index) for index, value in enumerate(rdata)]


def apply_mix(cdata):
    # print(get_reals(mixing))
    for index, z in enumerate(cdata):
        r = int(z.real)
        i = int(z.imag)
        if r == 0:
            continue
        # print(f'real: {r}, complex: {i}')
        new_i = (i + r) % (len(cdata) - 1)
        if new_i == 0:
            new_i = len(cdata) - 1
        _min = min(new_i, i)
        _max = max(new_i, i)
        for ii, zz in enumerate(cdata):
            if z != zz:
                if new_i == _max and _min < zz.imag <= _max:
                    cdata[ii] += complex(0, -1)
                elif new_i == _min and _min <= zz.imag < _max:
                    cdata[ii] += complex(0, 1)
        cdata[index] = complex(r, new_i)
        # print(get_reals(mixing))
    return cdata


def get_total(rdata):
    zero_index = rdata.index(0)
    a = rdata[(zero_index + 1000) % len(rdata)]
    b = rdata[(zero_index + 2000) % len(rdata)]
    c = rdata[(zero_index + 3000) % len(rdata)]
    return a + b + c


def part1(rdata):
    complex_data = apply_mix(transform_to_complex(rdata))
    return get_total(transform_to_real(complex_data))


def part2(rdata):
    big_data = [x * DECRYPTION_CONSTANT for x in rdata]
    # print(get_reals(big_data))
    cdata = transform_to_complex(big_data)
    for i in range(0, 10):
        cdata = apply_mix(cdata)
        # print(transform_to_real(cdata))
    return get_total(transform_to_real(cdata))


def process_input(input_data):
    return [int(x) for x in input_data]


def day20(filename):
    with open(filename, 'r') as f:
        input_data = f.read().split('\n')
    # print(f'Input: {input_data}')
    data = process_input(input_data)
    # print(f'data: {data}')
    total1 = part1(data)
    print(f'Part1: Total = {total1}')
    total2 = part2(data)
    print(f'Part2: Ttoal = {total2}')


if __name__ == '__main__':
    day20(DATAFILE)
