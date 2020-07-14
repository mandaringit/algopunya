import sys

sys.stdin = open('sample_input.txt', 'r')

import timeit

start = timeit.default_timer()

T = int(input())

for tc in range(1, T + 1):
    day, month_1, month_3, year = map(int, input().split())
    plan = [0] + list(map(int, input().split()))

    min_price = year  # 1년권
    dp = [0] * 13  # 1 ~ 12월

    for month in range(1, 13):  # 1월부터 12월까지,
        if month <= 2:  # 1월에서 2월까지는
            # 해당 월의 dp값 = 이전 월의 dp값 + 최소(일권사용 , 1달권사용)
            dp[month] = dp[month - 1] + min(plan[month] * day, month_1)
        else:  # 3월부터는, 최소(이전 월의 dp값 + 최소(일권사용 , 1달권사용) , 3달전의 dp값 + 3달권)
            dp[month] = min(dp[month - 1] + min(plan[month] * day, month_1), dp[month - 3] + month_3)

    if dp[-1] < min_price:
        min_price = dp[-1]

    print("#{} {}".format(tc, min_price))

end = timeit.default_timer()

print((end - start) * 1000)
