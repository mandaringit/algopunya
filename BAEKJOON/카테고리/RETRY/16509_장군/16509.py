import sys

sys.stdin = open('input.txt', 'r')


class Sang:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_not_wall_or_something(self, nx, ny, move_count):
        global wang_loc

        if 0 <= nx < 9 and 0 <= ny < 10:
            if move_count <= 2 and (nx, ny) == wang_loc:  # 세번 움직이기 전에 왕이 있으면
                return False
            return True
        else:
            return False

    def move(self, direction):

        # 상 상좌 상좌
        if direction == 0:
            d = [(-1, 0), (-1, -1), (-1, -1)]
        # 상 상우 상우
        elif direction == 1:
            d = [(-1, 0), (-1, 1), (-1, 1)]
        # 하 하좌 하좌
        elif direction == 2:
            d = [(1, 0), (1, -1), (1, -1)]
        # 하 하우 하우
        elif direction == 3:
            d = [(1, 0), (1, 1), (1, 1)]
        # 좌 상좌 상좌
        elif direction == 4:
            d = [(0, -1), (-1, -1), (-1, -1)]
        # 좌 하좌 하좌
        elif direction == 5:
            d = [(0, -1), (1, -1), (1, -1)]
        # 우 상우 상우
        elif direction == 6:
            d = [(0, 1), (-1, 1), (-1, 1)]
        # 우 하우 하우
        elif direction == 7:
            d = [(0, 1), (1, 1), (1, 1)]

        _x = self.x
        _y = self.y

        moving = True
        move_count = 1
        for dx, dy in d:
            nx = _x + dx
            ny = _y + dy

            if not self.is_not_wall_or_something(nx, ny, move_count):  # 뭔가 있어서 움직일 수 없으면
                moving = False

            _x = nx
            _y = ny
            move_count += 1

        if moving:
            self.x = _x
            self.y = _y

            return True

        return False


def BFS(sang, count):
    global wang_loc

    if [sang.x, sang.y] == wang_loc:
        print(count)
        return

    q = [(sang, 0)]

    while q:

        prev_sang, count = q.pop(0)

        for i in range(8):
            new_sang = Sang(prev_sang.x, prev_sang.y)
            is_moved = new_sang.move(i)

            if is_moved:
                if [new_sang.x, new_sang.y] == wang_loc:
                    print(count + 1)
                    return
                else:
                    q.append((new_sang, count + 1))


sang_loc = list(map(int, input().split()))
wang_loc = list(map(int, input().split()))

sang = Sang(sang_loc[0], sang_loc[1])
visited = [[0] * 10 for _ in range(10)]
BFS(sang, 0)
