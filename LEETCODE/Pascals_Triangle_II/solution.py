class Solution:
    memoize = {}

    def getValue(self, i, j):
        if j == 0 or j == i:
            return 1
        elif (i, j) in Solution.memoize:
            return Solution.memoize[(i, j)]
        else:
            value = self.getValue(i - 1, j - 1) + self.getValue(i - 1, j)
            Solution.memoize[(i, j)] = value
            return value

    def getRow(self, rowIndex: int) -> List[int]:
        return [self.getValue(rowIndex, j) for j in range(rowIndex + 1)]
