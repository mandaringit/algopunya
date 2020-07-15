T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))

    max_price = prices[-1]

    total = 0

    for i in range(N - 2, -1, -1):
        if prices[i] <= max_price:
            total += max_price - prices[i]
        else:
            max_price = prices[i]

    print(f"#{tc}", total)
