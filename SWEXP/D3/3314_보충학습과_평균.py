T = int(input())

for tc in range(1, T + 1):
    scores = map(int, input().split())

    study_more = map(lambda x: 40 if x < 40 else x, scores)

    avg = sum(study_more) // 5

    print(f"#{tc} {avg}")
