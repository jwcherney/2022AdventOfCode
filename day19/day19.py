REAL_DATAFILE = "input_data.txt"
TEST_DATAFILE = "test_input_data.txt"

# DATAFILE = REAL_DATAFILE
DATAFILE = TEST_DATAFILE


ORE=0
CLAY=1
OBSIDIAN=2
GEODE=3
def part1(blueprints):
    for blueprint in blueprints:
        num, ore_ore_need, clay_ore_need, obsidian_ore_need, obsidian_clay_need, geode_ore_need, geode_obsidian_need = blueprint
        factories = [0] * 4
        commodities = [0] * 4
        factories[0] = 1
        for minute in range(1, 25):
            new_factories = [0] * 4
            if commodities[ORE] >= geode_ore_need and commodities[OBSIDIAN] >= geode_obsidian_need:
                new_factories[GEODE] += 1
                commodities[ORE] -= geode_ore_need
                commodities[OBSIDIAN] -= geode_obsidian_need
            elif commodities[ORE] >= obsidian_ore_need and commodities[CLAY] >= obsidian_clay_need and commodities[OBSIDIAN] + factories[OBSIDIAN] <= geode_obsidian_need:
                new_factories[OBSIDIAN] += 1
                commodities[ORE] -= obsidian_ore_need
                commodities[CLAY] -= obsidian_clay_need
            elif commodities[ORE] >= clay_ore_need and commodities[CLAY] + factories[CLAY] <= obsidian_clay_need:
                new_factories[CLAY] += 1
                commodities[ORE] -= clay_ore_need
            for i in range(0, len(factories)):
                commodities[i] += factories[i]
                factories[i] += new_factories[i]
            print(f'Minute {minute}')
            print(f'  factories: {factories}')
            print(f'  commodities: {commodities}')
    return []


def process_input(input_data):
    blueprints = list()
    for line in input_data:
        data = line.split()
        num = data[1].strip(':')
        ore = int(data[6])
        clay = int(data[12])
        obsidian1 = int(data[18])
        obsidian2 = int(data[21])
        geode1 = int(data[27])
        geode2 = int(data[30])
        blueprints.append((num, ore, clay, obsidian1, obsidian2, geode1, geode2))
    return blueprints


def day19(filename):
    with open(filename, 'r') as f:
        input_data = f.read().split('\n')
    print(f'Input: {input_data}')
    blueprints = process_input(input_data)
    print(f'Blueprints: {blueprints}')
    quality_level = part1(blueprints)
    print(f'Part1: Total Quality: {sum(quality_level)}')
    print(f'Part2: Not Implemented')


if __name__ == '__main__':
    day19(DATAFILE)
