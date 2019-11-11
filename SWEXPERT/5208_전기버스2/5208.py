import sys

sys.stdin = open('sample_input.txt', 'r')


def f(i, d, cnt):
    global minV
    global stations
    global N

    if i == N - 1:
        if cnt < minV:
            minV = cnt
    elif cnt > minV:
        return
    else:
        for dx in range(1, d + 1):
            ni = i + dx

            if ni == N - 1:  # 목적지까지 바로 갈 수 있을때
                if cnt < minV:
                    minV = cnt

            elif ni < N - 1:
                f(ni, stations[ni], cnt + 1)


T = int(input())

for tc in range(1, T + 1):
    info = list(map(int, input().split()))

    N = info[0]
    stations = info[1:]
    minV = len(stations)
    f(0, stations[0], 0)
    print("#{} {}".format(tc, minV))
