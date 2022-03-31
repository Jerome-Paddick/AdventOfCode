import math

import numpy as np
import time


def read_input():
    with open('input.txt') as f:
        return f.read()


class Operator:
    def __init__(self, type, val):
        self.up = None
        self.down = None
        self.type = type
        self.remaining_packets = None
        self.remaining_length = None

        if type == 0:
            self.remaining_length = val
        else:
            self.remaining_packets = val


def part_1():
    hex_str = read_input()
    inp_int = int(hex_str, 16)
    get_bin = lambda x: format(x, 'b')
    inp = get_bin(inp_int)

    print(inp)
    length = len(inp)

    # vvv = inp[0:3]
    # ttt = inp[3:6]
    # # rest = inp_str[6:]
    #
    # version = int(vvv, base=2)
    # type = int(ttt, base=2)
    #
    # print('vvv', vvv, version)
    # print('ttt', ttt, type)
    # # print('rest', rest)

    class Packets:
        def __init__(self):
            self.op_packet = 'op_pa'
            self.op_len = 'op_len'
            self.lit = 'literal'

    total_version = 0
    pos = 0
    curr = None
    rem = None
    p = Packets()

    for _ in range(200):

        if pos + 11 >= length:
            break

        match curr:
            case None:
                version = int(inp[pos: pos+3], base=2)
                total_version += version
                type = int(inp[pos+3: pos+6], base=2)
                pos += 6

                if type == 4:
                    print('Literal Packet')
                    curr = p.lit
                else:
                    if inp[pos] == 0:
                        curr = p.op_packet
                        rem = int(inp[pos + 1:pos + 16], base=2)
                        pos += 16
                    else:
                        curr = p.op_len
                        rem = int(inp[pos + 1:pos + 11], base=2)
                        print(inp[pos + rem:])
                        pos += 11

            case p.lit:
                curr = None
                loop = True
                while loop:
                    print(inp[pos:pos+5])
                    if inp[pos] == '0':
                        loop = False
                    pos += 5

            case p.op_len:
                pass

            case p.op_packet:
                pass



    print(pos, curr, rem, total_version)

    # if type == 4:
    #     # Literal Packet
    #     print('Literal Packet')
    #     groups = []
    #     cont = True
    #
    #     while cont:
    #         if rest[0] == '0':
    #             cont = False
    #
    #         print('rest', rest)
    #         group = rest[1:5]
    #         groups.append(group)
    #         print(group)
    #         rest = rest[5:]
    #
    #     joined_int = int(''.join(groups), base=2)
    #     print(version, type, joined_int)
    #
    # else:
    #     # Operator Packet
    #     print('Operator Packet')
    #     if rest[0] == '0':
    #         # 15 bits -> length of sub packets
    #         bits_15 = rest[1:16]
    #         print(bits_15)
    #         print(int(bits_15, base=2))
    #
    #         ...
    #     else:
    #         # 11 bits -> immediately contained by this packet
    #         bits_11 = rest[1:12]
    #         print(int(bits_11, base=2))
    #         ...



def part_2():
    pass


start = time.perf_counter()
part_1()
# part_2()
# print('\n\n\n', time.perf_counter() - start)

