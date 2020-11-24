class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True

        l, r = 0, len(s) - 1

        while l < r:
            char1 = s[l]
            char2 = s[r]

            if char1.isalnum() and char2.isalnum():
                if char1.lower() != char2.lower():
                    return False
                else:
                    l += 1
                    r -= 1
            else:
                if not char1.isalnum():
                    l += 1

                if not char2.isalnum():
                    r -= 1

        return True
