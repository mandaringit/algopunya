class Solution:
    #  인덱스 이용
    def titleToNumber(self, s: str) -> int:
        num = 0
        N = len(s)
        for idx, char in enumerate(s):
            num += (ord(char) - 64) * (26**(N-1-idx))

        return num

    # doubling? 이용
    def titleToNumber(self, s: str) -> int:
        num = 0
        for char in s:
            num = num * 26 + (ord(char) - 64)  # 이전 수를 26배 함으로써 쉬프트 하는 효과.
        return num
