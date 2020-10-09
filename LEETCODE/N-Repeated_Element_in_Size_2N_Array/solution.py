class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        N = len(A)
        counter = {}
        for num in A:
            if num in counter:
                return num
            else:
                counter[num] = 1
