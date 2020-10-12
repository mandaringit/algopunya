class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()

        diff = set()
        for i in range(len(arr)-1):
            diff.add(arr[i] - arr[i+1])
            if len(diff) >= 2:
                return False

        return True
