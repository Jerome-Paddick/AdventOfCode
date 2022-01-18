from collections import Counter
import time


def read_input():
    with open('input.txt') as f:
        base = f.readline().strip()
        f.readline()
        tl = [t.strip().split(' -> ') for t in f.readlines()]
    return base, tl


def findall(string, substring):
    '''Yields all the positions of
    the pattern p in the string s.'''
    i = string.find(substring)
    while i != -1:
        yield i
        i = string.find(substring, i+1)


def part_1():
    base, tl = read_input()

    base_map = [(i, base[i]) for i in range(len(base))]

    for n in range(10):
        # print(base)
        for sub, rep in tl:
            for i in findall(base, sub):
                base_map.append((i + 0.5, rep))

        base = ''.join([item[1] for item in sorted(base_map, key=lambda x: x[0])])
        base_map = [(i, base[i]) for i in range(len(base))]
    # print(base)

    c = Counter(base)
    totals_sorted = sorted(c.values())
    print(totals_sorted[-1] - totals_sorted[0])


def part_2():
    base, tl = read_input()

    after_map = {}

    for sub, rep in tl:
        count = len(list(findall(base, sub)))
        after_map[sub] = {
            'rep': rep,
            'next': [],
            'count': count,
        }

    for sub, rep in tl:
        comb = sub[0] + rep + sub[1]
        for substring, _ in tl:
            if substring in comb:
                after_map[sub]['next'].append(substring)

    class Totals:
        def __init__(self, base):
            self.totals = {}
            for letter in base:
                self.add(letter)

        def add(self, letter, n=1):
            if letter in self.totals:
                self.totals[letter] += n
            else:
                self.totals[letter] = n

    totals = Totals(base)

    for n in range(40):
        diff_next = {after: 0 for after in after_map}
        for sub in after_map:
            if after_map[sub]['count']:
                count = after_map[sub]['count']
                for substring in after_map[sub]['next']:
                    diff_next[substring] += count
                totals.add(after_map[sub]['rep'], n=count)
                diff_next[sub] -= count
        for key, val in diff_next.items():
            after_map[key]['count'] += val

    counts = sorted([count for count in totals.totals.values()])
    print(counts[-1] - counts[0])


# part_1()
part_2()
