class Solution:
    def minDeletionSize(self, A: List[str]) -> int:

        N = len(A[0])

        columns = list(zip(*A))
        count = 0
        for i in range(len(columns)):
            if list(columns[i]) != list(sorted(columns[i])):
                count += 1

        return count
