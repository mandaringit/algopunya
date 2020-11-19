class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pair = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for bracket in s:
            if bracket in pair:
                stack.append(bracket)
            elif stack and pair.get(stack[-1]) == bracket:
                stack.pop()
            else:
                return False

        return len(stack) == 0
