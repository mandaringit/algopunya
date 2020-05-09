"""
# 일부 시간초과

Q4

# 입력

# 출력

# 접근
    - BFS ? DFS ?
    1. 0,0 출발
    2. 4방향 확인 => d = [(0,1),(1,0),(-1,0),(0,-1)]
        2-1 . 벽 또는 범위 밖 확인 + 이미 간곳이었는지 확인 후 진입
        2-2 . 전과 같은 방향이었으면 + 100
        2-3 . 전과 다른 방향이었으면 + 500 (빠꾸는 없으니께)

    3. N-1, N-1 에 도착하면 가격 계산 후 비교

"""

from collections import deque


def solution(board):
    # 0 - 비어있음
    # 1 - 벽
    N = len(board)

    visited = [[0] * N for _ in range(N)]

    minValue = N * N * 500

    def explore(i, j, price, prev_d):
        nonlocal minValue

        if (i, j) == (N - 1, N - 1):
            if price < minValue:
                minValue = price
            visited[i][j] = 0
            return
        elif price >= minValue:
            return
        else:
            visited[i][j] = 1

            d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in d:
                ni = i + dx
                nj = j + dy

                if 0 <= ni < N and 0 <= nj < N:
                    if board[ni][nj] == 0 and visited[ni][nj] == 0:

                        if prev_d == (dx, dy) or not prev_d:
                            # 직선도로라면
                            explore(ni, nj, price + 100, (dx, dy))
                        else:
                            # 코너라면
                            explore(ni, nj, price + 600, (dx, dy))

        visited[i][j] = 0

    explore(0, 0, 0, None)

    return minValue


print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0]]))
