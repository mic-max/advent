import sys

def replacer(s, newstring, index):
    return s[:index] + newstring + s[index + 1:]

def get_column(p, i):
    result = ''

    for line in p:
        result += line[i]

    return result

def find_hreflect(p):
    result = []
    middles = []
    for i, line in enumerate(p):
        if i >= len(p) - 1:
            break
        if line == p[i + 1]:
            middles.append(i)

    for mid in middles:
        front = p[:mid][::-1]
        back = p[mid+2:]
        sames = all(a == b for a, b in zip(front, back))
        if sames:
            result.append(mid + 1)

    return result

def find_vreflect(p):
    result = []
    middles = []
    for i in range(len(p[0]) - 1):
        c1 = get_column(p, i)
        c2 = get_column(p, i + 1)
        if c1 == c2:
            middles.append(i)

    for mid in middles:
        front = [get_column(p, i) for i in range(mid)][::-1]
        back = [get_column(p, i) for i in range(mid+2, len(p[0]))]
        sames = all(a == b for a, b in zip(front, back))
        if sames:
            result.append(mid + 1)

    return result

def main():
    L = [x.strip().split("\n") for x in sys.stdin.read().split("\n\n")]
    R = []

    p1 = 0
    for p in L:
        hr = find_hreflect(p)
        if hr:
            score = 100 * hr[0]
            R.append(score)
            p1 += score
            continue
        vr = find_vreflect(p)
        if vr:
            score = vr[0]
            R.append(score)
            p1 += score
            continue

    p2 = 0
    for idx, p  in enumerate(L):
        og_reflect = R[idx]
        plen = len(p) * len(p[0])
        stop_checking = False
        for i in range(plen):
            if stop_checking:
                break
            smudged = p.copy()
            y = i // len(smudged[0])
            x = i % len(smudged[0])
            newc = '.' if smudged[y][x] == '#' else '#'
            smudged[y] = replacer(smudged[y], newc, x)

            for hr in find_hreflect(smudged):
                score = hr * 100
                if score != og_reflect:
                    p2 += score
                    stop_checking = True
            for vr in find_vreflect(smudged):
                score = vr
                if score != og_reflect:
                    p2 += score
                    stop_checking = True
    print(p2)

if __name__ == '__main__':
    main()
