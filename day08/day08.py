REAL_DATAFILE = "input_data.txt"
TEST_DATAFILE = "test_input_data.txt"

DATAFILE = REAL_DATAFILE
# DATAFILE = TEST_DATAFILE


def process_input(input_data):
    cooked_input = []
    for line in input_data:
        cooked_input.append(list(line))
    return cooked_input


def is_visible(trees, row, column):
    value = trees[row][column]
    if row == 0 or column == 0 or row == (len(trees) - 1) or column == (len(trees[0]) - 1):
        return True
    blocking_tree_count = 0
    for i in range(0, column):
        if trees[row][i] >= value:
            blocking_tree_count += 1
    if blocking_tree_count == 0:
        return True
    blocking_tree_count = 0
    for i in range(column + 1, len(trees[0])):
        if trees[row][i] >= value:
            blocking_tree_count += 1
    if blocking_tree_count == 0:
        return True
    blocking_tree_count = 0
    for i in range(0, row):
        if trees[i][column] >= value:
            blocking_tree_count += 1
    if blocking_tree_count == 0:
        return True
    blocking_tree_count = 0
    for i in range(row + 1, len(trees)):
        if trees[i][column] >= value:
            blocking_tree_count += 1
    if blocking_tree_count == 0:
        return True
    return False


def get_scenic_score(trees, row, column):
    value = trees[row][column]
    trees_up = 0
    for i in range(row - 1, -1, -1):
        trees_up += 1
        if trees[i][column] >= value:
            break
    trees_left = 0
    for i in range(column + 1, len(trees[0])):
        trees_left += 1
        if trees[row][i] >= value:
            break
    trees_down = 0
    for i in range(row + 1, len(trees)):
        trees_down += 1
        if trees[i][column] >= value:
            break
    trees_right = 0
    for i in range(column - 1, -1, -1):
        trees_right += 1
        if trees[row][i] >= value:
            break
    return trees_up * trees_left * trees_down * trees_right


def day08(filename):
    with open(filename, 'r') as f:
        input_data = f.read().split('\n')
    # print(f'Input: {input_data}')
    tree_map = process_input(input_data)
    # print(f'Tree Map: {tree_map}')
    count = 0
    max_scenic_score = 0
    for row in range(0, len(tree_map)):
        for column in range(0, len(tree_map[0])):
            if is_visible(tree_map, row, column):
                # print(f'Tree [{row}][{column}]={tree_map[row][column]} is visible')
                count += 1
            scenic_score = get_scenic_score(tree_map, row, column)
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score
    print(f'Part 1: Count of visible trees: {count}')
    print(f'Part 2: Max Scenic Score: {max_scenic_score}')


if __name__ == '__main__':
    day08(DATAFILE)
