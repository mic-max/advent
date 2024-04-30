import collections
import copy
import sys
import math

def label_to_int(label):
    return label[0] * 26 + label[1]

def main():
    L = [x.strip() for x in sys.stdin]

    M = {} # mappings
    B = collections.deque() # broadcast
    S = {} # states

    for y, line in enumerate(L):
        if line.startswith("broadcaster"):
            start = line.find("-> ") + 3
            for x in line[start:].split(","):
                B.append(("broadcaster", x.strip(), False))
            continue

        name = line[1:line.find(" ")]
        if line.startswith("%"):
            S[name] = False
        elif line.startswith("&"):
            S[name] = {} # most recent pulse from each connected input, defaults to low
        start = line.find("-> ") + 3
        M[name] = [x.strip() for x in line[start:].split(",")]

    for name, s in S.copy().items():
        if type(s) is bool:
            continue
        # we have the name of a conjunction module
        for name2, m in M.items():
            if name in m:
                S[name][name2] = False

    presses = 0
    counts = [0, 0]

    while True:
        if presses == 1000:
            print(math.prod(counts))
        presses += 1

        BB = copy.deepcopy(B)
        # PERF: simply add ('button', 'broadcaster' False) to BB
        # print("button -low-> broadcaster")
        # lows += 1
        while BB:
            sender, receiver, pulse = BB.popleft()
            # print(i)
            if i % 1000 == 0:
                print(i)
            if receiver == 'rx' and not pulse:
                print(i)
                exit()
            elif receiver not in S:
                pass
            elif type(S[receiver]) is bool:
                if not pulse:
                    S[receiver] = not S[receiver]
                    for m in M[receiver]:
                        BB.append((receiver, m, S[receiver]))
            else:
                S[receiver][sender] = pulse
                pulse = any(not x for x in S[receiver].values())
                for m in M[receiver]:
                    BB.append((receiver, m, pulse))
    # p1 = lows * highs
    # print(lows)
    # print(highs)
    # print('Part 1:', p1)

    # for name, state in S.items():
    #     if state is False:
    #         print(f"{name} = OFF")
    #     if state is True:
    #         print(f"{name} = ON")

if __name__ == '__main__':
    main()

# p1. 11685999 too low (sample input)
# p1. 976312821 too high
# p1. 976242432 too high
# p1. 949764474 correct.
