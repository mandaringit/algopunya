class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        arr.sort()

        N = len(arr)
        minimum = float('inf')
        pairs = []
        for i in range(N-1):
            a, b = arr[i], arr[i+1]
            diff = abs(a - b)
            if diff == minimum:
                pairs.append([a, b])
            elif diff < minimum:
                minimum = diff
                pairs = [[a, b]]

        return pairs
