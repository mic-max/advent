import sys
from re import finditer

R = [0, 0]
L = [line for line in sys.stdin]
cards = {}

def calc_total(card):
    if card['total']:
        return card['total']

    total = 1
    prizes = card['cards_won']
    for c in prizes:
        total += calc_total(cards[c])
 
    card['total'] = total
    return total

for idx, line in enumerate(L):
    wins = set()
    mine = set()
    parts = line.split('|')

    for m in finditer(r'\d+', parts[0].split(':')[1]):
        wins.add(int(m[0]))

    for m in finditer(r'\d+', parts[1]):
        mine.add(int(m[0]))

    match = wins.intersection(mine)
    if match:
        R[0] += 2 ** (len(match) - 1)

    cards_won = [n for n in range(idx + 1, idx + len(match) + 1)]
    cards[idx] = {
        'total': None if len(cards_won) > 0 else 1,
        'cards_won': cards_won
    }

for i in reversed(range(0, idx + 1)):
    R[1] += calc_total(cards[i])

print(R)
