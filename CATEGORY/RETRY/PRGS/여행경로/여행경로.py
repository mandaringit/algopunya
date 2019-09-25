tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]


# tc1 통과못함 (898.80ms,69. 6MB)

def solution(tickets):
    graph = {}

    for i in range(len(tickets)):
        node1, node2 = tickets[i]
        if node1 in graph:
            graph[node1].add(i)
        else:
            graph[node1] = {i}

    paths = []
    possible_tickets = {i for i in range(len(tickets))}
    q = [('ICN', ['ICN'], set())]

    while q:
        airport, path, used = q.pop(0)

        if used == possible_tickets:
            paths.append(path)
        else:
            if airport in graph:  # tc1,2 런타임 에러 해결
                for i in graph[airport] - used:  # 가능한 티켓들만 사용
                    next_airport = tickets[i][1]
                    next_path = path + [next_airport]
                    next_used = used | {i}

                    if next_used == possible_tickets:
                        paths.append(next_path)
                    else:
                        q.append((next_airport, next_path, next_used))
    result = paths[0]

    # 정렬
    for i in range(len(tickets) + 1):
        paths.sort(key=lambda x: x[i])
        first = paths[0]

        if result != first:
            result = first
            break

    return result


print(solution(tickets))
