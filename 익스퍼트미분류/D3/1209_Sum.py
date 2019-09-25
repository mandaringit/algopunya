for tc in range(1, 11):
    t = input()
    N = 100
    arr = [list(map(int, input().split())) for i in range(N)]

    maxValue = 0

    # 가로합
    for row in arr:
        if sum(row) > maxValue:
            maxValue = sum(row)

    # 세로합
    for i in range(N):
        total = 0
        for j in range(N):
            total += arr[j][i]

        if total > maxValue:
            maxValue = total

    # 대각선 아래 합
    d1 = 0
    for i in range(N):
        d1 += arr[i][i]

    if d1 > maxValue:
        maxValue = d1

    # 대각선 위 합
    d2 = 0
    for i in range(N):
        d2 += arr[i][N-1-i]

    if d2 > maxValue:
        maxValue = d2

    print(f"#{tc} {maxValue}")
