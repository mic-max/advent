# Python
import math
import re
import typing

# Local
import util

def part_1(L: typing.List[str]) -> int:
    # R = [1, 0]
    # times = [] 
    # distances = []

    # for m in re.finditer(r'\d+', L[0]):
    #     times.append(int(m[0]))

    # for m in re.finditer(r'\d+', L[1]):
    #     distances.append(int(m[0]))

    # l0_colon = L[0].index(":")
    # p2_times = ""
    # for i in range(l0_colon + 1, len(L[0])):
    #     if L[0][i].isdigit():
    #         p2_times += L[0][i]
    # p2_time_int = int(p2_times)
    # print(p2_time_int)


    # print(times)
    # print(distances)

    # # use quadratic formula?
    # beat_product = 1
    # for x in zip(times, distances):
    #     time = x[0]
    #     distance = x[1]

    #     beats = 0
    #     for i in range(1, time - 1):
    #         x = (time - i) * i
    #         if x > distance:
    #             beats += 1
        
    #     beat_product *= beats

    # R[0] = beat_product
    # return R[0]
    return 0

def get_spaced_int(s: str) -> int:
    digits = ""
    for ch in s:
        if ch.isdigit():
            digits += ch
    return int(digits)

def get_spaced_int_2(s: str) -> int:
    num = 0
    for ch in s:
        if ch.isdigit():
            num = num * 10 + (ord(ch) - 48)
    return num

def quadratic_formula(a: float, b: float, c: float) -> typing.Tuple[float, float]:
    # if a == 0?
    import cmath

    d = (b ** 2) - (4 * a * c)
    divisor = a * 2
    sol1 = (-b - cmath.sqrt(d)) / divisor
    sol2 = (-b + cmath.sqrt(d)) / divisor
    return (sol1, sol2)

def brute_2_helper(time, distance):
    res = 1
    beats = 0
    for i in range(1, time - 1):
        x = (time - i) * i
        if x > distance:
            beats += 1
    res *= beats
    return res

def quadratic_2_helper(time, distance):
    return 0

def brute_2(L: typing.List[str]) -> int:
    time = get_spaced_int(L[0])
    distance = get_spaced_int(L[1])
    return brute_2_helper(time, distance)

def quadratic_2(L: typing.List[str]) -> int:
    time = get_spaced_int(L[0])
    distance = get_spaced_int(L[1])
    return quadratic_2_helper(time, distance)

def ways_to_beat_brute(time_allowed, best_distance):
    res = 0
    for i in range(1, time_allowed - 1):
        distance = (time_allowed - i) * i
        if distance > best_distance:
            res += 1
    return res

def ways_to_beat_two_pointer(time_allowed, best_distance):
    res = 0
    # TODO
    return res

def ways_to_beat_math(time_allowed, best_distance):
    root = math.sqrt(time_allowed ** 2 - 4 * best_distance)
    start = (time_allowed - root) // 2
    end = (time_allowed + root) / 2

    # // As we're using integer math we may need to adjust 1 step.
    if start * (time_allowed - start) > best_distance:
        start -= 1

    if end * (time_allowed - end) > best_distance:
        end += 1

    return end - start - 1

def part_1(L):
    times = [] 
    distances = []

    for m in re.finditer(r'\d+', L[0]):
        times.append(int(m[0]))

    for m in re.finditer(r'\d+', L[1]):
        distances.append(int(m[0]))

    res = 1
    for t, d in zip(times, distances):
        # res *= ways_to_beat_math(t, d)
        res *= ways_to_beat_brute(t, d)
    return res

if __name__ == '__main__':
    L = util.strip_stdin()
    results = util.run(L, 1, 440000, [part_1])
    # results += util.run(L, 2, 26187338, [brute_2, quadratic_2])
    util.print_table(results)
