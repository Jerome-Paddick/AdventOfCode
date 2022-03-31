import numpy as np


def read_input():
    with open('input.txt') as f:
        return [t.strip() for t in f.readlines()]


def part_1():
    lines = read_input()

    xy_vents = {'x': [], 'y': []}
    x_max = 0
    y_max = 0

    for line in lines:
        vent = [int(val) for val in line.replace(' -> ', ',').split(',')]
        if (vent_x_max := max([vent[index] for index in [0, 2]])) > x_max:
            x_max = vent_x_max
        if (vent_y_max := max([vent[index] for index in [1, 3]])) > y_max:
            y_max = vent_y_max
        if vent[0] == vent[2]:
            xy_vents['x'].append([vent[0], sorted([vent[1], vent[3]])])
        elif vent[1] == vent[3]:
            xy_vents['y'].append([vent[1], sorted([vent[0], vent[2]])])

    print(xy_vents['d'])

    grid = np.zeros([x_max, y_max]).astype(int)

    for x, [y1, y2] in xy_vents['x']:
        grid[x, y1:y2+1] += 1

    for y, [x1, x2] in xy_vents['y']:
        grid[x1:x2+1, y] += 1

    print(np.count_nonzero(grid > 1))


def part_2():
    lines = read_input()

    xy_vents = {'x': [], 'y': [], 'd': []}
    x_max = 0
    y_max = 0

    for line in lines:
        vent = [int(val) for val in line.replace(' -> ', ',').split(',')]
        if (vent_x_max := max([vent[index] for index in [0, 2]])) > x_max:
            x_max = vent_x_max
        if (vent_y_max := max([vent[index] for index in [1, 3]])) > y_max:
            y_max = vent_y_max
        if vent[0] == vent[2]:
            xy_vents['x'].append([vent[0], sorted([vent[1], vent[3]])])
        elif vent[1] == vent[3]:
            xy_vents['y'].append([vent[1], sorted([vent[0], vent[2]])])
        else:
            xy_vents['d'].append(sorted([vent[0:2], vent[2:4]], key=lambda v: v[0]))

    print(xy_vents['d'])

    grid = np.zeros([x_max, y_max]).astype(int)

    for x, [y1, y2] in xy_vents['x']:
        grid[x, y1:y2+1] += 1

    for y, [x1, x2] in xy_vents['y']:
        grid[x1:x2+1, y] += 1

    for [x1, y1], [x2, y2] in xy_vents['d']:
        y_move = 1 if y2 > y1 else -1
        curr_y = y1
        for x in range(x1, x2+1):
            grid[x, curr_y] += 1
            curr_y += y_move

    print(np.count_nonzero(grid > 1))

part_1()
part_2()
