import re

REAL_DATAFILE = "input_data.txt"
TEST_DATAFILE = "test_input_data.txt"

DATAFILE = REAL_DATAFILE
# DATAFILE = TEST_DATAFILE

ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3


def dfs(blueprint, max_spend, remaining_time, factories, amounts, cache):
    if remaining_time == 0:
        # print(f'dfs: time = 0, geodes = {amounts[GEODE]}')
        return amounts[GEODE]
    key = (remaining_time, *factories, *amounts)
    # print(f'key: {key}')
    if key in cache:
        # print(f'dfs: cache hit ({len(cache)}), geodes = {cache[key]}')
        return cache[key]
    max_val = amounts[GEODE] + factories[GEODE] * remaining_time
    for factory_type, recipe in enumerate(blueprint):
        if factory_type != GEODE and factories[factory_type] >= max_spend[factory_type]:
            continue
        wait = 0
        for recipe_amount, recipe_type in recipe:
            if factories[recipe_type] == 0:
                break
            wait = max(wait, -(-(recipe_amount - amounts[recipe_type]) // factories[recipe_type]))
        else:
            new_remaining_time = remaining_time - wait - 1
            if new_remaining_time <= 0:
                continue
            new_factories = factories.copy()
            new_amounts = [amt + factory * (wait + 1) for amt, factory in zip(amounts, factories)]
            for recipe_amount, recipe_type in recipe:
                new_amounts[recipe_type] -= recipe_amount
            new_factories[factory_type] += 1
            for i in range(3):
                new_amounts[i] = min(new_amounts[i], max_spend[i] * new_remaining_time)
            max_val = max(max_val, dfs(blueprint, max_spend, new_remaining_time, new_factories, new_amounts, cache))
    # print(f'for completed (cache has {len(cache)}), geodes = {max_val}')
    cache[key] = max_val
    return max_val


def part1(blueprints):
    total = 0
    for blueprint_num, blueprint in enumerate(blueprints):
        blueprint_recipes = blueprint[0:len(blueprint) - 1]
        blueprint_max_spend = blueprint[-1]
        # print(f'Recipes: {blueprint_recipes}')
        # print(f'Max Spend: {blueprint_max_spend}')
        factories = [1, 0, 0, 0]
        amounts = [0, 0, 0, 0]
        max_geode_count = dfs(blueprint_recipes, blueprint_max_spend, 24, factories, amounts, {})
        print(f'{blueprint_num + 1}: Max Geodes: {max_geode_count}')
        total += (blueprint_num + 1) * max_geode_count
    return total


def part2(blueprints):
    total = 1
    for i in range(0, min(3, len(blueprints))):
        blueprint = blueprints[i]
        blueprint_recipes = blueprint[0:len(blueprint)-1]
        blueprint_max_spend = blueprint[-1]
        factories = [1, 0, 0, 0]
        amounts = [0, 0, 0, 0]
        max_geode_count = dfs(blueprint_recipes, blueprint_max_spend, 32, factories, amounts, {})
        print(f'{i + 1}: Max Geodes: {max_geode_count}')
        total *= max_geode_count
    return total


def process_input(input_data):
    blueprints = list()
    for line in input_data:
        blueprint = []
        max_spend = [0, 0, 0]
        for section in line.split(': ')[1].split('. '):
            recipe = list()
            for amount, material in re.findall(r'(\d+) (\w+)', section):
                amount = int(amount)
                material = ['ore', 'clay', 'obsidian'].index(material)
                recipe.append((amount, material))
                max_spend[material] = max(max_spend[material], amount)
            blueprint.append(recipe)
        blueprint.append(max_spend)
        blueprints.append(blueprint)
    # print(f'blueprints: {blueprints}')
    return blueprints


def day19(filename):
    with open(filename, 'r') as f:
        input_data = f.read().split('\n')
    # print(f'Input: {input_data}')
    blueprints = process_input(input_data)
    quality_level = part1(blueprints)
    print(f'Part1: Total Quality: {quality_level}')
    quality_level = part2(blueprints)
    print(f'Part2: Total Quality: {quality_level}')


if __name__ == '__main__':
    day19(DATAFILE)
