T = int(input())

for tc in range(1, T + 1):
    sD, sH, sM = 11, 11, 11
    D, H, M = map(int, input().split())

    M_diff = 0

    # 분이 기준 분보다 작을때 시간을 하나 가져온다
    if M < sM:
        H -= 1
        M += 60

    M_diff = M - sM

    # 앞에서 가져간 분 때문에 혹시 시가 음수가 나오면 날에서 가져온다
    if H < 0:
        D -= 1
        H += 24

    H_diff = H - sH

    if H < sH:
        D -= 1
        H += 24

        H_diff = H - sH

    D_diff = D - sD

    result = -1

    if D_diff >= 0:
        result = D_diff * 24 * 60 + H_diff * 60 + M_diff

    print(f"#{tc} {result}")