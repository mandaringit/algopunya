import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    scores = list(map(int, input().split()))

    scores_set = list(set(scores))
    possible_scores = set()

    for i in range(1 << len(scores_set)):
        subset = []
        for j in range(len(scores_set)):
            if i & (1 << j):
                subset.append(scores_set[j])

        possible_scores.add(sum(subset))

    print("#{} {}".format(tc, len(possible_scores)))
