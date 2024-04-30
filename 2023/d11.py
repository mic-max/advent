import itertools
import sys

def manhattan(EC, ER, x1, y1, x2, y2, n):
    return abs(x1 - x2) + abs(y1 - y2)\
        + sum(n for x in EC if x1 <= x <= x2 or x1 >= x >= x2)\
        + sum(n for y in ER if y1 <= y <= y2 or y1 >= y >= y2)

def main():
    L = [line.strip() for line in sys.stdin]
    G = [(x, y) for y, line in enumerate(L) for x, ch in enumerate(line) if ch == '#']
    EC = [j for j in range(len(L[0])) if len(set(x[j] for x in L)) == 1]
    ER = [j for j, line in enumerate(L) if len(set(line)) == 1]

    r1 = sum(manhattan(EC, ER, *p[0], *p[1], 1) for p in itertools.combinations(G, 2))
    r2 = sum(manhattan(EC, ER, *p[0], *p[1], 999999) for p in itertools.combinations(G, 2))

    print(r1)
    print(r2)

if __name__ == '__main__':
    main()
