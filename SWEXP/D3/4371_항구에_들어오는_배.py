

# 시간초과
"""T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 즐거운 날의 수

    fun_days = [int(input()) for _ in range(N)]

    count = 0

    while fun_days != [1]:
        gap = fun_days[1] - 1
        fun_days = list(filter(lambda x: x == 1 or (x - 1) % gap != 0, fun_days))
        count += 1

    print(f"#{tc} {count}")"""
