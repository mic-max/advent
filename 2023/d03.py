import collections
import math
import re
import sys

import util

Number = collections.namedtuple('Number', ['value', 'y', 'x1', 'x2'])

def is_symbol(ch):
    return ch not in '.1234567890'

def simple(L, part_two = False):
    res = 0
    numbers = collections.defaultdict(list)

    def symbol_in_bounds(y, x1, x2):
        for y in range(max(0, y - 1), min(LINE_COUNT, y + 2)):
            for x in range(max(0, x1 - 1), min(LINE_LENGTH - 1, x2 + 1) + 1):
                if is_symbol(L[y][x]):
                    return True
        return False

    def adjacent_nums(y, x):
        return [n.value for n in (numbers[y - 1] + numbers[y] + numbers[y + 1]) if (n.x1 - 1) <= x <= (n.x2 + 1)]

    for y, line in enumerate(L):
        for m in re.finditer(r'\d+', line):
            if part_two:
                numbers[y].append(Number(m[0], y, m.start(), m.end() - 1))
            else:
                if symbol_in_bounds(y, m.start(), m.end() - 1):
                    res += int(m[0])
    
    if part_two:
        for y, line in enumerate(L):
            for x, ch in enumerate(line):
                if ch == '*':
                    adj = adjacent_nums(y, x)
                    if len(adj) == 2:
                        res += math.prod(map(int, adj))

    return res

if __name__ == "__main__":
    L = [line.strip() for line in sys.stdin]
    LINE_COUNT = len(L)
    LINE_LENGTH = len(L[0])
    
    print("| Part Number  | Time     |")
    print("| ------------ | -------- |")
    util.run("Part 1", simple, L, 538046, None)
    util.run("Part 2", simple, L, 81709807, None, True)
