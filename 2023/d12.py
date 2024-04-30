import itertools
import sys
from functools import cache

@cache
def cgds(line, map):
    v = [len(x) for x in line.split('.') if x]
    return v == map

# take line and return a list of contiguous tuples [('?', 3), ('.', 1), ('#', 3)]
def transform(line, map):
    idx = 0
    cur = line[idx]

    for idx, x in enumerate(line):
        print(x)

    jdx = 0
    next_dot = line.find('.', idx + 1)
    next_hash = line.find('#', idx + 1)
    next_map = map[jdx]
    print("idx", idx)
    print("jdx", jdx)
    print("next_dot", next_dot)
    print("next_hash", next_hash)
    print("next_map", next_map)

def permute(input_string):
    permutations = []

    def generate_helper(current_string, index):
        if index == len(input_string):
            permutations.append(current_string)
            return

        if current_string[index] == '?':
            generate_helper(current_string[:index] + '.' + current_string[index + 1:], index + 1)
            generate_helper(current_string[:index] + '#' + current_string[index + 1:], index + 1)
        else:
            generate_helper(current_string, index + 1)

    generate_helper(input_string, 0)
    return permutations

def main():
    L = [line.strip() for line in sys.stdin]

    r1 = 1
    for line in L:
        # springs = line.split(" ")[0]
        springs = (line.split(" ")[0] + '?') * 5
        springs = springs[:-1]
        damaged = [int(x) for x in line.split(" ")[1].split(',')]
        damaged = [element for element in damaged for _ in range(5)]

        for perm in permute(springs):
            if cgds(perm, damaged):
                r1 += 1
    print(r1)


if __name__ == '__main__':
    main()
