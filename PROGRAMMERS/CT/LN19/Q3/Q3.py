import sys

sys.stdin = open('input.txt', 'r')

N = int(input())

toilet = [0] * 151

for _ in range(N):
    go_time, back_time = map(int, input().split())

    for i in range(go_time, back_time):
        toilet[i] += 1

print(max(toilet))
