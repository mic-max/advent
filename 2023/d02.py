import collections
import functools
import operator
import sys
import statistics
import time

P1 = 2348
P2 = 76008

def part1(L, part_two = False):
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

def part2(L, part_two = False):
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

def run(name, function, fastest = None, part_two = False):
    start = time.perf_counter()
    res = function(L, part_two)
    elapsed = time.perf_counter() - start
    print(f"| {name:15} | {elapsed:.6f} |")
    assert res == (P2 if part_two else P1)
    return elapsed

if __name__ == "__main__":
    L = [line.strip() for line in sys.stdin]
    
    print(f"Average Reveals: {statistics.mean([x.count(';') for x in L])}")
    print(f"Median Reveals: {statistics.median([x.count(';') for x in L])}")
    print(f"Min Reveals: {min([x.count(';') for x in L])}")
    print(f"Max Reveals: {max([x.count(';') for x in L])}")
    
    print("| Part Number  | Time     |")
    print("| ------------ | -------- |")
    p1_elapsed = run("Part 1", part1, None)
    p2_elapsed = run("Part 2", part2, None, True)

