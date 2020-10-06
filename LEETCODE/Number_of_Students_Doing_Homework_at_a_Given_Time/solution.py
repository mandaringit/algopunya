class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:

        N = len(startTime)
        count = 0

        for i in range(N):
            if startTime[i] <= queryTime <= endTime[i]:
                count += 1

        return count
