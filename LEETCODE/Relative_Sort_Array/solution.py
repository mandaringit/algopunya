class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {i: 0 for i in arr2}
        rest = []

        for num in arr1:
            if num in order:
                order[num] += 1
            else:
                rest.append(num)

        realtive = []
        for key in order:
            realtive.extend([key]*order[key])

        rest.sort()

        return realtive + rest
