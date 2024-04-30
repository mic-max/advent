import sys

# B = [[]] * 256
B = [ [] for _ in range(256) ]

def hasher(str):
    r = 0
    for i, ch in enumerate(str):
        ascii = ord(ch)
        r += ascii
        r *= 17
        r %= 256
    return r

def show_boxes():
    for i, b in enumerate(B):
        if len(b) > 0:
            print(f'Box {i}: ', end='')
            for bb in b:
                print(f'[{bb[0]} {bb[1]}]', end=' ')
            print()
    print()

def main():
    L = [x.strip().split(",") for x in sys.stdin][0]
    
    for x in L:
        if x.endswith('-'):
            label = x[:-1]
            label_hash = hasher(label)
            for i, x in enumerate(B[label_hash]):
                if x[0] == label:
                    B[label_hash].pop(i)
                    break
        elif x[-2] == '=':
            parts = x.split("=")
            label = parts[0]
            focal_length = int(parts[1])
            label_hash = hasher(label)
            replaced = False
            for i, x in enumerate(B[label_hash]):
                if x[0] == label:
                    B[label_hash][i] = (label, focal_length)
                    replaced = True
                    break
            if not replaced:
                B[label_hash].append((label, focal_length))

    p2 = 0
    for i, b in enumerate(B, 1):
        for j, x in enumerate(b, 1):
            power = i * j * x[1]
            p2 += power
    print(p2)

if __name__ == '__main__':
    main()
