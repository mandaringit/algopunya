class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorting = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != sorting[i]:
                count += 1
        return count
