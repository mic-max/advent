import math
import re
import statistics
import sys
import time

import ahocorasick
import num2words

P1 = 54634
P2 = 53855

def simple(L, part_two = False):
    res = 0
    if part_two:
        digits = list('123456789')
        for i in range(1, 10):
            digits.append(num2words.num2words(i))
        for line in L:
            min_value = 0
            min_pos = len(line) - 1
            max_value = 0
            max_pos = 0

            for i, num in enumerate(digits):
                if (pos := line.find(num, 0, min_pos + 1)) != -1:
                    min_pos = pos
                    min_value = (i % 9) + 1

                if (pos2 := line.rfind(num, max_pos)) != -1:
                    max_pos = pos2
                    max_value = (i % 9) + 1

            res += min_value * 10
            res += max_value
    else:
        for line in L:
            for c in line:
                if c.isdigit():
                    res += (ord(c) - 48) * 10
                    break

            for c in reversed(line):
                if c.isdigit():
                    res += ord(c) - 48
                    break
    return res

def regex(L, part_two = False):
    nums = {}
    for i in range(1, 10):
        nums[str(i)] = i
        if part_two:
            nums[num2words.num2words(i)] = i

    res = 0
    for line in L:
        m = re.search("|".join(nums.keys()), line)
        res += nums[m[0]] * 10

        m = re.search("|".join([x[::-1] for x in nums.keys()]), line[::-1])
        res += nums[m[0][::-1]]
    return res

def aho_corasick(L, part_two = False):
    a1 = ahocorasick.Automaton()
    a2 = ahocorasick.Automaton()

    for i in range(1, 10):
        a1.add_word(str(i), i)
        a2.add_word(str(i), i)
    
        if part_two:
            word = num2words.num2words(i)
            a1.add_word(word, i)
            a2.add_word(word[::-1], i)

    a1.make_automaton()
    a2.make_automaton()

    res = 0
    for line in L:
        for _, x in a1.iter(line):
            res += x * 10
            break

        for _, x in a2.iter(line[::-1]):
            res += x
            break

    return res

def run(name, function, fastest = None, part_two = False):
    start = time.perf_counter()
    res = function(L, part_two)
    elapsed = time.perf_counter() - start
    print(f"| {name:15} | {elapsed:.6f} | {1 if not fastest else elapsed / fastest:.2f} |")
    assert res == (P2 if part_two else P1)
    return elapsed

if __name__ == "__main__":
    L = [line.strip() for line in sys.stdin]

    print(f"Average Length: {statistics.mean([len(x) for x in L])}")
    print(f"Median Length: {statistics.median([len(x) for x in L])}")
    print(f"Min Length: {min([len(x) for x in L])}")
    print(f"Max Length: {max([len(x) for x in L])}")

    print("| Part 1      | Time     | Times Slower |")
    print("| ------------ | -------- | ------------ |")
    fastest_p1 = run("Simple", simple, None)
    run("Aho-Corasick", aho_corasick, fastest_p1)
    run("Regex", regex, fastest_p1)

    print("| Part 2      | Time     | Times Slower |")
    print("| ------------ | -------- | ------------ |")
    fastest_p2 = run("Aho-Corasick", aho_corasick, None, True)
    run("Regex", regex, fastest_p2, True)
    run("Simple", simple, fastest_p2, True)
