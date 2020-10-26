

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:

        visited = [[0]*C for _ in range(R)]
        q = [[r0, c0]]
        visited[r0][c0] = 1
        rear = 0

        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while len(q) > rear:
            r, c = q[rear]
            rear += 1

            for dx, dy in d:
                ni = r + dx
                nj = c + dy

                if 0 <= ni < R and 0 <= nj < C:
                    if not visited[ni][nj]:
                        visited[ni][nj] = 1
                        q.append([ni, nj])

        return q
