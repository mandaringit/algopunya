class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while True:
            increment_num = digits[i] + 1

            if increment_num == 10:
                digits[i] = 0
                i -= 1
                if i < 0:
                    digits = [1] + digits
                    break
            else:
                digits[i] = increment_num
                break

        return digits
