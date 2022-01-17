def read_input():
    with open('input.txt') as f:
        tl = [t.strip().split('-') for t in f.readlines()]
    return tl



def part_1():
    tl = read_input()

    cave_map = {}

    for start, end in tl:
        if start in cave_map:
            cave_map[start].add(end)
        else:
            cave_map[start] = {end}
        if start == 'start':
            continue
        if end in cave_map:
            cave_map[end].add(start)
        else:
            cave_map[end] = {start}

    # cave_map = {start: end for start, end in tl}
    print(cave_map)

    cave_paths = []

    def traverse_cave_system(curr, visited, last):
        visited = visited.copy()
        visited.append(curr)

        if curr == 'end':
            cave_paths.append(visited)
            return

        paths = cave_map[curr]
        for path in paths:
            if path.isupper() and not (last == path and curr.isupper()):
                traverse_cave_system(path, visited, curr)
            elif path.islower() and path not in visited:
                traverse_cave_system(path, visited, curr)

    traverse_cave_system('start', [], None)

    print(cave_paths)
    print(len(cave_paths))


def part_2():

    start = 'start'
    A = 'A'
    b = 'b'
    c = 'c'
    d = 'd'
    end = 'end'
    asdf = [
    [start, A, b, A, b, A, c, A, end],
    [start, A, b, A, b, A, end],
    [start, A, b, A, b, end],
    [start, A, b, A, c, A, b, A, end],
    [start, A, b, A, c, A, b, end],
    [start, A, b, A, c, A, c, A, end],
    [start, A, b, A, c, A, end],
    [start, A, b, A, end],
    [start, A, b, d, b, A, c, A, end],
    [start, A, b, d, b, A, end],
    [start, A, b, d, b, end],
    [start, A, b, end],
    [start, A, c, A, b, A, b, A, end],
    [start, A, c, A, b, A, b, end],
    [start, A, c, A, b, A, c, A, end],
    [start, A, c, A, b, A, end],
    [start, A, c, A, b, d, b, A, end],
    [start, A, c, A, b, d, b, end],
    [start, A, c, A, b, end],
    [start, A, c, A, c, A, b, A, end],
    [start, A, c, A, c, A, b, end],
    [start, A, c, A, c, A, end],
    [start, A, c, A, end],
    [start, A, end],
    [start, b, A, b, A, c, A, end],
    [start, b, A, b, A, end],
    [start, b, A, b, end],
    [start, b, A, c, A, b, A, end],
    [start, b, A, c, A, b, end],
    [start, b, A, c, A, c, A, end],
    [start, b, A, c, A, end],
    [start, b, A, end],
    [start, b, d, b, A, c, A, end],
    [start, b, d, b, A, end],
    [start, b, d, b, end],
    [start, b, end],
    ]
    set_asdf = set()
    for a in asdf:
        set_asdf.add(''.join(a))

    # print(set_asdf)
    tl = read_input()

    cave_map = {}

    for start, end in tl:
        if start in cave_map:
            cave_map[start].add(end)
        else:
            cave_map[start] = {end}
        if start == 'start':
            continue
        if end in cave_map:
            cave_map[end].add(start)
        else:
            cave_map[end] = {start}

    print(cave_map, "\n")

    cave_paths = []

    # def traverse_cave_system(curr, visited, last, dub):
    #     print(curr, dub)
    #
    #     visited = visited.copy()
    #     visited.append(curr)
    #
    #     if curr == 'end':
    #         print('END\n\n')
    #         cave_paths.append(visited)
    #         return
    #
    #     paths = cave_map[curr]
    #
    #     for path in paths:
    #         if path.isupper():
    #             traverse_cave_system(path, visited, curr, dub)
    #         elif path.islower():
    #             if path not in visited:
    #                 traverse_cave_system(path, visited, curr, dub)
    #             if visited.count(path) == 1 and dub is None:
    #                 dub = path
    #                 traverse_cave_system(path, visited, curr, dub)

    cave_paths = []

    def traverse_cave_system(curr, visited, dub):
        curr_visited = visited.copy()
        curr_visited.append(curr)
        curr_dub = dub

        if curr == 'end':
            cave_paths.append(curr_visited)
            return

        for path in cave_map[curr]:
            if path.isupper():
                traverse_cave_system(path, curr_visited, curr_dub)
            if path.islower():
                if path not in visited:
                    traverse_cave_system(path, curr_visited, curr_dub)
                elif path in visited and curr_dub is False:
                    traverse_cave_system(path, curr_visited, True)

    traverse_cave_system('start', [], False)

    print('CAVES', len(cave_paths))
    print('\n\n\n')

    # for path in sorted(cave_paths, key=lambda x: len(x)):
    #     print(path)



"""
    start
    /   \
c--A-----b--d
    \   /
     end
"""

# part_1()
part_2()