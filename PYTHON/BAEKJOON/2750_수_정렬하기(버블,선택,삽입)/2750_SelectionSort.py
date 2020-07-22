N = int(input())
arr = [int(input()) for _ in range(N)]

for i in range(N - 1, 0, -1):  # N-1번째 인덱스부터 ~ 1 까지
    biggest = [i, arr[i]]  # 초기에 가장 큰 수 및 인덱스
    for j in range(0, i):  # 0 ~ i 번째 인덱스 수까지 돌면서
        # 최댓값을 찾는다.
        if biggest[1] < arr[j]:
            biggest = [j, arr[j]]

    arr[i], arr[biggest[0]] = arr[biggest[0]], arr[i]

for v in arr:
    print(v)
