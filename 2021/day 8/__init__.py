def read_input():
    with open('input.txt') as f:
        tl = [t.strip() for t in f.readlines()]
    return tl


def part_1():
    tl = read_input()

    total_unique = 0

    for line in tl:
        i, o = line.split('|')
        o = o.split()
        for out in o:
            if len(out) in [2, 3, 4, 7]:
                total_unique += 1

    print(total_unique)


def part_2():
    tl = read_input()

    """
      0:      1:      2:      3:      4:
     aaaa    ....    aaaa    aaaa    ....
    b    c  .    c  .    c  .    c  b    c
    b    c  .    c  .    c  .    c  b    c
     ....    ....    dddd    dddd    dddd
    e    f  .    f  e    .  .    f  .    f
    e    f  .    f  e    .  .    f  .    f
     gggg    ....    gggg    gggg    ....

      5:      6:      7:      8:      9:
     aaaa    aaaa    aaaa    aaaa    aaaa
    b    .  b    .  .    c  b    c  b    c
    b    .  b    .  .    c  b    c  b    c
     dddd    dddd    ....    dddd    dddd
    .    f  e    f  .    f  e    f  .    f
    .    f  e    f  .    f  e    f  .    f
     gggg    gggg    ....    gggg    gggg
    """

    len_map = {
        2: [1],
        3: [7],
        4: [4],
        5: [2, 3, 5],
        6: [0, 6, 9],
        7: [8]}

    total = 0

    for row in tl:
        i, o = row.split('|')

        coords = [set(coord) for coord in i.split()]

        _0, _1, _2, _3, _4, _5, _6, _7, _8, _9, = [None for _ in range(10)]
        _2_3_5, _0_6_9 = [], []

        for coord in coords:
            match len(coord):
                case 5:
                    _2_3_5.append(coord)
                case 6:
                    _0_6_9.append(coord)
                case 2:
                    _1 = coord
                case 3:
                    _7 = coord
                case 4:
                    _4 = coord
                case 7:
                    _8 = coord

        _069 = _0_6_9[0] & _0_6_9[1] & _0_6_9[2]
        _235 = _2_3_5[0] & _2_3_5[1] & _2_3_5[2]

        a = _7 - _1
        f = _1 & _069
        c = _1 - f
        d = (_235 - a) & _4
        b = _4 - c - d - f

        for num in _2_3_5:
            if len(num & b) == 1:
                _5 = num
            elif len(num & _1) == 2:
                _3 = num
            else:
                _2 = num

        _0 = _8 - d
        for num in _0_6_9:
            if num == _0:
                continue
            elif len(num & c) == 0:
                _6 = num
            else:
                _9 = num

        in_coord_map = {
            ''.join(sorted(list(_0))): 0,
            ''.join(sorted(list(_1))): 1,
            ''.join(sorted(list(_2))): 2,
            ''.join(sorted(list(_3))): 3,
            ''.join(sorted(list(_4))): 4,
            ''.join(sorted(list(_5))): 5,
            ''.join(sorted(list(_6))): 6,
            ''.join(sorted(list(_7))): 7,
            ''.join(sorted(list(_8))): 8,
            ''.join(sorted(list(_9))): 9,

        }
        # print(in_coord_map)
        out_coords = [''.join(sorted(coord)) for coord in o.split()]
        # print(len([in_coord_map[out_coord] for out_coord in out_coords]))
        total += int(''.join([str(in_coord_map[out_coord]) for out_coord in out_coords]))



    print(total)

# part_1()
part_2()
