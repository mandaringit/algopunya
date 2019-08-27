import sys

sys.stdin = open('input.txt', 'r')

# 행, 열
N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

# 왼쪽위가 W 일때랑 B 일때 두개 생성
line1 = "WBWBWBWB"
line2 = "BWBWBWBW"
W_board = []
B_board = []

for i in range(8):
    # 홀수일때
    if i % 2:
        W_board.append(list(line2))
        B_board.append(list(line1))
    else:
        W_board.append(list(line1))
        B_board.append(list(line2))

min_fixed_count = 63 # 왼쪽위 빼고 모두 고치는 경우

for i in range(0, N - 7):
    for j in range(0, M - 7):
        # left_top = i,j

        W_fix_count = 0
        B_fix_count = 0

        for k in range(0, 8):
            for m in range(0, 8):
                # 왼쪽 위가 W인 경우와 B인 경우 두개를 "모두" 검사해야한다.
                if board[i + k][j + m] != W_board[k][m]:
                    W_fix_count += 1

                if board[i + k][j + m] != B_board[k][m]:
                    B_fix_count += 1

        # 둘중 최소인걸로 선택
        minimum_count = min(W_fix_count, B_fix_count)

        if minimum_count < min_fixed_count:
            min_fixed_count = minimum_count

print(min_fixed_count)
