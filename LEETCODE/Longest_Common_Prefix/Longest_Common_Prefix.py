from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        prefix = []
        minimum = min(strs, key=lambda x: len(x))

        for i in range(len(minimum)):
            for s in strs:
                if s[i] != minimum[i]:
                    return "".join(prefix)

            prefix.append(minimum[i])

        return "".join(prefix)


sol = Solution()
print(sol.longestCommonPrefix(["abcd", "ab"]))
