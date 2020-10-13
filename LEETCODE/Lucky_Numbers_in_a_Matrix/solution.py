class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:

        rows = set(min(row) for row in matrix)
        cols = set(max(col) for col in zip(*matrix))

        return list(rows & cols)
