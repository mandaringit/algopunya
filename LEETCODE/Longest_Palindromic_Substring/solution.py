class Solution:
    # 1. 브루트 포스, TLE
    def longestPalindrome(self, s: str) -> str:
        LPS = s[0]
        for i in range(1, len(s)):
            for j in range(len(s) - i):
                substr = s[j:j + i + 1]
                if substr == substr[::-1]:
                    LPS = substr

        return LPS

    # 2.
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s

        def expand(left: int, right: int) -> str:
            # 중간에서부터 양쪽으로 팽창 & 팰린드롬인지 확인한다.
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            # 루프가 멈춘 left & right보다 1씩 작은 범위.
            return s[left+1:right]

        result = ''
        for i in range(len(s) - 1):
            # 이전 결과와 각각 두개/세개부터 시작하는 슬라이딩 윈도우의 길이를 키로 최댓값을 구함.
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)

        return result
