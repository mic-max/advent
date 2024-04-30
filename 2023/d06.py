import sys
import re

R = [1, 0]
L = [line for line in sys.stdin]

T = [] 
D = []

for m in re.finditer(r'\d+', L[0]):
    T.append(int(m[0]))

for m in re.finditer(r'\d+', L[1]):
    D.append(int(m[0]))

T = [int(''.join([str(x) for x in T]))]
D = [int(''.join([str(x) for x in D]))]

# use quadratic formula?
beat_product = 1
for x in zip(T, D):
    time = x[0]
    distance = x[1]

    beats = 0
    for i in range(1, time - 1):
        x = (time - i) * i
        if x > distance:
            beats += 1
    
    beat_product *= beats

R[0] = beat_product

print(R)
