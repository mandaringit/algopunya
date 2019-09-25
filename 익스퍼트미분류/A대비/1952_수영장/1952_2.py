import sys

sys.stdin = open('sample_input.txt', 'r')

import timeit

start = timeit.default_timer()

T = int(input())
for t in range(1, T + 1):
    d, m1, m3, y = list(map(int, input().split()))
    month = [0] + list(map(int, input().split()))

    dp = [0] * 13
    for i in range(1, 13):
        if i < 3:
            dp[i] = dp[i - 1] + min(d * month[i], m1)
        else:
            dp[i] = min((dp[i - 1] + min(d * month[i], m1)), dp[i - 3] + m3)
    result = dp[-1]
    if y < dp[-1]:
        result = y
    print("#{} {}".format(t,result))

end = timeit.default_timer()

print(end - start)
