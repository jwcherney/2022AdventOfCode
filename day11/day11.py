import math

REAL_DATAFILE = "input_data.txt"
TEST_DATAFILE = "test_input_data.txt"

DATAFILE = REAL_DATAFILE
# DATAFILE = TEST_DATAFILE


PART1_WORRY_LEVEL = 3


class Monkey:
    def __init__(self, number):
        self.number = number
        self.items = []
        self.items_touched = 0
        self.operation = ''
        self.operation_a = ''
        self.operation_b = ''
        self.test_amount = 0
        self.true_monkey_num = 0
        self.false_monkey_num = 0

    def catch(self, item):
        # print(f'catch: {item} {len(self.items)} {self.items_touched}')
        self.items.append(item)

    def perform_round(self, monkeys, constant_worry, worry_level):
        while len(self.items) > 0:
            item = self.items.pop(0)
            self.items_touched += 1
            worry = self.perform_operation(item)
            if constant_worry:
                worry //= PART1_WORRY_LEVEL
            else:
                worry %= worry_level
            if (worry % self.test_amount) == 0:
                monkeys[self.true_monkey_num].catch(worry)
            else:
                monkeys[self.false_monkey_num].catch(worry)

    def perform_operation(self, value):
        if self.operation_a == 'old':
            a = value
        else:
            a = int(self.operation_a)
        if self.operation_b == 'old':
            b = value
        else:
            b = int(self.operation_b)
        match self.operation:
            case '+':
                return a + b
            case '-':
                return a - b
            case '*':
                return a * b
            case '/':
                return a // b
            case _:
                print('INVALID OPERATION')
                return -1

    def test_worry(self, worry):
        return (worry % self.test_amount) == 0

    def __str__(self):
        return "Monkey " + str(self.number) + "(" + str(self.items_touched) + "):" + str(self.items)

    def __repr__(self):
        return self.__str__()


def process_input(input_data):
    monkeys = []
    current_monkey = None
    for raw in input_data:
        cooked = raw.strip()
        if cooked.startswith('Monkey'):
            num = cooked.split()[1].split(':')[0]
            current_monkey = Monkey(int(num))
        elif cooked.startswith('Starting items:'):
            items = cooked.split(':')[1].split(',')
            for x in items:
                current_monkey.items.append(int(x.strip()))
        elif cooked.startswith('Operation:'):
            expr = cooked.split(':')[1].strip().split(' ')
            current_monkey.operation_a = expr[2]
            current_monkey.operation = expr[3]
            current_monkey.operation_b = expr[4]
            # print(f'Expr: {expr}')
            # print(f'Operations: {current_monkey.operation_a} {current_monkey.operation} {current_monkey.operation_b}')
        elif cooked.startswith('Test: divisible by'):
            current_monkey.test_amount = int(cooked.split(' ')[-1])
        elif cooked.startswith('If true'):
            current_monkey.true_monkey_num = int(cooked.split(' ')[-1])
            # print(f' True Monkey: {current_monkey.true_monkey_num}')
        elif cooked.startswith('If false'):
            current_monkey.false_monkey_num = int(cooked.split(' ')[-1])
            # print(f'False Monkey: {current_monkey.false_monkey_num}')
        elif len(cooked) == 0:
            # print(f'Current Monkey: {current_monkey}')
            monkeys.append(current_monkey)
            current_monkey = None
        else:
            print('INVALID INPUT DATA')
    if current_monkey is not None:
        monkeys.append(current_monkey)
    return monkeys


def perform_rounds(input_data, rounds, constant_worry):
    monkeys = process_input(input_data)
    # print(f'Monkeys: {monkeys}')
    if constant_worry:
        worry_level = PART1_WORRY_LEVEL
    else:
        worry_level = math.lcm(*[x.test_amount for x in monkeys])
    # print(f'Worry level: {worry_level}')
    for i in range(1, rounds+1):
        for monkey in monkeys:
            monkey.perform_round(monkeys, constant_worry, worry_level)
        # if i == 20 or i % 1000 == 0:
            # print(f'End Round {i}: Monkeys: {monkeys}')
            # print(f'End Round {i}: Inspected: {[x.items_touched for x in monkeys]}')
    inspected = [x.items_touched for x in monkeys]
    # print(f'Inspected: {inspected}')
    inspected.sort(reverse=True)
    return inspected[0] * inspected[1]


def day11(filename):
    with open(filename, 'r') as f:
        input_data = f.read().split('\n')
    # print(f'Input: {input_data}')
    part1 = perform_rounds(input_data, 20, True)
    print(f'Part 1: Monkey Business = {part1}')
    part2 = perform_rounds(input_data, 10000, False)
    print(f'Part 2: Monkey Business = {part2}')


if __name__ == '__main__':
    day11(DATAFILE)
