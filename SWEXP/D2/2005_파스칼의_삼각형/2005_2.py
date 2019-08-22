import sys

sys.stdin = open('input.txt', 'r')


def Pascal(N):
    if N == 1:
        return [1]
    elif N == 2:
        return [1, 1]
    else:
        prev = Pascal(N - 1)

        next_center = []

        for i in range(0, len(prev) - 1):
            next_center.append(prev[i] + prev[i + 1])

        return [1, *next_center, 1]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    print(f'#{tc}')
    for i in range(1, N + 1):
        print(" ".join(map(str, Pascal(i))))

# 위에처럼 재귀로 하는 방법도 있고

# 2차원 리스트로 만들어서 규칙에 맞게 채우는 방법도 있다.
