import sys

sys.stdin = open('input.txt', 'r')

price = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]

coin_count = 0
for coin in coins:
    q, r = divmod(price, coin)
    if q > 0:
        coin_count += q
        price = r

print(coin_count)
