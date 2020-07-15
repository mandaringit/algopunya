import sys

sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())

temperatures = list(map(int, input().split()))

maxV = -100 * K
for i in range(N - K + 1):
    temp_part = temperatures[i:i + K]
    SUM = sum(temp_part)
    if SUM > maxV:
        maxV = SUM
print(maxV)
