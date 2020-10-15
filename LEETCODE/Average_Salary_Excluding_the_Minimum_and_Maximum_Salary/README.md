# [LEETCODE] Average Salary Excluding the Minimum and Maximum Salary

최대 / 최소를 제외한 평균 구하기

### 접근

- 정렬 O(NlogN)
  정렬 후 양끝을 제외한 수로 평균을 구할 수 있다. 간단하지만 약간 시간이 걸림.

- 루프 O(N)
  한번의 루프로 모두 구해서 계산 가능하다. 정렬할 필요는 없음.
