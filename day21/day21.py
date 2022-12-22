import sympy

REAL_DATAFILE = "input_data.txt"
TEST_DATAFILE = "test_input_data.txt"

DATAFILE = REAL_DATAFILE
# DATAFILE = TEST_DATAFILE


class Monkey:
    def __init__(self):
        self.name = ''
        self.num = 0
        self.m1name = ''
        self.m2name = ''
        self.operation = ''

    def get_number(self, left_monkeys, right_monkeys=None, constant_monkeys=None, found_root=True):
        if right_monkeys is None:
            right_monkeys = dict()
        if constant_monkeys is None:
            constant_monkeys = dict()
        if len(self.operation) == 0:
            # print(f'constant: {self} ({found_root})')
            return self.num
        else:
            # print(f'Doing operation: {self} ({found_root})')
            if found_root:
                if self.m1name in constant_monkeys:
                    lhs = constant_monkeys[self.m1name]
                else:
                    lhs = left_monkeys[self.m1name]
                if self.m2name in constant_monkeys:
                    rhs = constant_monkeys[self.m2name]
                else:
                    rhs = left_monkeys[self.m2name]
            else:
                if self.m1name == 'root':
                    # print(f'Found Root ({found_root})')
                    return left_monkeys[self.m2name].get_number(left_monkeys, right_monkeys, constant_monkeys, True)
                elif self.m2name == 'root':
                    # print(f'Found Root ({found_root})')
                    return left_monkeys[self.m1name].get_number(left_monkeys, right_monkeys, constant_monkeys, True)
                else:
                    if self.m1name in constant_monkeys:
                        lhs = constant_monkeys[self.m1name]
                    else:
                        lhs = right_monkeys[self.m1name]
                    if self.m2name in constant_monkeys:
                        rhs = constant_monkeys[self.m2name]
                    else:
                        rhs = right_monkeys[self.m2name]
            return self.do_operation(lhs.get_number(left_monkeys, right_monkeys, constant_monkeys, found_root),
                                     rhs.get_number(left_monkeys, right_monkeys, constant_monkeys, found_root))

    def do_operation(self, m1, m2):
        if self.operation == '+':
            return m1 + m2
        elif self.operation == '-':
            return m1 - m2
        elif self.operation == '*':
            return m1 * m2
        elif self.operation == '/':
            return m1 / m2
        else:
            print(f'BAD OPERATION DETECTED: {self.operation}')
            return 0

    def get_lhs_monkey(self):
        lhs = Monkey()
        lhs.name = self.m1name
        lhs.m1name = self.name
        lhs.operation = get_opposite_operation(self.operation)
        lhs.m2name = self.m2name
        return lhs

    def get_rhs_monkey(self):
        rhs = Monkey()
        rhs.name = self.m2name
        if self.operation == '-' or self.operation == '/':
            rhs.m1name = self.m1name
            rhs.operation = self.operation
            rhs.m2name = self.name
        else:
            rhs.m1name = self.name
            rhs.operation = get_opposite_operation(self.operation)
            rhs.m2name = self.m1name
        return rhs

    def __str__(self):
        if len(self.operation) == 0:
            return self.name + ': ' + str(self.num)
        else:
            return self.name + ': ' + self.m1name + ' ' + self.operation + ' ' + self.m2name


def get_opposite_operation(operation):
    output = ['-', '+', '/', '*']
    return output[['+', '-', '*', '/'].index(operation)]


def solve_for_human(input_data):
    constant_monkeys = dict()
    left_monkeys = dict()
    right_monkeys = dict()
    for line in input_data:
        raw_monkey = line.split()
        cooked_monkey = Monkey()
        cooked_monkey.name = raw_monkey[0].split(':')[0]
        if cooked_monkey.name == 'humn':
            continue
        if len(raw_monkey) == 4:
            # Make the cooked_monkey, but don't add it yet
            cooked_monkey.m1name = raw_monkey[1]
            cooked_monkey.operation = raw_monkey[2]
            cooked_monkey.m2name = raw_monkey[3]
            # Make the lhs monkey and add
            lhs_monkey = cooked_monkey.get_lhs_monkey()
            if lhs_monkey.name not in right_monkeys:
                right_monkeys[lhs_monkey.name] = lhs_monkey
            else:
                print(f'ERROR: LHS Monkey {lhs_monkey} already added')
            # Make the rhs monkey and add
            rhs_monkey = cooked_monkey.get_rhs_monkey()
            if rhs_monkey.name not in right_monkeys:
                right_monkeys[rhs_monkey.name] = rhs_monkey
            else:
                print(f'ERROR: RHS Monkey {rhs_monkey} already added')
            # Handle adding the cooked_monkey
            if cooked_monkey.name not in left_monkeys:
                left_monkeys[cooked_monkey.name] = cooked_monkey
            else:
                print(f'ERROR: Cooked Monkey {cooked_monkey} already added')
            # print(f'Monkey: {cooked_monkey}')
            # print(f'LHS Monkey: {lhs_monkey}')
            # print(f'RHS Monkey: {rhs_monkey}')
        elif len(raw_monkey) == 2:
            cooked_monkey.num = float(raw_monkey[1])
            constant_monkeys[cooked_monkey.name] = cooked_monkey
            # print(f'Monkey: {cooked_monkey}')
        else:
            print(f'ERROR: Invalid monkey line: {line}')
    return left_monkeys, right_monkeys, constant_monkeys


def copied_solution_slightly_modified_for_my_code_thankyou_hyperneutrino(input_data):
    monkeys = { "humn": sympy.Symbol("x") }
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
                    return sympy.solve(monkeys[left] - monkeys[right])[0]
                monkeys[name] = ops[op](monkeys[left], monkeys[right])
            else:
                x.append(a)


def solve_for_root(input_data):
    monkeys = dict()
    for line in input_data:
        raw_monkey = line.split()
        cooked_monkey = Monkey()
        cooked_monkey.name = raw_monkey[0].split(':')[0]
        if len(raw_monkey) == 4:
            cooked_monkey.m1name = raw_monkey[1]
            cooked_monkey.operation = raw_monkey[2]
            cooked_monkey.m2name = raw_monkey[3]
        elif len(raw_monkey) == 2:
            cooked_monkey.num = float(raw_monkey[1])
        else:
            print(f'ERROR: Invalid monkey line: {line}')
        monkeys[cooked_monkey.name] = cooked_monkey
        # print(f'Monkey: {cooked_monkey}')
    return monkeys


def day21(filename):
    with open(filename, 'r') as f:
        input_data = f.read().split('\n')
    # print(f'Input: {input_data}')
    monkeys = solve_for_root(input_data)
    # print(f'Monkey Count: {len(monkeys)}')
    root_total = monkeys['root'].get_number(monkeys)
    print(f'Part1: Root Total = {root_total}')
    # left_monkeys, right_monkeys, constant_monkeys = solve_for_human(input_data)
    # print(f'Monkey Count: {len(left_monkeys)}, {len(right_monkeys)}')
    # human_total = right_monkeys['humn'].get_number(left_monkeys, right_monkeys, constant_monkeys, False)
    # print(f'Part2: Human Total = {human_total}')
    print(f'Part2: Human Total = {copied_solution_slightly_modified_for_my_code_thankyou_hyperneutrino(input_data)}')


if __name__ == '__main__':
    day21(DATAFILE)
