# Python
import collections

# Local
import util

def simple_1(L):
    # took me 6 minutes 12:15pm to 12:21pm on dec 2.
    lefts = []
    rights = []
    res = 0
    for line in L:
        l, r = map(int, line.split())
        lefts.append(l)
        rights.append(r)
    lefts.sort()
    rights.sort()

    for l, r in zip(lefts, rights):
        delta = abs(r - l)
        res += delta

    return res

def simple_2(L):
    # took me an additional 5 minutes. finished at 12:26pm
    lefts = []
    rights = collections.Counter()
    res = 0
    for line in L:
        l, r = map(int, line.split())
        lefts.append(l)
        rights[r] += 1

    for l in lefts:
        res += l * rights[l]

    return res

if __name__ == '__main__':
    L = util.strip_stdin()
    results = util.run(L, 1, 1889772, [simple_1])
    results += util.run(L, 2, 23228917, [simple_2])
    util.print_table(results)
