import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

N = int(input())

board = [[0] * N for _ in range(N)]

snake = deque()
snake.append([0, 0])
K = int(input())
for _ in range(K):
    i, j = map(int, input().split())
    board[i - 1][j - 1] = 1

turning = {}
L = int(input())
for _ in range(L):
    X, D = input().split()
    turning[int(X)] = D

T = 0
# 우, 하, 상, 좌
directions = {
    (0, 1): {
        'L': (-1, 0),
        'D': (1, 0)
    },
    (1, 0): {
        'L': (0, 1),
        'D': (0, -1)
    },
    (-1, 0): {
        'L': (0, -1),
        'D': (0, 1)
    },
    (0, -1): {
        'L': (1, 0),
        'D': (-1, 0)
    }
}

current_direction = (0, 1)
while True:
    # 1. 시간증가
    T += 1
    # 2. 다음 위치를 구한다.
    snake_head = snake[-1]
    dx, dy = current_direction
    ni, nj = snake_head[0] + dx, snake_head[1] + dy

    # 3. 다음 위치가 자신의 몸 안에 없고 && 인덱스 안인가? => 진행
    if 0 <= ni < N and 0 <= nj < N:
        if [ni, nj] not in snake:
            # 사과가 있으면 => 기존꺼 두고 뒤에 헤드 추가
            if board[ni][nj] == 1:
                snake.append([ni, nj])
                board[ni][nj] = 0  # 사과 지우기
            # 사과가 없으면 => 기존 꼬리 삭제, 헤드 추가
            else:
                snake.popleft()
                snake.append([ni, nj])
        else:
            break
    else:
        break

    # 4. 방향 전환
    if T in turning:
        current_direction = directions[current_direction][turning[T]]

print(T)
