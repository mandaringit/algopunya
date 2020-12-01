from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 내장 함수 사용
        # return permutations(nums)

        # DFS 사용
        result = []
        self.dfs(nums, [], result)
        return result

    def dfs(self, nums, path, result):
        # 모든 수를 다 쓴 경우.
        if not nums:
            result.append(path)

        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], result)
