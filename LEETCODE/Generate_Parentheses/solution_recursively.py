from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def helper(left, right, pattern):

            if left == n and right == n:
                result.append(pattern)
                return
            elif left == n and right < n:
                helper(left, right + 1, pattern + ")")
            elif left == right:
                helper(left + 1, right, pattern + "(")
            elif left > right:
                helper(left + 1, right, pattern + "(")
                helper(left, right + 1, pattern + ")")

        helper(0, 0, "")

        return result


sol = Solution()
sol.generateParenthesis(3)
