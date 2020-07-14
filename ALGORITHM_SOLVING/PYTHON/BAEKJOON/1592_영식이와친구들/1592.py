import sys

sys.stdin = open('input.txt', 'r')

N, M, L = map(int, input().split())  # N명의 사람, M번 받으면 종료, L번째 사람에게..

seats = [0] * N
idx = 0
cnt = 0

while True:
    seats[idx] += 1

    if seats[idx] == M:
        break
    else:
        if seats[idx] % 2 == 1:
            next_idx = (idx + L) % N
        else:
            next_idx = abs(idx - L) % N
