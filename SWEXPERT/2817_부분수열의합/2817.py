import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    numbers = list(sorted(list(map(int, input().split()))))
    count = 0
    for i in range(1, 1 << N):
        summation = 0
        for j in range(N):
            if i & (1 << j):
                summation += numbers[j]
                if summation > K:
                    break

        if summation == K:
            count += 1
    print(f"#{tc} {count}")
