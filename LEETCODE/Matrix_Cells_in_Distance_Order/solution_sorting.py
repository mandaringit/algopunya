class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:

        points = []
        for i in range(R):
            for j in range(C):
                points.append([i, j])

        points.sort(key=lambda x: abs(r0 - x[0]) + abs(c0 - x[1]))

        return points
