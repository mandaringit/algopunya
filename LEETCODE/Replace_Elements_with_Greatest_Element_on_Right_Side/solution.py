class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        N = len(arr)
        greatest = -1
        for i in range(N-1, -1, -1):
            origin = arr[i]
            arr[i] = greatest  # 현재 최댓값으로 변경

            if origin > greatest:  # 현재 자리의 원본값이 지금 최댓값보다 크면 변경
                greatest = origin

        return arr
