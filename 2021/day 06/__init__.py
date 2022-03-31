import numpy as np


def read_input():
    with open('input.txt') as f:
        return f.read().strip()


def part_1():
    data = np.array([int(fish) for fish in read_input().split(',')])
    values, count = np.unique(data, return_counts=True)
    fish_map = dict(zip(values, count))

    for n in range(9):
        if n not in fish_map:
            fish_map[n] = 0

    days = 80

    old_map = fish_map
    new_map = {}

    for day in range(1, days+1):
        new_map[0] = old_map[1]
        new_map[1] = old_map[2]
        new_map[2] = old_map[3]
        new_map[3] = old_map[4]
        new_map[4] = old_map[5]
        new_map[5] = old_map[6]
        new_map[6] = old_map[7] + old_map[0]
        new_map[7] = old_map[8]
        new_map[8] = old_map[0]
        old_map = new_map.copy()

        print('day', day, 'total', sum(old_map.values()))

    print(sum(old_map.values()))


def part_2():
    data = np.array([int(fish) for fish in read_input().split(',')])
    values, count = np.unique(data, return_counts=True)
    fish_map = dict(zip(values, count))

    for n in range(9):
        if n not in fish_map:
            fish_map[n] = 0

    days = 256

    old_map = fish_map
    new_map = {}

    for day in range(1, days+1):
        new_map[0] = old_map[1]
        new_map[1] = old_map[2]
        new_map[2] = old_map[3]
        new_map[3] = old_map[4]
        new_map[4] = old_map[5]
        new_map[5] = old_map[6]
        new_map[6] = old_map[7] + old_map[0]
        new_map[7] = old_map[8]
        new_map[8] = old_map[0]
        old_map = new_map.copy()

        print('day', day, 'total', sum(old_map.values()))

    print(sum(old_map.values()))


# part_1()
part_2()
