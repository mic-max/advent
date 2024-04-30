import sys
from collections import namedtuple
from math import prod
from re import finditer

Number = namedtuple('Number', ['num', 'y', 'x1', 'x2'])
Special = namedtuple('Special', ['ch', 'y', 'x'])

R = [0, 0]
L = [line for line in sys.stdin]
N = []
S = []
# keep these lists in order could optimize the searching. adjacent_nums could
# only check a 3 row window instead of every single line. then also that removes
# the y-check done in the function, leaving on the x check!

def adjacent_nums(y, x):
    return [n.num for n in N if (n.y - 1) <= y <= (n.y + 1) and (n.x1 - 1) <= x <= (n.x2 + 1)]

for y, line in enumerate(L):
    for x, ch in enumerate(line):
        if ch not in '.1234567890\n':
            S.append(Special(ch, y, x))

for y, line in enumerate(L):
    for m in finditer(r'\d+', line):
        N.append(Number(int(m[0]), y, m.start(), m.end() - 1))

for s in S:
    adj = adjacent_nums(s.y, s.x)
    if s.ch == '*' and len(adj) == 2:
        R[1] += prod(adj)

# TODO: reimplement part 1
print(R)
