import time

def run(name, function, L, expected, fastest = None, part_two = False):
    start = time.perf_counter()
    res = function(L, part_two)
    elapsed = time.perf_counter() - start
    print(f"| {name} | {elapsed:.6f} |")
    assert res == expected
    return elapsed