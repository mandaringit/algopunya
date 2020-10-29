class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        count = 0
        for x in arr1:
            is_distance = True
            for y in arr2:
                if abs(x-y) <= d:
                    is_distance = False
                    break

            if is_distance:
                count += 1

        return count
