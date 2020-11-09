from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        result = []

        for key in nums2:
            if c1[key] > 0:
                result.append(key)
                c1[key] -= 1

        return result
