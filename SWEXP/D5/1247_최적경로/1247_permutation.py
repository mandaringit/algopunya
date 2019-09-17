import sys

sys.stdin = open('input.txt', 'r')


def permutation(n, k, total_distance):
    global customers
    global home
    global company
    global N
    global minV

    if n == k:
        roads = customers + [home]

        distance = abs(roads[-2][0] - roads[-1][0]) + abs(roads[-2][1] - roads[-1][1])

        if total_distance + distance < minV:
            minV = total_distance + distance

    elif total_distance > minV:
        return
    else:
        for i in range(n, k):
            customers[n], customers[i] = customers[i], customers[n]  # 이 부분에서 n번째 자리까진 확정이다 ?

            roads = [company] + customers[:n + 1]
            distance = abs(roads[-2][0] - roads[-1][0]) + abs(roads[-2][1] - roads[-1][1])
            permutation(n + 1, k, total_distance + distance)
            customers[n], customers[i] = customers[i], customers[n]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    info = list(map(int, input().split()))
    minV = 200 * (N + 1)
    coords = [(info[2 * i], info[2 * i + 1]) for i in range(N + 2)]
    company = coords[0]
    home = coords[1]
    customers = coords[2:]

    permutation(0, N, 0)
    print("#{} {}".format(tc, minV))
