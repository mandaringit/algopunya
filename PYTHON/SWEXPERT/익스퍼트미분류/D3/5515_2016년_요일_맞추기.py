T = int(input())

d31 = [1, 3, 5, 7, 8, 10, 12]
d30 = [4, 6, 9, 11]
Week = [4, 5, 6, 0, 1, 2, 3]

for t in range(1, T+1):
    m, d = map(int, input().split())
    std_m = std_d = 1

    total_day = (d-1)

    for i in range(1, m):
        if i in d31:
            total_day += 31
        elif i in d30:
            total_day += 30
        else:
            total_day += 29

    print(f"#{t} {Week[total_day%7]}")
