# Python
import re
import sys

# PIP
import ahocorasick

# Local
import util

def slicing_1_pinw_helper(line):
    matches = 0

    colon_index = line.index(':')
    pipe_index = line.index('|', colon_index)
    win_string = line[colon_index + 1:pipe_index]

    line += ' '
    for i in range(pipe_index + 1, len(line) - 1, 3):
        if line[i:i + 4] in win_string:
            matches += 1

    return matches

def slicing_1_pinw(L):
    return frame_1(L, slicing_1_pinw_helper)

def slicing_1_winp_helper(line):
    matches = 0

    colon_index = line.index(':')
    pipe_index = line.index('|', colon_index)
    mine_string = line[pipe_index + 1:] + ' '

    for part in line[colon_index + 1:pipe_index - 1].split():
        if f" {part} " in mine_string:
            matches += 1

    return matches

def slicing_1_winp(L):
    return frame_1(L, slicing_1_winp_helper)

def regex_1_pinw(L):
    def count_matches_regex(line):
        wins = set()
        matches = 0

        colon_index = line.index(':')
        pipe_index = line.index('|', colon_index)
        win_string = line[colon_index + 1:pipe_index]

        for m in re.finditer(r'\d+', win_string):
            wins.add(m[0])

        for m in re.finditer(r'\d+', line[pipe_index + 1:]):
            if m[0] in wins:
                matches += 1
        
        return matches
    return frame_1(L, count_matches_regex)

def regex_1_winp(L):
    def count_matches_regex(line):
        mine = set()
        matches = 0

        colon_index = line.index(':')
        pipe_index = line.index('|', colon_index)
        win_string = line[colon_index + 1:pipe_index]

        for m in re.finditer(r'\d+', line[pipe_index + 1:]):
            mine.add(m[0])

        for m in re.finditer(r'\d+', win_string):
            if m[0] in mine:
                matches += 1
        
        return matches
    return frame_1(L, count_matches_regex)

def aho_corasick_1_pinw(L):
    def count_matches_aho_corasick(line):
        matches = 0

        colon_index = line.index(':')
        pipe_index = line.index('|', colon_index)
        win_string = line[colon_index + 2:pipe_index - 1]

        a1 = ahocorasick.Automaton()
        for i, win in enumerate(win_string.split()):
            a1.add_word(win, True)
        a1.make_automaton()

        mine_string = line[pipe_index + 2:]
        for x in mine_string.split():
            if a1.get(x, False):
                matches += 1
        
        return matches
    return frame_1(L, count_matches_aho_corasick)

def aho_corasick_1_winp(L):
    def count_matches_aho_corasick2(line):
        matches = 0

        colon_index = line.index(':')
        pipe_index = line.index('|', colon_index)
        mine_string = line[pipe_index + 1:] + ' '

        a1 = ahocorasick.Automaton()
        for i, mine in enumerate(mine_string.split()):
            a1.add_word(mine, True)
        a1.make_automaton()

        win_string = line[colon_index + 2:pipe_index - 1]
        for x in win_string.split():
            if a1.get(x, False):
                matches += 1
        
        return matches

    return frame_1(L, count_matches_aho_corasick2)

def frame_1(L, helper):
    res = 0
    for line in L:
        if matches := helper(line):
            res += 2 ** (matches - 1)
    return res

def part_2(L):
    cards = []

    for line in L:
        matches = slicing_1_winp_helper(line)
        cards.append({
            'total': 0 if matches else 1,
            'matches': matches
        })

    res = 0
    for j in range(len(L) - 1, -1, -1):
        if not cards[j]["total"]:
            cards[j]['total'] = 1
            for c in range(j + 1, j + cards[j]['matches'] + 1):
                cards[j]['total'] += cards[c]['total']
        res += cards[j]['total']
    return res

if __name__ == '__main__':
    L = [line.strip() for line in sys.stdin]
    results = util.run(L, 1, 26426, [slicing_1_pinw, slicing_1_winp, aho_corasick_1_pinw, aho_corasick_1_winp, regex_1_pinw, regex_1_winp])
    results += util.run(L, 2, 6227972, [part_2])
    util.print_table(results)
