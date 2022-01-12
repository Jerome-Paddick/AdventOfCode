import matplotlib.pyplot as plt
import numpy
from matplotlib.pyplot import figure
import functools

def read_input():
    with open('input.txt') as f:
        tl = f.read().strip().split(',')
    return tl


class BinarySearch:
    def __init__(self, n, start=0):
        self.n = n - start
        self.curr = start + ((n-start)/2)
        self.factor = 4

    def get_curr(self):
        return round(self.curr)

    def up(self):
        self.curr = self.curr + (self.n / self.factor)
        self.factor = 2 * self.factor
        return round(self.curr)

    def down(self):
        self.curr = self.curr - (self.n / self.factor)
        self.factor = 2 * self.factor
        return round(self.curr)


def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


@functools.cache
def fuel_cost(crabs, point):
    tot = 0
    for c in crabs:
        tot += abs(c - point)
    return tot


def part_1():
    tl = read_input()

    crabs = numpy.array([int(crab) for crab in tl]).astype(int)


    found = False
    n = 0
    print(crabs.max())
    bi = BinarySearch(crabs.max())
    curr = bi.get_curr()

    fuel_cost_memo = {}

    while found is False and n < 100:


        fuel_cost(crabs, curr)


        n += 1
    # print(crabs)
    # print(sum(crabs)/len(crabs))
    #
    # fuels = []
    # for x in range(0, 1100):
    #     tot = 0
    #     for c in crabs:
    #         tot += abs(c - x)
    #     fuels.append(tot)
    # plt.plot(fuels)
    # plt.show()

def part_2():
    tl = read_input()

    inc = 0
    for n in range(3, len(tl)):
        if tl[n] > tl[n-3]:
            inc += 1

    print(inc)


part_1()
# part_2()