import sys

sys.stdin = open('input.txt', 'r')


def BFS(i, j):
    global visited
    # 우 , 좌, 하, 상
    d1 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    d2 = [[(-1, 1), (1, 1)], [(-1, -1), (1, -1)], [(1, -1), (1, 1)], [(-1, 1), (-1, -1)]]

    visited[i][j] = 1
    q = [(i, j)]

    while q:
        i_, j_ = q.pop(0)
        for d in range(4):
            # 한걸음
            ni_1 = i_ + d1[d][0]
            nj_1 = j_ + d1[d][1]

            if 0 <= ni_1 < 10 and 0 <= nj_1 < 9 and (ni_1, nj_1) != (R2, C2):
                for nd in range(2):
                    # 두걸음
                    ni_2 = ni_1 + d2[d][nd][0]
                    nj_2 = nj_1 + d2[d][nd][1]

                    # 세걸음
                    if 0 <= ni_2 < 10 and 0 <= nj_2 < 9 and (ni_2, nj_2) != (R2, C2):
                        ni_3 = ni_2 + d2[d][nd][0]
                        nj_3 = nj_2 + d2[d][nd][1]

                        if 0 <= ni_3 < 10 and 0 <= nj_3 < 9:
                            if (ni_3, nj_3) == (R2, C2):
                                return visited[i_][j_]
                            else:
                                if visited[ni_3][nj_3] == 0:
                                    visited[ni_3][nj_3] = visited[i_][j_] + 1
                                    q.append((ni_3, nj_3))
    return -1


R1, C1 = map(int, input().split())
R2, C2 = list(map(int, input().split()))
visited = [[0] * 9 for _ in range(10)]
print(BFS(R1, C1))
