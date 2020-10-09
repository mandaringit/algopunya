class Solution:
    def diStringMatch(self, S: str) -> List[int]:

        result = []
        left = 0
        right = len(S)

        for char in S:
            if char == 'I':
                result.append(left)
                left += 1
            else:
                result.append(right)
                right -= 1

        result.append(right)

        return result
