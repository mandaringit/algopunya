class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        a, b = -1, -1  # 각각 첫번째로 큰 수, 두번째로 큰 수

        for num in nums:
            if num >= a:  # a보다 큰 수
                temp = a
                a = num  # a는 큰 수로 바꾸고
                b = temp  # b는 a로 교환. a가 전까지 가장 큰 수였을 테니..

            elif num >= b:  # a보단 작고 b보다 크면 b만 교환
                b = num

        return (a-1) * (b-1)
