def read_input():
    with open('input.txt') as f:
        return [t.strip() for t in f.readlines()]


def part_1():
    lines = read_input()

    x = 0
    y = 0

    for line in lines:
        match line.split(' '):
            case ['forward', v]:
                x += int(v)
            case ['down', v]:
                y += int(v)
            case ['up', v]:
                y -= int(v)
    print(x*y)


def part_2():
    lines = read_input()

    x = 0
    y = 0
    aim = 0

    for line in lines:
        match line.split(' '):
            case ['forward', v]:
                x += int(v)
                y += aim*int(v)
            case ['down', v]:
                aim += int(v)
            case ['up', v]:
                aim -= int(v)
    print(x*y)


# part_1()
part_2()
