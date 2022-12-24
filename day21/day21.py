import sympy

REAL_DATAFILE = "input_data.txt"
TEST_DATAFILE = "test_input_data.txt"

DATAFILE = REAL_DATAFILE
# DATAFILE = TEST_DATAFILE


class Monkey:
    def __init__(self, line=None):
        self.name = ''
        self.num = 0
        self.m1name = ''
        self.m2name = ''
        self.operation = ''
        if line is not None and len(line) > 0:
            line = line.split()
            self.name = line[0].split(':')[0]
            if len(line) == 4:
                self.m1name = line[1]
                self.operation = line[2]
                self.m2name = line[3]
            elif len(line) == 2:
                self.num = float(line[1])
            else:
                print(f'ERROR: Invalid monkey line: {line}')

    def is_constant(self):
        return len(self.operation) == 0

    def get_number(self, monkeys):
        if len(self.operation) == 0:
            # print(f'constant: {self} ({found_root})')
            return self.num
        else:
            # print(f'Doing operation: {self} ({found_root})')
            lhs = monkeys[self.m1name]
            rhs = monkeys[self.m2name]
            return self.do_operation(lhs.get_number(monkeys),
                                     rhs.get_number(monkeys))

    def do_operation(self, m1, m2):
        if self.operation == '+':
            return m1 + m2
        elif self.operation == '-':
            return m1 - m2
        elif self.operation == '*':
            return m1 * m2
        elif self.operation == '/':
            return m1 // m2
        else:
            print(f'BAD OPERATION DETECTED: {self.operation}')
            return 0

    def __str__(self):
        if self.is_constant():
            return self.name + ': ' + str(self.num)
        else:
            return self.name + ': ' + self.m1name + ' ' + self.operation + ' ' + self.m2name


def get_opposite_operation(operation):
    output = ['-', '+', '/', '*']
    return output[['+', '-', '*', '/'].index(operation)]


def copied_solution_slightly_modified_for_my_code_thankyou_hyperneutrino(input_data):
    monkeys = {"humn": sympy.Symbol("x")}
    x = [line.strip() for line in input_data]
    ops = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }
    for a in x:
        name, expr = a.split(": ")
        if name in monkeys: continue
        if expr.isdigit():
            monkeys[name] = sympy.Integer(expr)
        else:
            left, op, right = expr.split()
            if left in monkeys and right in monkeys:
                if name == "root":
                    # print(f' here1: {monkeys[name]}')
                    return sympy.solve(monkeys[left] - monkeys[right])[0]
                monkeys[name] = ops[op](monkeys[left], monkeys[right])
            else:
                x.append(a)


def sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0


def solve_for_human(monkeys):
    human = monkeys['humn']
    root = monkeys['root']
    root.operation = get_opposite_operation(root.operation)
    low_h = human.get_number(monkeys)
    low_r = root.get_number(monkeys)
    # print(f'Root when humn = {human.num} = {low_r}')
    h_delta = 10
    high_h = low_h * h_delta
    human.num *= high_h
    high_r = root.get_number(monkeys)
    while sign(low_r) == sign(high_r):
        high_h = high_h * 10
        human.num = high_h
        high_r = root.get_number(monkeys)
    while not(abs(high_r - low_r) <= 1) and not(abs(high_h - low_h) <= 1):
        mid_h = (high_h + low_h) // 2
        human.num = mid_h
        mid_r = root.get_number(monkeys)
        if sign(mid_r) == sign(low_r):
            low_h = mid_h
            low_r = mid_r
        else:
            high_h = mid_h
            high_r = mid_r
        # print(f'({low_r}, {low_h}, {h_delta})')
    if low_r == 0:
        return low_h
    else:
        return high_h


def make_monkeys(input_data):
    monkeys = dict()
    for line in input_data:
        monkey = Monkey(line)
        monkeys[monkey.name] = monkey
        # print(f'Monkey: {monkey}')
    return monkeys


def day21(filename):
    with open(filename, 'r') as f:
        input_data = f.read().split('\n')
    # print(f'Input: {input_data}')
    monkeys = make_monkeys(input_data)
    # print(f'Monkey Count: {len(monkeys)}')
    root_total = monkeys['root'].get_number(monkeys)
    print(f'Part1: Root Total = {root_total}')
    monkeys = make_monkeys(input_data)
    human_total2 = solve_for_human(monkeys)
    print(f'Part2: Human Total = {human_total2}')
    print(f'Part2: Human Total = {copied_solution_slightly_modified_for_my_code_thankyou_hyperneutrino(input_data)}')


if __name__ == '__main__':
    day21(DATAFILE)
