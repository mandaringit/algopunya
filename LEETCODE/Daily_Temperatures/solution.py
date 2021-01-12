class Solution:
    '''
    거리를 계산하면서 풀기. O(N * 온도범위)
    '''

    def dailyTemperatures(self, T: List[int]) -> List[int]:
        T_idx = [None] * 101
        result = [0] * len(T)

        for i in range(len(T)-1, -1, -1):
            current_T = T[i]  # 현재 온도
            T_idx[current_T] = i  # 위치 기록
            d = 0  # 거리
            for t in range(current_T + 1, 101):
                t_loc = T_idx[t]
                if t_loc:  # 온도는 나보다 크고,
                    diff = t_loc - i
                    d = diff if d == 0 else min(diff, d)

            result[i] = d

        return result

    '''
    스택 사용하기. O(N)
    '''

    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0] * len(T)
        stack = []

        for i, t in enumerate(T):
            # 마지막 인덱스의 온도가 현재 온도보다 작은 경우에만,
            while stack and T[stack[-1]] < t:
                prev_i = stack.pop()
                d = i - prev_i
                result[prev_i] = d

            stack.append(i)
        return result
