import sys
import functools
import collections

L = [line for line in sys.stdin]

FIVE_KIND = 6
FOUR_KIND = 5
FULL_HOUSE = 4
THREE_KIND = 3
TWO_PAIR = 2
PAIR = 1

def five_kind(h):
    return 5 in h.values()

def four_kind(h):
    return 4 in h.values()

def full_house(h):
    return 3 in h.values() and 2 in h.values()

def three_kind(h):
    return 3 in h.values()

def two_pair(h):
    pair_count = 0
    for x in h:
        if h[x] == 2:
            pair_count += 1
    return pair_count == 2

def pair(h):
    return 2 in h.values()

def hand_rank(h):
    if five_kind(h):
        return FIVE_KIND
    elif four_kind(h):
        if h.get('J') in (1, 4):
            return FIVE_KIND
        return FOUR_KIND
    elif full_house(h):
        if h.get('J') in (2, 3):
            return FIVE_KIND
        return FULL_HOUSE
    elif three_kind(h):
        if h.get('J') in (1, 3):
            return FOUR_KIND
        return THREE_KIND
    elif two_pair(h):
        if h.get('J') == 2:
            return FOUR_KIND
        elif h.get('J') == 1:
            return FULL_HOUSE
        return TWO_PAIR
    elif pair(h):
        if h.get('J') in (1, 2):
            return THREE_KIND
        return PAIR
    elif 'J' in h:
        return PAIR
    return 0

def compare_hands(a, b):
    cards = 'J23456789TQKA' # Note: Moved J to beginning for Part 2.
    h1, _, _, r1 = a
    h2, _, _, r2 = b

    if r1 != r2:
        return r1 - r2

    for c1, c2 in zip(h1, h2):
        if c1 != c2:
            return cards.index(c1) - cards.index(c2)
    return 0

H = []

for line in L:
    hand = line[:5]
    bid = int(line[6:])
    dic = collections.Counter(hand)
    rank = hand_rank(dic)
    H.append((hand, bid, dic, rank))

H = sorted(H, key=functools.cmp_to_key(compare_hands))

winnings = 0
for idx, h in enumerate(H, 1):
    winnings += idx * h[1]

print(winnings)
