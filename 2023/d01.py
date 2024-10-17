# Python
import math
import re

# PIP
import ahocorasick
import num2words

# Local
import util

def simple_1(L):
    res = 0
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

def simple_2(L):
    res = 0
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
    return res

def regex_1(L):
    nums = {}
    for i in range(1, 10):
        nums[str(i)] = i

    res = 0
    for line in L:
        m = re.search("|".join(nums.keys()), line)
        res += nums[m[0]] * 10
        m = re.search("|".join([x[::-1] for x in nums.keys()]), line[::-1])
        res += nums[m[0][::-1]]
    return res

def regex_2(L):
    nums = {}
    for i in range(1, 10):
        nums[str(i)] = i
        nums[num2words.num2words(i)] = i

    res = 0
    for line in L:
        m = re.search("|".join(nums.keys()), line)
        res += nums[m[0]] * 10
        m = re.search("|".join([x[::-1] for x in nums.keys()]), line[::-1])
        res += nums[m[0][::-1]]
    return res

def aho_corasick_1(L):
    a1 = ahocorasick.Automaton()
    a2 = ahocorasick.Automaton()
    for i in range(1, 10):
        a1.add_word(str(i), i)
        a2.add_word(str(i), i)
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

def aho_corasick_2(L):
    a1 = ahocorasick.Automaton()
    a2 = ahocorasick.Automaton()
    for i in range(1, 10):
        a1.add_word(str(i), i)
        a2.add_word(str(i), i)
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

if __name__ == '__main__':
    L = util.strip_stdin()
    results = util.run(L, 1, 54634, [simple_1, regex_1, aho_corasick_1])
    results += util.run(L, 2, 53855, [simple_2, regex_2, aho_corasick_2])
    util.print_table(results)
