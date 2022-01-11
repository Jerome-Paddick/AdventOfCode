def read_input():
    with open('input.txt') as f:
        tl = [int(t.strip()) for t in f.readlines()]
    return tl


def part_1():
    tl = read_input()

    increase = 0
    for n in range(1, len(tl)):
        if tl[n] > tl[n-1]:
            increase += 1

    print(increase)


def part_2():
    tl = read_input()

    inc = 0
    for n in range(3, len(tl)):
        if tl[n] > tl[n-3]:
            inc += 1

    print(inc)

part_2()