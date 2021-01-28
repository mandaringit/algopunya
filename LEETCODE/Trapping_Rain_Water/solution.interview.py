from typing import List


class Solution:
    # two pointer -> to the tallest height
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        rain = 0
        left, right = 0, len(height) - 1  # 초기 위치.
        l_max, r_max = height[left], height[right]  # 초기 최댓값

        while left < right:  # 포인터 둘이 만나기 전까지 루프를 계속한다.
            if l_max < r_max:  # 왼쪽보다 오른쪽 벽이 더 큰 경우. 최소한 왼쪽 벽 높이 만큼은 물이 찬다.
                rain += l_max - height[left]
                left += 1
                l_max = max(l_max, height[left])  # 왼쪽 최대 높이 갱신
            else:
                rain += r_max - height[right]
                right -= 1
                r_max = max(r_max, height[right])  # 오른쪽 최대 높이 갱신

        return rain

    # stack
    def trap(self, height: List[int]) -> int:
        stack = []
        rain = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:

                top = stack.pop()  # 변곡점 바로 전의 땅을 스택에서 뽑는다.

                # 방금 스택에서 뽑은게 왼쪽 벽이라면 종료.
                if not len(stack):
                    break

                distance = i - stack[-1] - 1  # 변함을 감지한 위치(오른쪽 벽) ~ 왼쪽벽 사이의 거리
                # 왼쪽 벽, 오른쪽 벽중 낮은 벽을 찾고, 사이에 있는 땅의 높이를 빼 물의 높이를 구한다.
                waters = min(height[i], height[stack[-1]]) - height[top]

                rain += distance * waters

            stack.append(i)
        return rain
