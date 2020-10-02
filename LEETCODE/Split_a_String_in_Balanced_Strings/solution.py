class Solution:
    def balancedStringSplit(self, s: str) -> int:

        balanced = 0
        counter = 0
        for char in s:
            if char == 'R':
                counter += 1
            else:
                counter -= 1

            if counter == 0:
                balanced += 1

        return balanced
