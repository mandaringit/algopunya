waves = {
    1: 1,
    2: 1,
    3: 1
}

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    for i in range(1, N + 1):
        if i not in waves:
            waves[i] = waves[i - 2] + waves[i - 3]

    print(f"#{tc} {waves[N]}")
