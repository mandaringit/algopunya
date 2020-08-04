import sys

sys.stdin = open('input.txt', 'r')


# 시간초과

def DFS(i, total):
    global numbers
    global N
    global count

    if i == N - 2:
        if total == numbers[N - 1]:
            count += 1
            return
        else:
            return

    elif total > 20 or total < 0:
        return
    else:
        DFS(i + 1, total + numbers[i + 1])
        DFS(i + 1, total - numbers[i + 1])


N = int(input())

numbers = list(map(int, input().split()))
count = 0
DFS(0, numbers[0])
print(count)
