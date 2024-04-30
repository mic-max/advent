import sys
import collections

L = [line.strip() for line in sys.stdin]
G = []
N = len(L)
M = len(L[0])
D = collections.defaultdict(lambda: 9999)

def dfs(y, x, steps):
    if not (0 <= y < N and 0 <= x < M) or G[y][x] == '#':
        return

    G[y][x] = '.'
    D[(y, x)] = min(steps, D[(y, x)])

    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        dfs(y + dy, x + dx, steps + 1)    

sy, sx = -1, -1
for y, line in enumerate(L):
    G.append([])
    for x, ch in enumerate(line):
        if ch == 'S':
            sy, sx = y, x
        G[y].append(ch)
    
dfs(sy, sx, 0)

for y, row in enumerate(G):
    for x, col in enumerate(row):
        # if G[(y, x)]
        print(col, end='')
    print()

print(D)

p1 = 0
# for pos, steps in D.items():
#     print(pos, steps)
    # if steps % 2 == 1:
    #     p1 += 1
print('Part 1:', p1)

# Pattern emerges after walking 6 steps.
# x == even, y == even
# x == odd, y == odd
# x % 2 == y % 2 and ch == '.'
# starting pos 5,5
# y range: [2, 9] that's 5-3 and 5+4
# x range: [0, 8] that's 5-5 and 5+3

# count spots reachable in exactly 6 steps.
# if I flood fill and remember how long it took to get to each position.
#  if a position is <= 64 and is even i can reach it...
