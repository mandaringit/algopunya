import sys

sys.stdin = open('input.txt', 'r')


def BFS(start, graph):
    global visited

    visited.add(start)
    red = {start}
    blue = set()
    q = [(start, 'R')]

    while q:
        node, color = q.pop(0)

        for nearby in graph[node]:
            # 방문 안한곳은 색을 자신과 반대로 칠해준다
            if nearby not in visited:
                if color == 'R':
                    visited.add(nearby)
                    blue.add(nearby)
                    q.append((nearby, 'B'))
                elif color == 'B':
                    visited.add(nearby)
                    red.add(nearby)
                    q.append((nearby, 'R'))
            else:  # 만약 방문 했었고 색이 있다면
                if color == 'R' and nearby in red:
                    return 'NO'
                elif color == 'B' and nearby in blue:
                    return 'NO'

    return 'YES'


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = {i: set() for i in range(1, V + 1)}

    for _ in range(E):
        n1, n2 = map(int, input().split())

        graph[n1].add(n2)
        graph[n2].add(n1)

    visited = set()
    nodes = set(list(graph.keys()))

    last_result = 'YES'
    for i in nodes:  # 연결 그래프가 아닐 수도 있습니다 그러므로 모두 들어가봐야합니다
        if i not in visited:
            result = BFS(i, graph)
            if result == 'NO':
                last_result = 'NO'
                break
    print(last_result)
