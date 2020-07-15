import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    weights = list(map(int, input().split()))
    truck_weights = list(map(int, input().split()))

    truck_weights.sort()
    weights.sort(reverse=True)
    used = []
    for available in truck_weights:  # 작은 놈들한테 큰거 먼저 준다
        for weight in weights:
            if weight <= available:
                used.append(weight)
                weights.remove(weight)
                break
    print("#{} {}".format(tc, sum(used)))
