# 브루트포스
class Solution:
    def __init__(self):
        self.ans = []

    def partitionLabels(self, S: str) -> List[int]:

        def helper(s, partitions):
            for i in range(len(s)):
                l = s[:i]
                r = s[i:]

                if i > 0 and not (set(l) & set(r)):
                    helper(r, partitions + [l])

                else:
                    last_result = partitions + [s]
                    if len(self.ans) < len(last_result):
                        self.ans = last_result

        helper(S, [])

        return [len(part) for part in self.ans]

# 투포인터


class Solution2:
    def partitionLabels(self, S: str) -> List[int]:
        right_most = {char: i for i, char in enumerate(S)}
        left, right = 0, 0

        result = []
        for i, char in enumerate(S):

            right = max(right, right_most[char])

            if i == right:
                result.append(right - left + 1)
                left = i + 1

        return result
