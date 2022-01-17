import math


def read_input():
    with open('input.txt') as f:
        return f
        # tl = [int(t.strip()) for t in f.readlines()]


def part_1():

    start_chunk = {'(', '[', '{', '<'}
    end_chunk = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    score_map = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    scores = {
        ')': 0,
        ']': 0,
        '}': 0,
        '>': 0,
    }
    score = 0

    with open('input.txt') as f:
        while line := f.readline():
            stack = []
            chunk = ''
            for c in line.strip():
                if c in start_chunk:
                    chunk += c
                    stack.append(end_chunk[c])
                else:
                    s_pop = stack.pop()
                    if s_pop != c:
                        score += score_map[c]
                        break

    print(score)


def part_2():

    start_chunk = {'(', '[', '{', '<'}
    end_chunk = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    score_map = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }

    scores = []

    with open('input.txt') as f:
        while line := f.readline():

            stack = []
            corr = False
            line_score = 0

            for c in line.strip():
                if c in start_chunk:
                    stack.append(end_chunk[c])
                elif s_pop := stack.pop() != c:
                    corr = True
                    break
            if not corr:
                for c in stack[::-1]:
                    line_score *= 5
                    line_score += score_map[c]
                # print(line_score)
                scores.append(line_score)

    print(sorted(scores)[int(len(scores)/2)])


# part_1()
part_2()