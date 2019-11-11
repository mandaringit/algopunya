import sys

sys.stdin = open('input.txt', 'r')

def decomposition_sum(constructor):
    for char in str(constructor):
        constructor += int(char)

    return constructor


N = int(input())

i = 1

while i < N:
    constructor = decomposition_sum(i)
    if constructor == N:
        break
    i += 1

print(0) if i == N else print(i)
