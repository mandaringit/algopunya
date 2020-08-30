class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_length = max(len(a), len(b))
        result = [0] * (max_length + 1)
        a = a.zfill(max_length)
        b = b.zfill(max_length)
        for i in range(max_length - 1, -1, -1):
            result[i + 1] += int(a[i]) + int(b[i])

            if result[i + 1] >= 2:
                result[i] = 1
                result[i + 1] -= 2

        result = result if result[0] == 1 else result[1:]

        return "".join(map(str, result))

    def addBinary2(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        return format(a + b, 'b')


sol = Solution()

print(sol.addBinary2("11", "1"))
