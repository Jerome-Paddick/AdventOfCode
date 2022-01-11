import numpy as np


def read_input():
    with open('input.txt') as f:
        return [t.strip() for t in f.readlines()]


def part_1():
    lines = read_input()

    total = np.zeros(len(lines[0]))

    for line in lines:
        total += np.array([int(n) for n in line])

    num_map = ['1' if num >= 0.5 else '0' for num in total/len(lines)]

    gamma = int(''.join(num_map), base=2)
    epsilon = int(''.join(['0' if num == '1' else '1' for num in num_map]), base=2)

    print(gamma*epsilon)


def part_2():
    lines = read_input()

    n = 0

    a_most = np.array([[int(num) for num in line] for line in lines])
    im = 0

    a_least = a_most.copy()
    il = 0

    while n < 100:

        most_rows = a_most.shape[0]
        least_rows = a_least.shape[0]

        # print(n)
        # print('most', most_rows)
        # print('least', least_rows)

        if most_rows == 1 and least_rows == 1:
            break

        if most_rows > 1:
            m_col_sum = a_most[:, im].sum()
            most = 1 if m_col_sum >= most_rows / 2 else 0
            a_most = a_most[a_most[:, im] == most]
            im += 1

        if least_rows > 1:
            l_col_sum = a_least[:, il].sum()
            least = 1 if l_col_sum < least_rows / 2 else 0
            a_least = a_least[a_least[:, il] == least]
            il += 1

        n+=1

    oxygen = int(''.join([str(n) for n in a_most[0]]), base=2)
    co2 = int(''.join([str(n) for n in a_least[0]]), base=2)

    print(oxygen*co2)

# part_1()
part_2()
