# [LEETCODE] Running Sum of 1d Array

nums가 주어질 때, `runningSum[i] = sum(nums[0]…nums[i])`로 정의되는 누적합 배열 구하기

### 접근

i번째 요소는 i-1번째요소와 자신의 합과 같다. 누적합이라고 해야하나 ? 그렇게 구하면 된다.

- `itertools.accumulate()` : 배열을 가져다 넣으면 누적된 값을 리턴해줌. 이를 써도 쉽게 가능

크게 성능 차이는 나지 않아 보인다.
