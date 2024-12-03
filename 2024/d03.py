# Python
import re

# Local
import util

def simple_1(L):
    res = 0
    for line in L:
        for m in re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', line):
            x = int(m.group(1))
            y = int(m.group(2))
            res += x * y

    return res

def simple_2(L):
    res = 0
    
    L = "".join(L)
    for m in re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', "".join(L)):
        x = int(m.group(1))
        y = int(m.group(2))

        i = m.start()
        recent_do = L.rfind("do()", 0, i)
        recent_dont = L.rfind("don't()", 0, i)
        if recent_dont == -1 or recent_do > recent_dont:
            res += x * y

    return res

if __name__ == '__main__':
    L = util.strip_stdin()
    results = util.run(L, 1, 189600467, [simple_1])
    results += util.run(L, 2, 107069718, [simple_2])
    util.print_table(results)


