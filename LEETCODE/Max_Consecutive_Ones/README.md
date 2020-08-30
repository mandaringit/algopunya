# [LEETCODE] Max Consecutive Ones

Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
The maximum number of consecutive 1s is 3.

#### 1이 연속적으로 나오는 길이들 중 가장 긴것을 찾아라

가장 간단하게, 모두 돌면서 1을 센다. 그 중 길이가 길면 바꾼다. 마지막 끝나는 경우를 주의하자.
