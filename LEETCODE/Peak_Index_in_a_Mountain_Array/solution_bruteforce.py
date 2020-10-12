class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        peak = [0, arr[0]]
        for i, h in enumerate(arr):
            if h > peak[1]:
                peak[0] = i
                peak[1] = h

        return peak[0]
