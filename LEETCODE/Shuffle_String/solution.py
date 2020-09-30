class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled_string = ['']*len(s)
        for i in range(len(s)):
            shuffled_string[indices[i]] = s[i]

        return "".join(shuffled_string)
