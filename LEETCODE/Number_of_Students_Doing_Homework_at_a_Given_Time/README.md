# [LEETCODE] Number of Students Doing Homework at a Given Time

특정 시간이 포함된 구간을 갖는 학생의 갯수 세기

### 접근

`[startTime ~ queryTime ~ endTime]` 인 쌍을 찾아야 한다. 범위 내에 있는지만 확인하면 O(N)으론 충분히 끝내기가 가능.
