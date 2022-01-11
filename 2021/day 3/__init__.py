import numpy as np


def read_input():
    with open('input.txt') as f:
        return [t.strip() for t in f.readlines()]


def part_1():
    lines = read_input()

    total = np.zeros(len(lines[0]))

    for line in lines:
        line_arr = np.array([int(n) for n in line])
        total += line_arr

    num_map = ['1' if num >= 0.5 else '0' for num in total/len(lines)]

    gamma = int(''.join(num_map), base=2)
    epsilon = int(''.join(['0' if num == '1' else '1' for num in num_map]), base=2)

    print(gamma*epsilon)


def part_2():
    lines = read_input()

    most = []
    least = []


# part_1()
part_2()
