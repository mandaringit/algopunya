import sys

sys.stdin = open('sample_input.txt', 'r')

# 70분 ..

def get_max_honey_price(arr, C):
    max_price = 0
    for i in range(1, 1 << len(arr)):
        subset = []
        for j in range(len(arr)):
            if i & (1 << j):
                subset.append(arr[j])
        if sum(subset) <= C:
            new_subset = map(lambda x: x ** 2, subset)
            value = sum(new_subset)
            if value > max_price:
                max_price = value

    return max_price


T = int(input())

for tc in range(1, T + 1):
    N, M, C = map(int, input().split())

    house = [list(map(int, input().split())) for _ in range(N)]

    get_honey = {i: 0 for i in range(N)}

    for i in range(0, N):

        for j in range(0, N - M + 1):
            honeys = house[i][j:j + M]
            honeys.sort(reverse=True)

            total_price = get_max_honey_price(honeys, C)

            if get_honey[i] < total_price:
                get_honey[i] = total_price

    honey_prices = sorted(get_honey.values(), reverse=True)

    sold_price = honey_prices[0] + honey_prices[1]

    print("#{} {}".format(tc, sold_price))
