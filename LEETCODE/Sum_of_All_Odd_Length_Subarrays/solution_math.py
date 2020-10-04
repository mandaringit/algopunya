class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        N = len(arr)
        total = 0
        for i in range(len(arr)):
            count = ((i+1)*(N-i)+1) // 2  # 부분 배열에서 A[i]의 등장횟수
            total += arr[i]*count

        return total
