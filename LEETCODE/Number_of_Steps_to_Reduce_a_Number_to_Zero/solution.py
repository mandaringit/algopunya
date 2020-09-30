class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num != 0:
            if num == 1:
                count += 1
                num = 0
            else:
                q, r = divmod(num, 2)
                count = count + 2 if r else count + 1
                num = q

        return count
