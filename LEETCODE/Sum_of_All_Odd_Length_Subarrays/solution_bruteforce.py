class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        total = 0
        for term in range(1, len(arr) + 1, 2):
            for i in range(len(arr) - term + 1):
                total += sum(arr[i:i+term])

        return total
