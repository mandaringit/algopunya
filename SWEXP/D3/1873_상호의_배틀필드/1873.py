import sys

sys.stdin = open('input.txt', 'r')


class Tank:

    def __init__(self, x, y, direction, H, W, maps):
        self.x = x
        self.y = y
        self.direction = direction
        self.map_height = H
        self.map_width = W
        self.maps = maps

    def check_range(self, x, y):
        return 0 <= x < self.map_height and 0 <= y < self.map_width

    def move(self):
        self.maps[self.x][self.y] = '.'

        if self.direction == '^':
            self.x -= 1
        elif self.direction == 'v':
            self.x += 1
        elif self.direction == '<':
            self.y -= 1
        elif self.direction == '>':
            self.y += 1

        self.maps[self.x][self.y] = self.direction

    def shooting(self):

        bullet_x = self.x
        bullet_y = self.y

        while True:
            if self.direction == '^':
                bullet_x -= 1
            elif self.direction == 'v':
                bullet_x += 1
            elif self.direction == '<':
                bullet_y -= 1
            elif self.direction == '>':
                bullet_y += 1

            # 범위 안이고
            if self.check_range(bullet_x, bullet_y):
                bullet_location = self.maps[bullet_x][bullet_y]
                if bullet_location in ['.', '-']:
                    pass
                elif bullet_location == '#':
                    break
                elif bullet_location == '*':
                    self.maps[bullet_x][bullet_y] = '.'
                    break
            else:
                break

    def command(self, cmd):
        if cmd == 'U':
            self.direction = '^'
            self.maps[self.x][self.y] = '^'
            nx = self.x - 1
            if self.check_range(nx, self.y) and self.maps[nx][self.y] == '.':
                self.move()
        elif cmd == 'D':
            self.direction = 'v'
            self.maps[self.x][self.y] = 'v'
            nx = self.x + 1
            if self.check_range(nx, self.y) and self.maps[nx][self.y] == '.':
                self.move()
        elif cmd == 'L':
            self.direction = '<'
            self.maps[self.x][self.y] = '<'
            ny = self.y - 1
            if self.check_range(self.x, ny) and self.maps[self.x][ny] == '.':
                self.move()
        elif cmd == 'R':
            self.direction = '>'
            self.maps[self.x][self.y] = '>'
            ny = self.y + 1
            if self.check_range(self.x, ny) and self.maps[self.x][ny] == '.':
                self.move()
        elif cmd == 'S':
            self.shooting()


def get_starting_point(game_map):
    start_x = 0
    start_y = 0
    direction = ''
    for i in range(H):
        for j in range(W):
            if game_map[i][j] in ['^', '<', '>', 'v']:
                start_x = i
                start_y = j
                direction = game_map[i][j]
                return start_x, start_y, direction

    return None


T = int(input())

for tc in range(1, T + 1):
    H, W = map(int, input().split())

    game_map = [list(input()) for _ in range(H)]

    N = int(input())
    cmds = list(input())

    start_x, start_y, direction = get_starting_point(game_map)

    tank = Tank(start_x, start_y, direction, H, W, game_map)

    for cmd in cmds:
        tank.command(cmd)

    print("#{} ".format(tc), end='')
    for row in tank.maps:
        print(''.join(row))
