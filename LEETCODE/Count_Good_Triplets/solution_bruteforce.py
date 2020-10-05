class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        N = len(arr)
        count = 0
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j]-arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1

        return count
