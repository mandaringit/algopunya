import sys

sys.stdin = open('sample_input.txt', 'r')


# 백트래킹

# 현재 row, 지금까지 선택된 공장(column)들, 지금까지 든 비용
def DFS(i, selected_factories, total_cost):
    global costs
    global N
    global minV
    global factories

    # 맨 마지막 줄에 도달하면 종료
    if i == N - 1:
        if total_cost < minV:
            minV = total_cost
    else:
        for j in factories - selected_factories:  # 이미 선택한 공장(column)을 제외한 나머지 공장중 하나를 선택한다.
            next_row = i + 1  # 같은 제품은 선택 할 수 없으므로 무조건 다음 row로 넘어간다
            next_cost = total_cost + costs[next_row][j]

            if next_cost < minV:  # 다음 가격이 현재 최소보다 작을 경우에만 더 탐색을 진행하도록 한다
                next_selected_factories = selected_factories | {j}
                DFS(next_row, next_selected_factories, next_cost)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    costs = [list(map(int, input().split())) for _ in range(N)]

    minV = 99 * N

    factories = set(i for i in range(N))
    for j in range(N):
        DFS(0, {j}, costs[0][j])  # 첫번째 줄 모든 column이 출발점이 될 수 있음

    print("#{} {}".format(tc, minV))
