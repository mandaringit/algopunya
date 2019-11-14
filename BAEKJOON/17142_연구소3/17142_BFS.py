import sys

sys.stdin = open('input.txt', 'r')


# 바이러스 유출. --> 활성, 비활성
# 초기 바이러스는 모두 비활성
# 활성 상태인 바이러스는 상하 좌우로 인접한 모든 빈칸 동시 복제. 1초 걸림
# 승원이는 연구소 바이러스 "M" 개를 활성 상태로 변경하려 한다.
# 활성 meet 비활성 => 활성으로 변함


def BFS(Q):
    global lab
    visited = [[-1]*N for _ in range(N)]
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i, j in Q:
        visited[i][j] = 0

    while Q:
        i, j = Q.pop(0)

        for dx, dy in d:
            ni = i+dx
            nj = j+dy

            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == -1:
                    if lab[ni][nj] != 1:
                        visited[ni][nj] = visited[i][j]+1
                        Q.append([ni, nj])

    max_time = 0
    for i in range(N):
        for j in range(N):
            # 중요한 부분. 방문체크는 했지만 여기가 바이러스 자리라면 세지 않는다.
            # 만약 최대값이 바이러스가 아닌 자리라면 그땐 체크 할것.
            if visited[i][j] > max_time and lab[i][j] != 2:
                max_time = visited[i][j]

            # 빈자리가 있는데 하나라도 방문을 안했으면 아웃.
            if lab[i][j] == 0 and visited[i][j] == -1:
                return -1
    return max_time


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

# 1.바이러스 위치 수집
virus_location = []
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus_location.append([i, j])

# 2. 바이러스중 M개 뽑는 경우 구하기
vc = len(virus_location)
result = 100000000
for i in range(1, 1 << vc):
    Q = []
    for j in range(vc):
        if i & (1 << j):
            Q.append(virus_location[j])

    if len(Q) == M:
        # 3. 해당 경우의 BFS 시작.
        time = BFS(Q)

        if -1 < time < result:
            result = time
if result == 100000000:
    result = -1
print(result)
