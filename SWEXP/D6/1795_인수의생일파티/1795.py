import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M, X = map(int, input().split())  # 노드수, 간선수, 도착지


