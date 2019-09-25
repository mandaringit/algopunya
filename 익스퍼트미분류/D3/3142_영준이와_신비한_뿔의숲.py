T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())

    twin_horn = n - m
    unicorn = m - twin_horn

    print(f"#{tc}", unicorn, twin_horn)
