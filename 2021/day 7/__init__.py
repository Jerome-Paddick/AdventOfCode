# import matplotlib.pyplot as plt
import numpy
# from matplotlib.pyplot import figure
import functools
import sys

import numpy as np


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


def part_1():
    tl = read_input()

    @functools.cache
    def fuel_cost(point):
        return np.sum(np.absolute(crabs - point))

    crabs = numpy.array([int(crab) for crab in tl]).astype(int)

    print(crabs.shape)

    found = False
    n = 0
    print('max_crabs', crabs.max())
    bi = BinarySearch(crabs.max())
    curr = bi.get_curr()
    fc = None

    while found is False and n < 100:
        print('curr: ', curr)
        fc_minus = fuel_cost(curr - 1)
        fc = fuel_cost(curr)
        fc_plus = fuel_cost(curr + 1)

        if fc_plus > fc > fc_minus:
            curr = bi.down()
        elif fc_minus > fc > fc_plus:
            curr = bi.up()
        elif fc_plus > fc < fc_minus:
            print('found')
            found = True
            print(curr)

        n += 1

    print('fuel cost:', fc)


@functools.cache
def triangle_number(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    return number + triangle_number(number - 1)


def part_2():
    tl = read_input()
    sys.setrecursionlimit(1900)

    @functools.cache
    def triangle_fuel_cost(point):
        return sum([triangle_number(val) for val in np.absolute(crabs - point)])

    crabs = numpy.array([int(crab) for crab in tl]).astype(int)

    print(crabs.shape)

    found = False
    n = 0
    print('max_crabs', crabs.max())
    bi = BinarySearch(crabs.max())
    curr = bi.get_curr()
    fc = None

    while found is False and n < 100:
        print('curr: ', curr)
        fc_minus = triangle_fuel_cost(curr - 1)
        fc = triangle_fuel_cost(curr)
        fc_plus = triangle_fuel_cost(curr + 1)

        if fc_plus > fc > fc_minus:
            curr = bi.down()
        elif fc_minus > fc > fc_plus:
            curr = bi.up()
        elif fc_plus > fc < fc_minus:
            print('found')
            found = True
            print(curr)

        n += 1

    print('fuel cost:', fc)


# part_1()
part_2()
