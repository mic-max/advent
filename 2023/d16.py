import sys
import itertools

def bitnum(y, x):
    if y == 1: return 0
    if y == -1: return 1
    if x == 1: return 2
    if x == -1: return 3

def is_bit_set(n, p):
    return (n & (1 << p)) != 0

def main():
    L = [x.strip() for x in sys.stdin]
    # y, x, yDir, xDir
    # O = [(0, 0, 0, 1)] # p1
    O = []
    N = len(L)
    M = len(L[0])

    # fill original beam configs
    for i in range(M):
        O.append((0, i, 1, 0)) # top going down
        O.append((N - 1, i, -1, 0)) # bottom going up

    for i in range(N):
        O.append((i, 0, 0, 1)) # left going right
        O.append((i, M - 1, 0, -1)) # right going left

    p2 = 0
    for o in O:
        B = [o]
        C = [[0] * M for _ in range(N)]
        while B:
            y, x, yDir, xDir = B.pop()

            while (0 <= y < N and 0 <= x < M and not is_bit_set(C[y][x], bitnum(yDir, xDir))):
                C[y][x] |= (1 << bitnum(yDir, xDir))
                match L[y][x]:
                    case '/':
                        xDir, yDir = (-yDir, -xDir)
                    case '\\':
                        xDir, yDir = (yDir, xDir)
                    case '-':
                        if yDir != 0:
                            yDir, xDir = (0, 1)
                            B.append((y, x - 1, 0, -1))
                    case '|':
                        if xDir != 0:
                            yDir, xDir = (1, 0)
                            B.append((y - 1, x, -1, 0))
                y += yDir
                x += xDir

        x = sum(1 for x in itertools.chain.from_iterable(C) if x)
        p2 = max(x, p2)
    print(p2)

if __name__ == '__main__':
    main()
