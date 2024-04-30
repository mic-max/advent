from sys import stdin

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
          'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def first_appear(x, search_strs):
    min_idx = -1
    min_pos = 100000000
    for idx, s in enumerate(search_strs):
        position = x.find(s)
        if position != -1 and position < min_pos:
            min_idx = idx
            min_pos = position
    return min_idx

sum = 0
for line in stdin:
    line = line.strip()

    n1 = first_appear(line, digits)
    sum += 10 * (n1 % 9) + 1

    n2 = first_appear(line[::-1], [x[::-1] for x in digits])
    sum += (n2 % 9) + 1

print(sum)
