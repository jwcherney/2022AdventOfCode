REAL_DATAFILE = "input_data.txt"
TEST1_DATAFILE = "test1_input_data.txt"
TEST2_DATAFILE = "test2_input_data.txt"

DATAFILE = REAL_DATAFILE
# DATAFILE = TEST1_DATAFILE
# DATAFILE = TEST2_DATAFILE


class Knot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.visited = set()
        self.visited.add(str(self))

    def move(self, motion):
        if motion == 'R':
            self.x += 1
        elif motion == 'L':
            self.x -= 1
        elif motion == 'U':
            self.y += 1
        elif motion == 'D':
            self.y -= 1
        else:
            print("UNKNOWN MOTION DIRECTION")

    def is_adjacent(self, knot):
        if abs(self.x - knot.x) <= 1 and abs(self.y - knot.y) <= 1:
            return True
        return False

    def get_x(self, dx):
        if dx > 0:
            return 'R'
        else:
            return 'L'

    def get_y(self, dy):
        if dy > 0:
            return 'U'
        else:
            return 'D'

    def follow(self, head):
        if not self.is_adjacent(head):
            dx = head.x - self.x
            dy = head.y - self.y
            if abs(dx) == 2 and abs(dy) == 2:
                self.move(self.get_x(dx))
                self.move(self.get_y(dy))
            else:
                if abs(dx) == 2:
                    self.move(self.get_x(dx))
                    if abs(dy) == 1:
                        self.move(self.get_y(dy))
                if abs(dy) == 2:
                    self.move(self.get_y(dy))
                    if abs(dx) == 1:
                        self.move(self.get_x(dx))
            self.visited.add(str(self))

    def visited_count(self):
        # print(f'visited: {self.visited}')
        return len(self.visited)

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'


def part1(input_data):
    head = Knot()
    tail = Knot()
    index = 0
    for line in input_data:
        index += 1
        print(f'line: {index}:{line}')
        move = line.split()
        for i in range(0, int(move[1])):
            head.move(move[0])
            tail.follow(head)
            print(f'head: {head}, tail: {tail}')
    return tail.visited_count()


def part2(input_data):
    head = Knot()
    one = Knot()
    two = Knot()
    three = Knot()
    four = Knot()
    five = Knot()
    six = Knot()
    seven = Knot()
    eight = Knot()
    nine = Knot()
    index = 0
    for line in input_data:
        index += 1
        print(f'line: {index}:{line}')
        move = line.split()
        for i in range(0, int(move[1])):
            head.move(move[0])
            one.follow(head)
            two.follow(one)
            three.follow(two)
            four.follow(three)
            five.follow(four)
            six.follow(five)
            seven.follow(six)
            eight.follow(seven)
            nine.follow(eight)
            print(f'head: {head}, one: {one}, two: {two}, three: {three}, four: {four}, five: {five}, six: {six}, seven: {seven}, eight: {eight}, nine: {nine}')
    return nine.visited_count()


def day09(filename):
    with open(filename, 'r') as f:
        input_data = f.read().split('\n')
    # print(f'Input: {input_data}')
    tail_visited = part1(input_data)
    print(f'Part 1: Tail visited positions: {tail_visited}')
    tail_visited = part2(input_data)
    print(f'Part 2: Tail visited positions: {tail_visited}')


if __name__ == '__main__':
    day09(DATAFILE)
