import numpy as np
import timeit

def read_input():
    with open('input.txt') as f:
        tl = [t.strip() for t in f.readlines()]
    return tl


def part_1():
    tl = read_input()

    grid = np.array([[int(num) for num in row] for row in tl]).astype(int)
    grid_map = np.zeros(grid.shape).astype(int)

    for i, row in enumerate(grid):
        prev = None
        for num in range(len(row) - 1):
            dir = 1 if row[num] < row[num + 1] else 0

            match prev, dir:
                case None, 1:
                    grid_map[i][num] = 1
                case 0, 1:
                    grid_map[i][num] = 1
            prev = dir

        if dir == 0:
            grid_map[i][num + 1] = 1

    for i in range(grid.shape[1]):
        col = grid[:, i]
        prev = None
        for num in range(len(col) - 1):
            dir = 1 if col[num] < col[num + 1] else 0
            match prev, dir:
                case None, 1:
                    grid_map[num][i] += 1
                case 0, 1:
                    grid_map[num][i] += 1
                    # print(grid_map[num-1:num+2, i])
            prev = dir

        if dir == 0:
            grid_map[num + 1][i] += 1
            # print(grid_map[num - 1:num + 2, i])

    x, y = np.where(grid_map == 2)

    total = 0

    for coord in range(len(x)):
        total += grid[x[coord], y[coord]] + 1

    print(total)


class Valley:
    def __init__(self, start, id, row):
        self.start = start
        self.end = None
        self.children = []
        self.parents = []
        self.id = id
        self.row = row

    def total(self):
        return (self.end - self.start) + 1


def autoincrement_gen():
    output = 0
    while True:
        yield output
        output += 1


def part_2():
    tl = read_input()
    valley_map = {n: [] for n in range(len(tl))}
    grid = np.array([[int(num) for num in row] for row in tl]).astype(int)

    gen = autoincrement_gen()

    for n in range(len(tl)):

        in_valley = False
        curr_val = None

        for i, num in enumerate(grid[n]):
            match in_valley, num:
                case False, 9:
                    continue
                case False, _:
                    val_id = next(gen)
                    curr_val = Valley(start=i, id=val_id, row=n)
                    in_valley = True
                case True, 9:
                    in_valley = False
                    curr_val.end = i - 1
                    valley_map[n].append(curr_val)
            if i == len(grid[1]) - 1 and in_valley:
                curr_val.end = i
                valley_map[n].append(curr_val)

    for n in range(1, len(tl)):
        for valley in valley_map[n]:
            for sub in valley_map[n - 1]:
                exclusive = sub.start > valley.end or sub.end < valley.start
                if not exclusive:
                    valley.children.append(sub)
                    sub.parents.append(valley)

    valley_indexes = set()

    def traverse_linked_valleys(valley):
        if valley.id in valley_indexes:
            # print('found', valley.id)
            return 0

        total = valley.total()

        valley_indexes.add(valley.id)
        for child in valley.children:
            total += traverse_linked_valleys(child)
            # valley_indexes.add(child.id)
        for parent in valley.parents:
            total += traverse_linked_valleys(parent)

        return total

    total = []

    for n in range(0, len(tl)):
        for valley in valley_map[n]:
            valley_size = traverse_linked_valleys(valley)
            if valley_size:
                total.append(valley_size)

    top_3 = sorted(total, reverse=True)[0:3]
    return np.prod(top_3)


def part_2_alt():
    tl = read_input()

    grid = np.array([[int(num) for num in row] for row in tl]).astype(int)
    visited_grid = np.zeros(grid.shape).astype(int)

    len_x, len_y = grid.shape

    for x, row in enumerate(grid):
        for y, num in enumerate(row):
            if num == 9:
                visited_grid[x, y] = 1

    def traverse_cave(x, y):
        if x < 0 or x > len_x - 1 or y < 0 or y > len_y - 1 or visited_grid[x, y] == 1:
            return 0

        total = 1
        visited_grid[x, y] = 1
        total += traverse_cave(x-1, y)
        total += traverse_cave(x+1, y)
        total += traverse_cave(x, y-1)
        total += traverse_cave(x, y+1)

        return total

    caves = []

    for x, row in enumerate(grid):
        for y, num in enumerate(row):
            if visited_grid[x, y] == 1:
                continue
            else:
                caves.append(traverse_cave(x, y))

    # print(caves)
    # print(sorted(caves, reverse=True))
    return np.prod(sorted(caves, reverse=True)[:3])

# part_1()
print(part_2())
# part_2_alt()

# p2_timeit = timeit.timeit(part_2, number=1000)
# p2_alt_timeit = timeit.timeit(part_2_alt, number=1000)
#
# print('Complex', p2_timeit)
# print('Simple', p2_alt_timeit)
# Complex 20.339120299999195
# Simple 27.07645969999976
