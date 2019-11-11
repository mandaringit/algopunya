import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):

    N, L = map(int, input().split())

    gradients = []

    for _ in range(N):
        score, cal = map(int, input().split())
        gradients.append((score, cal))

    max_score = 0
    max_subset = []

    for i in range(1, 1 << N):
        # subset = []  # 해당 부분집합이 뭔지 보고싶다면 이하 주석을 해제해보자
        total_score = 0
        total_cal = 0
        is_over_cal = False
        for j in range(N):
            if i & (1 << j):
                # subset.append(gradients[j])
                total_score += gradients[j][0]
                total_cal += gradients[j][1]

                if total_cal > L:
                    is_over_cal = True
                    break

        if not is_over_cal and max_score < total_score:
            # max_subset = subset
            max_score = total_score

    print(f"#{tc} {max_score}")
