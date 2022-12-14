REAL_DATAFILE = "input_data.txt"
TEST_DATAFILE = "test_input_data.txt"

DATAFILE = REAL_DATAFILE
# DATAFILE = TEST_DATAFILE


def cmp_right_order(left, right):
    return_value = 0
    largest = max(len(left), len(right))
    for i in range(0, largest):
        return_value = 0
        try:
            l_value = left[i]
        except IndexError:
            return 1
        try:
            r_value = right[i]
        except IndexError:
            return -1
        print(f'comparing {l_value} to {r_value}')
        if type(l_value) is int and type(r_value) is int:
            if l_value < r_value:
                return 1
            elif l_value > r_value:
                return -1
        elif type(l_value) is list and type(r_value) is list:
            return_value = cmp_right_order(l_value, r_value)
        elif type(l_value) is list and type(r_value) is int:
            return_value = cmp_right_order(l_value, [r_value])
        elif type(l_value) is int and type(r_value) is list:
            return_value = cmp_right_order([l_value], r_value)
        if return_value != 0:
            return return_value
    return return_value


def part1(input_data):
    total = 0
    index = 0
    for item in input_data:
        index += 1
        left, right = item
        print(f'Comparing {index}: {left} to {right}')
        if cmp_right_order(left, right) > 0:
            total += index
            print(f'Index {index} in right order')
        else:
            print(f'Index {index} not in right order')
    return total


def process_input(input_data):
    data = list()
    left = None
    right = None
    for line in input_data:
        if len(line) == 0:
            continue
        # print(f'line: {line}')
        num = -1
        l_line = list(line)
        list_of_lists = list()
        for letter in l_line:
            if letter == '[':
                list_of_lists.append(list())
            elif letter == ']':
                finished = list_of_lists.pop()
                if num != -1:
                    finished.append(num)
                    num = -1
                if len(list_of_lists) == 0:
                    list_of_lists.extend(finished)
                else:
                    list_of_lists[-1].append(finished)
            elif letter == ',':
                if num != -1:
                    list_of_lists[-1].append(num)
                    num = -1
            else:
                if num == -1:
                    num = int(letter)
                else:
                    num *= 10
                    num += int(letter)
        # print(f'list of lists: {list_of_lists}')
        if left is None:
            left = list_of_lists
        else:
            right = list_of_lists
        if left is not None and right is not None:
            # print(f'data tuple: ({left}, {right})')
            data.append((left, right))
            left = None
            right = None
    # print(f'data to be returned: {data}')
    return data


def day13(filename):
    with open(filename, 'r') as f:
        input_data = f.read().split('\n')
    # print(f'Input: {input_data}')
    data = process_input(input_data)
    print(f'Part1: Total = {part1(data)}')


if __name__ == '__main__':
    day13(DATAFILE)
