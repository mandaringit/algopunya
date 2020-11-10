class Solution:
    def digitSum(self, n: int) -> int:
        result = 0
        while n:
            n, r = divmod(n, 10)
            result += r ** 2

        return result

    # hashmap
    def isHappy1(self, n: int) -> bool:
        if n == 1:
            return True

        used = {}
        while n != 1:
            n = self.digitSum(n)

            if n in used:
                return False
            else:
                used[n] = True
        return True

    # floyd cycle detection
    def isHappy2(self, n: int) -> bool:
        if n == 1:
            return True

        slow = self.digitSum(n)
        fast = self.digitSum(self.digitSum(n))

        while fast != slow:
            slow = self.digitSum(slow)
            fast = self.digitSum(self.digitSum(fast))

        return fast == 1
