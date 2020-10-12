class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        big = arr[0]
        small = arr[0]

        for num in arr:
            if num > big:
                big = num
            if num < small:
                small = num

        gap = (big - small) // (len(arr) - 1)

        if gap == 0:
            return True

        return set(arr) == set(i for i in range(small, big+1, gap))
