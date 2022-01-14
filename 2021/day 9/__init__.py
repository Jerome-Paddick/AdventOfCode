import numpy as np

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
            grid_map[i][num+1] = 1

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
    def __init__(self, start):
        self.total = 0
        self.start = start
        self.end = None
        self.children = []
        self.parents = []


def part_2():
    tl = read_input()
    valley_map = {n: [] for n in range(len(tl))}
    grid = np.array([[int(num) for num in row] for row in tl]).astype(int)


    for n in range(len(tl)):

        in_valley = False
        curr_val = None

        for i, num in enumerate(grid[n]):
            match num, in_valley:
                case _, False:
                    curr_val = Valley(start=i)
                    in_valley = True
                case 9, True:
                    in_valley = False
                    curr_val.end = [curr_val.start, i-1]
                    valley_map[n].append(curr_val)
            if i == len(grid[1]) - 1 and in_valley:
                curr_val.end = [curr_val.start, i]
                valley_map[n].append(curr_val)

    for n in range(1, len(tl)):
        for valley in valley_map[n]:
            start, end = valley.end
            for sub in valley_map[n-1]:
                if start < sub.start < end or start < sub.end < end:
                    valley.children.append(sub)
                    sub.parents.append(valley)



    # for i, num in enumerate(grid[1]):
    #     match num, in_valley:
    #         case _, False:
    #             curr_val = Valley(start=i)
    #             in_valley = True
    #         case 9, True:
    #             in_valley = False
    #             curr_val.parents.append([curr_val.start, i-1])
    #             valley_map.append(curr_val)
    #     if i == len(grid[1]) - 1 and in_valley:
    #         curr_val.parents.append([curr_val.start, i])
    #         valley_map.append(curr_val)

    print([[valley.parents for valley in val] for key, val in valley_map.items()])




# part_1()
part_2()
