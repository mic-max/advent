# Python
import collections
import functools
import operator

# Local
import util

def part1(L):
    res = 0
    max_counts = { 'red': 12, 'green': 13, 'blue': 14 }

    for i, line in enumerate(L, 1):
        skip_game = False
        for setx in line[line.index(':') + 1:].strip().split(';'):
            if skip_game:
                break
            for pair in setx.strip().split(','):
                parts = [x.strip() for x in pair.split()]
                count, colour = int(parts[0]), parts[1]

                if count > max_counts[colour]:
                    skip_game = True
                    break

        if not skip_game:
            res += i
    return res

def part2(L):
    res = 0

    for idx, line in enumerate(L, 1):
        counts = collections.defaultdict(int)

        for setx in line[line.index(':') + 1:].strip().split(';'):
            for pair in setx.strip().split(','):
                parts = [x.strip() for x in pair.split()]
                count, colour = int(parts[0]), parts[1]
                counts[colour] = max(count, counts[colour])

        res += functools.reduce(operator.mul, counts.values(), 1)
    return res

if __name__ == "__main__":
    L = util.strip_stdin()
    results = util.run(L, 1, 2348, [part1])
    results += util.run(L, 2, 76008, [part2])
    util.print_table(results)
