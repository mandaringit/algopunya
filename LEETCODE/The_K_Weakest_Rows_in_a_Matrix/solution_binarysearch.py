class Solution:
    """
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldier_counter = sorted([(sum(row), i) for i, row in enumerate(mat)])
        return [soldier_counter[i][1] for i in range(k)]
    """

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        def binary_search(row):
            l, r = 0, len(row)
            while l < r:
                mid = (l + r) // 2
                if row[mid] == 1:
                    l = mid + 1
                else:
                    r = mid
            return l

        soldier_counter = sorted([(binary_search(row), i)
                                  for i, row in enumerate(mat)])

        return [soldier_counter[i][1] for i in range(k)]
