import numpy as np


def read_input():
    with open('input.txt') as f:
        rows = [[int(num) for num in row.strip()] for row in f.readlines()]
        return np.array(rows)


def part_1():
    rows = read_input()

    x_len, y_len = rows.shape
    min_path = np.sum(rows[:, 0]) + np.sum(rows[-1, :][1:])
    traversals = 0
    print(min_path)

    def traverse_cave(x, y, history, cost=0):
        if f'{x}-{y}' in history:
            return

        nonlocal x_len, y_len, min_path, traversals
        traversals += 1

        curr_cost = cost + rows[x][y]

        if curr_cost >= min_path:
            return

        if x == x_len - 1 and y == y_len - 1:
            if cost < min_path:
                print('NEW MIN', min_path)
                min_path = curr_cost

        curr_history = history.copy()
        curr_history.add(f'{x}-{y}')

        if x > 0:
            traverse_cave(x-1, y, history=curr_history, cost=curr_cost)
        if y < y_len - 1:
            traverse_cave(x, y+1, history=curr_history, cost=curr_cost)
        if x < x_len - 1:
            traverse_cave(x+1, y, history=curr_history, cost=curr_cost)
        if y > 0:
            traverse_cave(x, y-1, history=curr_history, cost=curr_cost)

    traverse_cave(0, 0, history=set(), cost=-rows[0][0])

    print(traversals)
    print(min_path)


def part_2():
    rows = read_input()

    x_len, y_len = rows.shape
    min_path = np.sum(rows[:, 0]) + np.sum(rows[-1, :][1:])

    def traverse_cave(x, y, history, cost=0):

        if f'{x}-{y}' in history:
            return

        nonlocal x_len, y_len, min_path

        curr_cost = cost + rows[x][y]

        if curr_cost >= min_path:
            return

        if x == x_len - 1 and y == y_len - 1:
            if cost < min_path:
                print('NEW MIN', min_path)
                min_path = curr_cost

        curr_history = history.copy()
        curr_history.add(f'{x}-{y}')

        if x > 0:
            traverse_cave(x-1, y, history=curr_history, cost=curr_cost)
        if x < x_len - 1:
            traverse_cave(x+1, y, history=curr_history, cost=curr_cost)
        if y > 0:
            traverse_cave(x, y-1, history=curr_history, cost=curr_cost)
        if y < y_len - 1:
            traverse_cave(x, y+1, history=curr_history, cost=curr_cost)

    traverse_cave(0, 0, history=set(), cost=-rows[0][0])

    print(min_path)


part_1()
# part_2()
