import sys

sys.stdin = open('input.txt', 'r')

L = int(input())
N = int(input())
cake = [0] + [0] * L

max_expect = 0
max_watcher = 0
real_max = 0
real_watcher = 0
for watcher_num in range(1, N + 1):
    P, K = map(int, input().split())
    length = K - P + 1
    if length > max_expect:
        max_expect = length
        max_watcher = watcher_num

    my_cake = 0
    for i in range(P, K + 1):
        if cake[i] == 0:
            cake[i] = watcher_num
            my_cake += 1

    if my_cake > real_max:
        real_max = my_cake
        real_watcher = watcher_num

print(max_watcher)
print(real_watcher)



