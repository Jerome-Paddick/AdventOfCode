import numpy as np


def read_input():
    with open('input.txt') as f:
        tl = np.array([[int(num) for num in t.strip()] for t in f.readlines()])
    return tl


# class Clamp:
#     def __init__(self, min_val, max_x, max_y):
#         self.min_val = min_val
#         self.max_x = max_x
#         self.max_y = max_y
#
#     def x(self, val):
#         return sorted((self.min_val, val, self.max_x))[1]
#
#     def y(self, val):
#         return sorted((self.min_val, val, self.max_x))[1]

def clamp(val):
    return max((val, 0))

def part_1():
    batteries = read_input()
    # popped = np.zeros(batteries.shape)
    total = 0
    for n in range(100):
        batteries += 1
        popped = set()
        asdf = 0
        while len((nines := np.where(batteries > 9))[0]) != len(popped) and asdf < 100:
            # print(len(nines[0]), len(popped))
            for i in range(len(nines[0])):
                x, y = nines[0][i],  nines[1][i]
                if f'{x}-{y}' in popped:
                    continue
                    # print(f'{x}-{y} already added')
                popped.add(f'{x}-{y}')
                batteries[clamp(x-1):clamp(x+2), clamp(y-1): clamp(y+2)] += 1
                asdf += 1
        total += len(popped)
        batteries[batteries > 9] = 0
        print(total, len(popped))
        # for line in batteries.tolist():
        #     print(line)
    print(total)


def part_2():
    batteries = read_input()
    x_len, y_len = batteries.shape
    total_batteries = x_len*y_len

    sync = False
    total = 0
    tries = 0

    while sync is False and tries < 500:
        tries += 1
        batteries += 1
        popped = set()

        iterations = 0
        while len((nines := np.where(batteries > 9))[0]) != len(popped) and iterations < 100:
            iterations += 1

            for i in range(len(nines[0])):
                x, y = nines[0][i],  nines[1][i]
                if f'{x}-{y}' in popped:
                    continue
                    # print(f'{x}-{y} already added')
                popped.add(f'{x}-{y}')
                batteries[clamp(x-1):clamp(x+2), clamp(y-1): clamp(y+2)] += 1

        total += len(popped)
        batteries[batteries > 9] = 0
        if len(popped) == total_batteries:
            print('SYNCRONISED:', tries)
            break

    print(total)


# part_1()
part_2()
