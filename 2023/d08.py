import re
import sys
import math

L = [line.strip() for line in sys.stdin]
D = L[0]
M = {}

def distance(state):
    idx = 0
    # while state != 'ZZZ': # part 1
    while not state.endswith('Z'): # part 2
        y = 1 if D[idx % len(D)] == 'R' else 0
        state = M[state][y]
        idx += 1
    return idx

for line in L[2:]:
    m = re.findall(r"\w{3}", line)
    M[m[0]] = (m[1], m[2])

# p1 = distance('AAA')
# print(p1)

As = [x for x in M.keys() if x.endswith('A')]
distances = [distance(x) // len(D) for x in As]
p2 = math.prod(distances) * len(D)
print(p2)
