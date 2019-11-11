import sys

sys.stdin = open('s_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    lines = [0] * 5000

    for _ in range(N):
        A, B = map(int, input().split())

        for i in range(A - 1, B):
            lines[i] += 1

    P = int(input())

    result = []

    for _ in range(P):
        j = int(input())

        result.append(lines[j - 1])

    print(f"#{tc} {' '.join(map(str,result))}")
