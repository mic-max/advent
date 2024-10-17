import operator
import sys
import tabulate
import time

def run(L, part, expected, functions):
    results = []

    for f in functions:
        start = time.perf_counter()
        res = f(L)
        elapsed = time.perf_counter() - start
        results.append([f.__name__, part, elapsed, "🔥", res, "✔" if res == expected else "✖"])

    fastest = min([r[2] for r in results])
    for r in results:
        if r[2] != fastest:
            r[3] = f"{r[2] / fastest:.2f}x 🐌"

    # Sort by elapsed time
    results.sort(key=operator.itemgetter(2))
    return results

def print_table(table):
    headers = ["Name", "Part", "Time (s)", "Slower Than Best", "Result", "Correct"]
    res = tabulate.tabulate(table, headers=headers, tablefmt="github")
    print(res)

def strip_stdin():
    return [line.strip() for line in sys.stdin]