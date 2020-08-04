# 파리채가 X자 모양이라면 (크기는 K)

# # 부분 배열의 왼쪽 위 모서리 좌표가 i,j 일때,
#
# s = 0
#
# for m in range(K):
#     s += fly[i + m][j + m]
#     s += fly[i + m][j + k - 1 - m]
# # K가 홀수인 경우 가운데 원소가 두번 더해지므로
#
# if K % 2 == 1:
#     s -= fly[i + K // 2][j + K // 2]

# 정답

import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0

    for i in range(0, N - M + 1):
        for j in range(0, N - M + 1):

            kill = 0

            # 대각선
            for k in range(M):
                kill += board[i + k][j + k]
                kill += board[i + k][j + M - k - 1]

            # 파리채 길이가 홀수 일때

            if M % 2 == 1:
                kill -= board[i + M // 2][j + M // 2]

            if kill > max_kill:
                max_kill = kill

    print(f"#{tc} {max_kill}")
