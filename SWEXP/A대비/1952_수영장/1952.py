import sys

sys.stdin = open('sample_input.txt', 'r')


def get_next_month(month):
    global plan
    for m in range(month + 1, 12):
        if plan[m]:
            return m
    return 12


def using(month, total, p):
    global min_price
    global prices

    if month >= 12:
        if total < min_price:
            min_price = total
    else:
        if total < min_price:
            if p == 0:
                total += plan[month] * prices[0]
                next_month = get_next_month(month)
            elif p == 1:
                total += prices[1]
                next_month = get_next_month(month)
            elif p == 2:
                total += prices[2]
                if month + 3 >= 12:
                    next_month = 12
                else:
                    next_month = get_next_month(month + 2)

            for k in range(3):
                using(next_month, total, k)


import timeit

start = timeit.default_timer()

T = int(input())

for tc in range(1, T + 1):
    prices = list(map(int, input().split()))

    plan = list(map(int, input().split()))

    min_price = prices[-1]  # 1년권

    start = get_next_month(-1)

    for i in range(3):
        using(start, 0, i)

    print("#{} {}".format(tc, min_price))

end = timeit.default_timer()

print((end - start) * 1000)
