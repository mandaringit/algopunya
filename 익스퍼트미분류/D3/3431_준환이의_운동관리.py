T = int(input())

for tc in range(1, T + 1):
    L, U, X = map(int, input().split())

    result = 0
    if L > X:
        result += (L-X)

    if U < X:
        result = -1

    print(f"#{tc} {result}")
