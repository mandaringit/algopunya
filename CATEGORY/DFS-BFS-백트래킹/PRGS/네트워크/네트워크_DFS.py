n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]


def solution(n, computers):
    visited = [0] * n
    count = 0
    for i in range(n):
        if visited[i] == 0:
            count += 1
            stack = [i]
            while stack:

                x = stack.pop()  # 시작 컴퓨터

                for nx in range(n):
                    if nx != x and visited[nx] == 0:
                        if computers[x][nx] == 1:  # 연결 시
                            visited[nx] = 1
                            stack.append(nx)

    return count


print(solution(n, computers))
