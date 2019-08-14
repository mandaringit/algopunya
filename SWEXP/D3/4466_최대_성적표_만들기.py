T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    scores = list(map(int, input().split()))

    score_sum = 0

    for _ in range(K):
        max_score = max(scores)
        score_sum += max_score
        scores.remove(max_score)

    print(f"#{tc} {score_sum}")
