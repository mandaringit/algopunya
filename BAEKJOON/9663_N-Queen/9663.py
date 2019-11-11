import sys

sys.stdin = open('input.txt', 'r')


def DFS(i, j):
    global N
    global count
    global board

    if i == N - 1:
        count += 1
    else:
        backups = []  # 이따가 복원 할 것들

        # 1. 대각선 처리
        d = [(1, -1), (1, 1)]  # 왼쪽 대각선, 오른쪽 대각선
        for dx, dy in d:
            ni = i + dx
            nj = j + dy

            while 0 <= ni < N and 0 <= nj < N:
                if board[ni][nj] == 0:
                    board[ni][nj] = 1
                    backups.append([ni, nj])
                ni += dx
                nj += dy

        # 2. 방문한 열 체크 표시
        for row in range(i, N):
            if board[row][j] == 0:
                board[row][j] = 1
                backups.append([row, j])

        # 3. 다음줄에 가보고 가능한 곳이면 방문
        for j_ in range(0, N):
            if board[i + 1][j_] == 0:
                DFS(i + 1, j_)

        # 4. 실패하고 돌아온 친구를 위해 보드 원상복구
        for bi, bj in backups:
            board[bi][bj] = 0


N = int(input())

board = [[0] * N for _ in range(N)]
count = 0

for j in range(N):
    DFS(0, j)
print(count)
