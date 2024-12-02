# Python
import collections
import itertools

# Local
import util

def is_safe(levels):
    increasing = levels[0] < levels[-1]
    for l, r in itertools.pairwise(levels):
        diff = r - l
        if increasing and (diff < 1 or diff > 3):
            return False
        if not increasing and (diff < -3 or diff > -1):
            return False

    return True

def simple_1(L):
    # started at ~12:54pm
    res = 0
    for line in L:
        levels = list(map(int, line.split()))
        safe = is_safe(levels)
        if safe:
            res += 1

    return res

def simple_2(L):
    # finished at 1:16pm
    res = 0
    for line in L:
        levels = list(map(int, line.split()))
        safe = False
        for i in range(len(levels)):
            popped = levels.pop(i)
            safe = is_safe(levels)
            if safe:
                break
            levels.insert(i, popped)
        if safe:
            res += 1

    return res

if __name__ == '__main__':
    L = util.strip_stdin()
    results = util.run(L, 1, 486, [simple_1])
    results += util.run(L, 2, 540, [simple_2])
    util.print_table(results)
