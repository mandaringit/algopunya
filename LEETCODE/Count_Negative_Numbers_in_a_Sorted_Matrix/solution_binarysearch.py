from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])

        def binary_search(row):
            l, r = 0, N - 1

            while l < r:
                mid = (l + r) // 2

                if row[mid] < 0:
                    r = mid
                else:
                    l = mid + 1

            if row[l] >= 0:
                return 0

            return N - l

        count = 0
        for row in grid:
            count += binary_search(row)

        return count


sol = Solution()
sol.countNegatives([[4, 3, 2, -1], [3, 2, 1, -1],
                    [1, 1, -1, -2], [-1, -1, -2, -3]])
sol.countNegatives([[3, 2], [1, 0]])
