# Python
import collections
import math
import re

# Local
import util

Number = collections.namedtuple('Number', ['value', 'y', 'x1', 'x2'])

def is_symbol(ch):
    return ch not in '.1234567890'

def simple_1(L):
    res = 0

    def symbol_in_bounds(y, x1, x2):
        for y in range(max(0, y - 1), min(len(L), y + 2)):
            for x in range(max(0, x1 - 1), min(len(L[0]) - 1, x2 + 1) + 1):
                if is_symbol(L[y][x]):
                    return True
        return False

    for y, line in enumerate(L):
        for m in re.finditer(r'\d+', line):
            if symbol_in_bounds(y, m.start(), m.end() - 1):
                res += int(m[0])

    return res

def simple_2(L):
    res = 0
    numbers = collections.defaultdict(list)

    def adjacent_nums(y, x):
        return [n.value for n in (numbers[y - 1] + numbers[y] + numbers[y + 1]) if (n.x1 - 1) <= x <= (n.x2 + 1)]

    for y, line in enumerate(L):
        for m in re.finditer(r'\d+', line):
            numbers[y].append(Number(m[0], y, m.start(), m.end() - 1))

    for y, line in enumerate(L):
        for x, ch in enumerate(line):
            if ch == '*':
                adj = adjacent_nums(y, x)
                if len(adj) == 2:
                    res += math.prod(map(int, adj))
    return res

if __name__ == "__main__":
    L = util.strip_stdin()
    results = util.run(L, 1, 538046, [simple_1])
    results += util.run(L, 2, 81709807, [simple_2])
    util.print_table(results)
