from sys import stdin
from operator import mul
from functools import reduce

result = 0
max_counts = { 'red': 12, 'green': 13, 'blue': 14 }

for idx, line in enumerate(stdin, 1):
    good_so_far = True
    min_count = { 'red': 0, 'green': 0, 'blue': 0 }

    for setx in line[line.index(':') + 1:].strip().split(';'):
        for pair in setx.strip().split(','):
            count = int(pair.strip().split()[0])
            color = pair.strip().split()[1]

            min_count[color] = max(count, min_count[color])

            if count > max_counts[color]:
                good_so_far = False

    # part 2.
    power_value = reduce(mul, min_count.values(), 1)
    result += power_value # pt 2

    # part 1.
    # if good_so_far:
    #     result += idx

print(result)
