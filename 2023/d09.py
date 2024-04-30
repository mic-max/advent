import sys

def gen_diffs(a):
    res = []
    for idx in range(len(a) - 1):
        res.append(a[idx + 1] - a[idx])
    return res

def main():
    L = [line.strip() for line in sys.stdin]
    X = []
    total = 0

    for line in L:
        line_arr = [int(x) for x in line.split()]
        X.append(line_arr)

    for oasis in X:
        state = oasis
        states = [ state ]
        while not all(x == 0 for x in state):
            state = gen_diffs(state)
            states.append(state)

        # part 1
        # for i in reversed(range(len(states) - 1)):
        #     x = states[i][-1] + states[i + 1][-1]
        #     states[i].append(x)
        #     print(states[i])
        # value = states[0][-1]

        # part 2
        for i in reversed(range(len(states) - 1)):
            x = states[i][0] - states[i + 1][0]
            states[i].insert(0, x)
            # print(states[i])
        value = states[0][0]

        total += value
    print(total)

if __name__ == '__main__':
    main()
