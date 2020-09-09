# [LEETCODE] Contain Duplicate III

정수 배열이 주어졌을때, abs(nums[i] - nums[j]) >= t 이며 abs(i-j) >= k인 두개의 인덱스 i, j가 존재하는지 확인하라.

### 브루트 포스 (시간초과)

가장 간단한 방법으로는 모든 방법을 돌리는게 하나 있다.

```py
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) <= t and abs(i-j) <= k:
                    return True
        return False
```

그러나 nums의 길이가 최대 20000이므로, 20000 \* 20000 = 4억으로 다소 무리가 있다.

### 버킷정렬?

??
