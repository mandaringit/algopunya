import sys

sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())

peoples = [num for num in range(1,N+1)]
front = K - 1
count = 0
josepers = []
while count != N:

    josepers.append(peoples[front])
    peoples[front] = 0

    plus = 0
    while plus != K:
        front += 1
        if front == N:
            front = front % N

        if peoples[front] != 0:
            plus += 1

        if peoples == [0]*N:
            break

    count += 1
print(f"<{', '.join(map(str,josepers))}>")


