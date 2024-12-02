# Python
import operator
import sys
import tabulate
import time
import typing

def run(L: typing.List[str], part: int, expected: int, functions: typing.List[any]) -> typing.List[any]:
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

def print_table(table: typing.List[any]):
    headers = ["Name", "Part", "Time (s)", "Slower Than Best", "Result", "Correct"]
    res = tabulate.tabulate(table, headers=headers, tablefmt="github")
    print(res)

def strip_stdin() -> typing.List[str]:
    return [line.strip() for line in sys.stdin]