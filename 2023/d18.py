import sys
import itertools

# def count_interior(D, N, M):
#     result = 0
#     for i in range(N):
#         hits = 0
#         first = 999999
#         last = -999999
#         for j in range(M):
#             if D[i][j] == 1:
#                 first = min(first, j)
#                 last = max(last, j)

#         for j in range(first, last):
            
#             if D[i][j] == 1 and D[i][j-1] != 1:
#                 hits += 1
#             elif D[i][j] == 0:
#                 if hits % 2 == 1:
#                     result += 1
#     return result

def main():
    L = [x.strip() for x in sys.stdin]
    N = 999
    M = 999
    D = [[0] * M for _ in range(N)]

    y = N // 2
    x = M // 2
    D[y][x] = 1

    for i, line in enumerate(L):
        parts = line.split()
        dir = parts[0]
        amount = int(parts[1])
        colour = int(parts[2][2:-1], 16)

        for j in range(amount):
            y += 0 if dir in 'RL' else (1 if dir == 'D' else -1)
            x += 0 if dir in 'UD' else (1 if dir == 'R' else -1)
            D[y][x] = 1

    p1 = sum(x for x in itertools.chain.from_iterable(D))
    # p1 += count_interior(D, N, M)
    p1 += 
    print(p1)

if __name__ == '__main__':
    main()
