import numpy as np
import time


def read_input():
    with open('input.txt') as f:
        rows = [[int(num) for num in row.strip()] for row in f.readlines()]
        return np.array(rows)


def brute_force():
    rows = read_input()

    x_len, y_len = rows.shape
    min_path = np.sum(rows[:, 0]) + np.sum(rows[-1, :][1:])
    traversals = 0
    print(min_path)

    def traverse_cave(x, y, history, cost=0):
        if f'{x}-{y}' in history:
            return

        nonlocal x_len, y_len, min_path, traversals
        traversals += 1

        curr_cost = cost + rows[x][y]

        if curr_cost >= min_path:
            return

        if x == x_len - 1 and y == y_len - 1:
            if cost < min_path:
                print('NEW MIN', min_path)
                min_path = curr_cost

        curr_history = history.copy()
        curr_history.add(f'{x}-{y}')

        if x > 0:
            traverse_cave(x-1, y, history=curr_history, cost=curr_cost)
        if y < y_len - 1:
            traverse_cave(x, y+1, history=curr_history, cost=curr_cost)
        if x < x_len - 1:
            traverse_cave(x+1, y, history=curr_history, cost=curr_cost)
        if y > 0:
            traverse_cave(x, y-1, history=curr_history, cost=curr_cost)

    traverse_cave(0, 0, history=set(), cost=-rows[0][0])

    print(traversals)
    print(min_path)


def part_1():
    rows = read_input()

    x_len, y_len = rows.shape

    ons = np.zeros(rows.shape).astype(int)

    class Node:
        def __init__(self, x, y, ):
            self.x = x
            self.y = y
            self.cost = float('inf')
            self.dir = None
            self.dirs = {'u', 'l', 'd', 'r'}
            if x == x_len - 1:
                self.dirs.remove('r')
            if x == 0:
                self.dirs.remove('l')
            if y == y_len - 1:
                self.dirs.remove('d')
            if y == 0:
                self.dirs.remove('u')

    node_map = {}

    for x in range(x_len):
        for y in range(y_len):
            node_map[f'{x}-{y}'] = Node(x, y)

    node_map[f'{0}-{0}'].cost = 0
    nodes = sorted([node for node in node_map.values()], key=lambda x: x.cost)

    def count_gen():
        n = 0
        while True:
            yield n
            n += 1

    counter = count_gen()

    while len(nodes) > 0 and (curr := next(counter)) < 100000:
        nodes.sort(key=lambda x: x.cost)
        node = nodes[0]
        x = node.x
        y = node.y
        if x == x_len - 1 and y == y_len - 1:
            print('FOUND', x, y)
            break
        node_dirs = node.dirs
        if node.dir:
            node_dirs = node.dirs - {node.dir}

        for dir in node_dirs:
            match dir:
                case 'u':
                    nxt_x, nxt_y = x, y - 1
                    nxt = node_map[f'{nxt_x}-{nxt_y}']
                    mv_cost = rows[nxt_x][nxt_y]
                    mv_dir = 'd'
                case 'r':
                    nxt_x, nxt_y = x + 1, y
                    nxt = node_map[f'{nxt_x}-{nxt_y}']
                    mv_cost = rows[nxt_x][nxt_y]
                    mv_dir = 'l'
                case 'd':
                    nxt_x, nxt_y = x, y + 1
                    nxt = node_map[f'{nxt_x}-{nxt_y}']
                    mv_cost = rows[nxt_x][nxt_y]
                    mv_dir = 'u'
                case 'l':
                    nxt_x, nxt_y = x - 1, y
                    nxt = node_map[f'{nxt_x}-{nxt_y}']
                    mv_cost = rows[nxt_x][nxt_y]
                    mv_dir = 'r'
            total_cost = node.cost + mv_cost
            if nxt.cost is None or total_cost < nxt.cost:
                nxt.cost = total_cost
                nxt.dir = mv_dir
                ons[nxt_x][nxt_y] = total_cost

        del nodes[0]
    print(curr)
    print(node_map[f'{x_len-1}-{y_len-1}'].cost) # 717
    print(ons)


