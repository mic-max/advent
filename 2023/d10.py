import sys

LEFT = (0, -1, '-FL')
RIGHT = (0, 1, '-7J')
UP = (-1, 0, '|JL')
DOWN = (1, 0, '|F7')

DIRS = {
    '-': [LEFT, RIGHT],
    'F': [DOWN, RIGHT],
    '7': [DOWN, LEFT],
    '|': [UP, DOWN],
    'J': [UP, LEFT],
    'L': [UP, RIGHT],
    '.': [],
    'S': [LEFT, RIGHT, UP, DOWN]
}

DIRXNS = [LEFT, RIGHT, UP, DOWN]
route = []

def nav(map, pos, path):
    opp = opposite(path)
    for move in moves:
        if move[:2] != opp and map[pos[0] + move[0]][pos[1] + move[1]] in move[2]:
            return move

def opposite(direction):
    if direction == LEFT: return LEFT
    if direction == RIGHT: return RIGHT
    if direction == UP: return DOWN
    if direction == DOWN: return UP
    else: return (0, 0)

def s(map, pos, direction):
    return map[pos[0] + direction[0]][pos[1] + direction[1]]

def main():
    # Padded Map with ground spaces
    L = [f'.{line.strip()}.' for line in sys.stdin]
    L.insert(0, '.' * len(L[0]))
    L.append('.' * len(L[0]))

    # Find starting position
    pos = list(filter(lambda x: x[1] != -1, ((y, x.find('S')) for y, x in enumerate(L))))[0]
    route.append(pos)
    print('Start:', pos)
    # check if spot to the right can go left
    path = [x for x in DIRXNS if x in DIRS[pos] and opposite(x) in DIRS[s(L, pos, x)]][0]

    while True:
        path = nav(L, pos, path)
        if path is None:
            break
        pos = (pos[0] + path[0], pos[1] + path[1])
        route.append(pos)

    max_route = len(route) / 2
    print(max_route)

    # if L[y][x + 1] in '-7J':
    # so we start at the S
    # take the first path we find
    # take a step and add it to our graph
    # the next step we need to make sure we don't double back. (check if position is in graph)
    #   if last direction was left. don't go right.
    # if we have a rout

    # paths = find_path(L, y, x, coming)
    # print("Paths:", paths)
    # for p in paths:
    #     y1 = y + p[0]
    #     x1 = x + p[1]
    #     print("  Direction:", p)
    #     print(f"  y = {y1}, x = {x1}")
    #     coming = flip(p)
    #     pathsx = find_path(L, y1, x1, coming)
    #     print(pathsx)
    # print(paths)


if __name__ == '__main__':
    main()
