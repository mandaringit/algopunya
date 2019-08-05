# ?? 뭐에서 틀린건지 모르겟당

T = int(input())

for t in range(1, T+1):
    N = int(input())
    lines = {}
    for _ in range(1, N+1):
        # i번째 버스노선은 번호가 A_i ~ B_i 인 모든 정류장을 다니는 노선이다.
        A_i, B_i = map(int, input().split())

        for line in range(A_i, B_i + 1):
            if line in lines:
                lines[line] += 1
            else:
                lines[line] = 1

    result = f"#{t} "

    P = int(input())  # P개의 정류장을 조사하자
    for _ in range(1, P+1):
        C_j = int(input())  # C_j번째 정류장은 노선 몇개가 다니나?
        result += f"{lines[C_j]} "

    print(result)
