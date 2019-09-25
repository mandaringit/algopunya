import sys

sys.stdin = open('input.txt', 'r')


def f(x, y):
    global count
    global take_time
    global N, M

    if x > N or y > M:
        return
    else:
        q = [[0, 0, 0]]  # 문 x,y,움직인 횟수
        while q:
            x_, y_, moving = q.pop(0)

            for dx, dy in [(1, 0), (0, 1)]:
                nx = x_ + dx
                ny = y_ + dy

                if 0 <= nx <= x and 0 <= ny <= y:  # 코니 좌표 이전까지만 해당방향으로 움직이도록함
                    if (nx, ny) == (x, y):
                        count += 1
                        take_time = moving + 1
                    else:
                        q.append([nx, ny, moving + 1])


N, M = map(int, input().split())  # 모눈종이 가로,세로
x, y = map(int, input().split())  # 코니 가로, 세로

count = 0
take_time = 0

f(x, y)
if not count:
    print('fail')
else:
    print(count)
    print(take_time)
