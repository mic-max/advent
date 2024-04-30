from collections import defaultdict, deque
from math import prod
import sys
from datetime import datetime

modules = dict()
flips = defaultdict(int)
conjunctions = defaultdict(lambda: defaultdict(int))

def parse():
    for line in [x.strip() for x in sys.stdin]:
        tag = ''
        (name, _, *outputs) = line.replace(',', '').split()
        if name[0] in '%&':
            tag, name = name[0], name[1:]

        modules[name] = tag, outputs

        for output_name in outputs:
            conjunctions[output_name][name] = 0
            if output_name == 'rx':
                # rx = kj
                rx = name

rx_ins = {i: 0 for i in conjunctions[rx]}
print(rx_ins)
# &kj -> rx
# &ln -> kj
# &dr -> kj
# &vn -> kj
# &zx -> kj
# kj conjunction feeds into rx. input file only has one thing going into rx.
# kj conjunction receives inputs from ln, dr, vn, zx conjunctions
# 
# {'ln': 0, 'dr': 0, 'zx': 0, 'vn': 0}

presses = 0
counts = [0, 0]

while True:
    if presses == 1000:
        print(prod(counts))
    presses += 1

    if all(rx_ins.values()):
        # fewest number of button presses required to deliver a single low pulse to the module named rx

        print(rx_ins)
        print(prod(rx_ins.values()))
        break

    queue = deque()
    queue.append((None, 'broadcaster', 0))
    while queue:
        source, mod, pulse_in = queue.popleft()
        counts[pulse_in] += 1

        if mod not in modules: continue
        type, nexts = modules[mod]

        match type, pulse_in:
            case '', _:
                pulse_out = pulse_in
            case '%', 0:
                pulse_out = flips[mod] = not flips[mod]
            case '&', _:
                conjunctions[mod][source] = pulse_in
                pulse_out = not all(conjunctions[mod].values())

                if 'rx' in nexts:
                    for k, v in conjunctions[mod].items():
                        if v: rx_ins[k] = presses
            case _,_: continue

        for n in nexts:
            queue.append((mod, n, pulse_out))
