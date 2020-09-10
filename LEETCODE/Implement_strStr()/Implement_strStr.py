class Solution:
    # 그냥 find 이용해서 풀기.
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        return haystack.find(needle)

    def strStr_by_KMP(self, haystack: str, needle: str) -> int:
        """
        KMP 구현해보기
        """
        return
