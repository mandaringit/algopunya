import sys

sys.stdin = open('input.txt', 'r')

N, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(board)

maxV = 0

for i in range(N):
    for j in range(N):
        # i,j는 기준점이 된다.
        print(f"{i},{j} 일때..")
        # 상하좌우
        S1 = board[i][j]
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for di, dj in d:
            for r in range(1, R + 1):
                ni = i + r * di
                nj = j + r * dj

                # 인덱스는 구했고, 이게 범위 안인지 보자
                if 0 <= ni < N and 0 <= nj < N:
                    S1 += board[ni][nj]

        # 대각선
        S2 = board[i][j]
        d2 = [(-1, -1), (1, 1), (1, -1), (-1, 1)]
        for di, dj in d2:
            for r in range(1, R + 1):
                ni = i + r * di
                nj = j + r * dj

                if 0 <= ni < N and 0 <= nj < N:
                    S2 += board[ni][nj]

        print(f'상하좌우 : {S1}, 대각선 : {S2}')

        if max(S1, S2) > maxV:
            maxV = max(S1, S2)

print(f"최대값: {maxV}")



import sys

sys.stdin = open('input.txt', 'r')

N, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(board)

maxV = 0

for i in range(N):
    for j in range(N):
        # i,j는 기준점이 된다.
        print(f"{i},{j} 일때..")
        # 상하좌우
        S1 = board[i][j]
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for di, dj in d:
            for r in range(1, R + 1):
                ni = i + r * di
                nj = j + r * dj

                # 인덱스는 구했고, 이게 범위 안인지 보자
                if 0 <= ni < N and 0 <= nj < N:
                    S1 += board[ni][nj]

        # 대각선
        S2 = board[i][j]
        d2 = [(-1, -1), (1, 1), (1, -1), (-1, 1)]
        for di, dj in d2:
            for r in range(1, R + 1):
                ni = i + r * di
                nj = j + r * dj

                if 0 <= ni < N and 0 <= nj < N:
                    S2 += board[ni][nj]

        print(f'상하좌우 : {S1}, 대각선 : {S2}')

        if max(S1, S2) > maxV:
            maxV = max(S1, S2)

print(f"최대값: {maxV}")