def part_2():
    rows = read_input()

    x_len, y_len = rows.shape

    ons = np.zeros(rows.shape).astype(int)

    # Shitty A*

    class Node:
        def __init__(self, x, y, g_cost):
            self.x = x
            self.y = y
            # distance from starting node
            self.g_cost = g_cost
            # heuristic distance from end node
            self.h_cost = (x_len - x) + (y_len - y)
            self.dir = None
            self.dirs = {'u', 'l', 'd', 'r'}
            if x == x_len - 1:
                self.dirs.remove('r')
            if x == 0:
                self.dirs.remove('l')
            if y == y_len - 1:
                self.dirs.remove('d')
            if y == 0:
                self.dirs.remove('u')

    node_map = {}

    # for x in range(x_len):
    #     for y in range(y_len):
    #         node_map[f'{x}-{y}'] = Node(x, y)
    #
    # node_map[f'{0}-{0}'].cost = 0
    # nodes = sorted([node for node in node_map.values()], key=lambda x: x.cost)

    def count_gen():
        n = 0
        while True:
            yield n
            n += 1

    counter = count_gen()

    curr_x = 0
    curr_y = 0

    nodes = []
    node_map = {f'{0}-{0}': Node(x=0, y=0, g_cost=0)}

    while curr_x != x_len - 1 and curr_y != y_len - 1 and next(counter) < 1:
        node = node_map[f'{curr_x}-{curr_y}']
        x, y = node.x, node.y
        node_dirs = node.dirs
        for dir in node_dirs:
            match dir:
                case 'u':
                    nxt_x, nxt_y = x, y - 1
                    mv_dir = 'd'
                case 'r':
                    nxt_x, nxt_y = x + 1, y
                    mv_dir = 'l'
                case 'd':
                    nxt_x, nxt_y = x, y + 1
                    mv_dir = 'u'
                case 'l':
                    nxt_x, nxt_y = x - 1, y
                    mv_dir = 'r'
            if f'{nxt_x}-{nxt_y}' not in node_map:
                mv_cost = rows[nxt_x][nxt_y]
                node_map[f'{nxt_x}-{nxt_y}'] = Node(x=nxt_x, y=nxt_y, g_cost=node.g_cost+mv_cost)
                ons[nxt_x][nxt_y] = node.g_cost+mv_cost


    print(ons)
    # while len(nodes) > 0 and (curr := next(counter)) < 100000:
    #     nodes.sort(key=lambda x: x.cost)
    #     node = nodes[0]
    #     x = node.x
    #     y = node.y
    #     node_dirs = node.dirs
    #     if node.dir:
    #         node_dirs = node.dirs - {node.dir}
    #
    #     for dir in node_dirs:
    #         match dir:
    #             case 'u':
    #                 nxt_x, nxt_y = x, y - 1
    #                 nxt = node_map[f'{nxt_x}-{nxt_y}']
    #                 mv_cost = rows[nxt_x][nxt_y]
    #                 mv_dir = 'd'
    #             case 'r':
    #                 nxt_x, nxt_y = x + 1, y
    #                 nxt = node_map[f'{nxt_x}-{nxt_y}']
    #                 mv_cost = rows[nxt_x][nxt_y]
    #                 mv_dir = 'l'
    #             case 'd':
    #                 nxt_x, nxt_y = x, y + 1
    #                 nxt = node_map[f'{nxt_x}-{nxt_y}']
    #                 mv_cost = rows[nxt_x][nxt_y]
    #                 mv_dir = 'u'
    #             case 'l':
    #                 nxt_x, nxt_y = x - 1, y
    #                 nxt = node_map[f'{nxt_x}-{nxt_y}']
    #                 mv_cost = rows[nxt_x][nxt_y]
    #                 mv_dir = 'r'
    #         total_cost = node.cost + mv_cost
    #         if nxt.cost is None or total_cost < nxt.cost:
    #             nxt.cost = total_cost
    #             nxt.dir = mv_dir
    #             ons[nxt_x][nxt_y] = total_cost
    #
    #     del nodes[0]
    # print(curr)
    # print(node_map[f'{x_len-1}-{y_len-1}'].cost)
    # print(ons)

# start = time.time()
# part_1()
# print(time.time() - start)
part_2()
