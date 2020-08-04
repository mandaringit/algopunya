T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    S1 = (N * (N + 1)) // 2

    S2 = N * N

    S3 = N * (N + 1)

    print(f"#{tc}", S1, S2, S3)
