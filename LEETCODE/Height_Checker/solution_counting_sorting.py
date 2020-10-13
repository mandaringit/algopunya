from itertools import accumulate


class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        frequencies = [0] * (max(heights) + 1)  # 빈도 수 구하기
        for h in heights:
            frequencies[h] += 1

        # 빈도수 누적하기.
        # 누적값의 i번째 인덱스의 의미는
        # 원본 배열의 값 i가 있는 인덱스는 acc[i]라는 의미이다.
        acc = list(accumulate(frequencies))

        result = [0] * (len(heights))  # 다시 순서대로 구성할 배열
        for h in heights:
            result[acc[h]-1] = h  # acc[h] - 1은 값 h가 정렬되어있다면 원래 있어야할 인덱스를 의미한다.
            acc[h] -= 1  # 한번 사용했으니 카운트를 1 감소시킨다.

        count = 0
        for i in range(N):
            if result[i] != heights[i]:
                count += 1
        return count
