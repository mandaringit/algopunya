T = int(input())

for tc in range(1, T+1):
    N = int(input())

    results = [f"1/{N}" for _ in range(N)]

    print(f"#{tc} {' '.join(results)}")
