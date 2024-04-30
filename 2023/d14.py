import sys

P = {}

def tilt_north():
    for k, p in P.copy().items():
        if p != 'O':
            continue
        above = [(kk, vv) for kk, vv in dict(sorted(P.items())).items() if kk[1] == k[1] and kk[0] < k[0] and kk != k]
        new_y = 0 if not above else above[-1][0][0] + 1
        if new_y != k[0]:
            del P[k]
            P[(new_y, k[1])] = p

def tilt_west():
    for k, p in P.copy().items():
        if p != 'O':
            continue
        left = [(kk, vv) for kk, vv in dict(sorted(P.items())).items() if kk[0] == k[0] and kk[1] < k[1] and kk != k]
        new_x = 0 if not left else left[-1][0][1] + 1
        if new_x != k[1]:
            del P[k]
            P[(k[0], new_x)] = p

def main():
    L = [x.strip() for x in sys.stdin]
    N = len(L)

    for y, line in enumerate(L):
        for x, ch in enumerate(line):
            if ch == 'O':
                P[(y, x)] = 'O'
            elif ch == '#':
                P[(y, x)] = '#'

    tilt_north()
    tilt_west()

    # p1 = 0
    # for y in [k[0] for k, v in P.items() if v == 'O']:
    #     load = N - y
    #     print(y, load)
    #     p1 += load
    # print(p1)


if __name__ == '__main__':
    main()
