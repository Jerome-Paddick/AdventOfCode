import math

import numpy as np
import time


def read_input():
    with open('input.txt') as f:

        algo_arr = [f.readline().strip()]

        while (next := f.readline().strip()) != "":
            algo_arr.append(next)

        algo = ''.join(algo_arr)
        algo_bin = algo.replace('#', '1').replace('.', '0')

        rest = []

        for line in f.readlines():
            line = line.strip().replace('#', '1').replace('.', '0')
            line_list = list(line)
            rest.append([int(item) for item in line_list])

        grid = np.array([np.array(x) for x in rest])

        return algo_bin, grid


def part_1():
    algo, grid = read_input()

    x_len, y_len = grid.shape

    # print(algo, grid)
    # print(type(grid))
    #
    # print(dir(grid))

    print(grid)

    # [rows, cols]

    for n in range(-1, x_len-1):

        flat_list = grid[:, max(n, 0):n+3].flatten()

        if n == -1 or n == x_len-2:
            width = 2
        else:
            width = 3


        print(flat_list)



    # output = np.empty([x_len, y_len], dtype='int32')
    # print(output)

start = time.time()
part_1()
print(time.time() - start)

