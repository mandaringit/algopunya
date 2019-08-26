import sys

sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())

peoples = [num for num in range(1, N + 1)]
josepers = []

front = 0
while peoples:
    front = (front + K - 1) % len(peoples)
    josepers.append(peoples.pop(front))

print(f"<{', '.join(map(str, josepers))}>")
