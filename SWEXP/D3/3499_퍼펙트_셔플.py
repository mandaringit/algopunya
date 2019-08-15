T = int(input())

results = []

for tc in range(1, T + 1):
    N = int(input())
    cards = input().split()

    center = N // 2 if N % 2 else N // 2 - 1

    left = cards[:center + 1]
    right = cards[center + 1:]

    for i in range(len(right) - 1, -1, -1):  # 뒤부터 넣는 이유는 인덱스를 망치지 않기 위해
        left.insert(i + 1, right[i])

    results.append(f"#{tc} {' '.join(left)}")

print('\n'.join(results))
