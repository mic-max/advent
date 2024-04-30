import sys
import re

R = [0, 0]
L = [line for line in sys.stdin]
S = []
M = []

def flatten(x):
    result = []
    for v in x:
        result.extend(v[0:2])
    return result

# merges two sorted mappings
def merge(a, b):
    idx1 = 0
    idx2 = 0
    result = []
    flata = flatten(a)
    flatb = flatten(b)
    print('flata', flata)
    print('flatb', flatb)


    while(idx1 < len(a) and idx2 < len(b)):
        if a[idx1] <= b[idx2]:
            result.append()
        else:
            pass

    return result


# Seeds
for m in re.finditer(r'(\d+) (\d+)', L[0]):
    n1 = int(m[1]) # start range
    n2 = int(m[2]) + n1 - 1 # end range inclusive
    S.append([n1, n2])
S.sort(key=lambda x: x[0])

m_idx = -1
for line in L[2:]:
    # Process Map Signature
    m = re.search(r'\w+-to-\w+ map:', line)
    if m:
        m_idx += 1
        M.append([])
        continue

    # Process Map Data
    m = re.search(r'(\d+) (\d+) (\d+)', line)
    if m:
        n1 = int(m.group(1))
        n2 = int(m.group(2))
        n3 = int(m.group(3))
        inc = n1 - n2
        M[m_idx].append([n2, n2 + n3 - 1, inc])
        continue

    # End of Current Map
    if line == '\n':
        M[m_idx].sort(key=lambda x: x[0])

# print('seeds:', S)
# for x in M:
#     print('*' * 40)
#     for r in x:
#         # split S into new ranges
#         print(r)

# print(M)
merge(M[0], M[1])
