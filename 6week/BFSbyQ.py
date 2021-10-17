from circularQueueclass import CircularQueue


def isValidPos(x, y):
    if x < 0 or y < 0 or x >= MAP_SIZE or y >= MAP_SIZE:
        return False
    else:
        return map[y][x] == '0' or map[y][x] == 'x'


def BFS():
    que = CircularQueue()
    que.enqueue((0, 1))
    print('BFS: ')

    while not que.isEmpty():
        here = que.dequeue()
        print(here, end='->')
        x, y = here
        if map[y][x] == 'x':
            return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y - 1): que.enqueue((x, y - 1))
            if isValidPos(x, y + 1): que.enqueue((x, y + 1))
            if isValidPos(x - 1, y): que.enqueue((x - 1, y))
            if isValidPos(x + 1, y): que.enqueue((x + 1, y))
    return False


map = [['1', '1', '1', '1', '1', '1'],
       ['e', '0', '1', '0', '0', '1'],
       ['1', '0', '0', '0', '1', '1'],
       ['1', '0', '1', '0', '1', '1'],
       ['1', '0', '1', '0', '0', 'x'],
       ['1', '1', '1', '1', '1', '1']]
MAP_SIZE = 6
result = BFS()
if result:
    print(' --> 미로탐색 성공')
else:
    print(' --> 미로탐색 실패')
