M = [[] for _ in range(10)]

def can_move(y, x, moves):
    paths = []
    # down
    if M[y+1][x] != '#' and moves[-1] not in '><^':
        paths.append((1, 0))
    
    return paths
