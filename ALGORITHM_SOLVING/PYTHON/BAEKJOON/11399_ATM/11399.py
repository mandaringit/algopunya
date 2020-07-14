import sys

sys.stdin = open('input.txt', 'r')

N = int(input())

waiting = list(map(int, input().split()))

waiting.sort()  # 작은 순서대로 정렬하고,

total_waiting = []

for i in range(N):
    total_waiting.append(sum(waiting[:i + 1]))  # 기다리는 사람은 이전까지 뽑는데 소요되는 시간 + 자기자신의 소요시간

print(sum(total_waiting))
