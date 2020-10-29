class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()

        N = len(arr)
        cut = int(N * 0.05)
        center = arr[cut: N - cut]

        return sum(center) / len(center)
