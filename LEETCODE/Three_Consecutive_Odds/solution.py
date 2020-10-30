class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        count = 0
        for num in arr:
            if num % 2:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        return False

    """
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        consecutive = [0]*(len(arr)+1)

        for i, num in enumerate(arr):
            if num % 2:
                consecutive[i+1] = consecutive[i] + 1

                if consecutive[i+1] == 3:
                    return True

        return False
    """
