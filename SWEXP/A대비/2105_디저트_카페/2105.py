import sys

sys.stdin = open('sample_input.txt', 'r')


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    cafes = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    maxV = 0
    maxPath = 0

    for i in range(N):
        for j in range(N):


    print(maxPath)
