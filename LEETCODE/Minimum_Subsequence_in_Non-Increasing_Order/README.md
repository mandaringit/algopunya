# [LEETCODE] Minimum Subsequence in Non-Increasing Order

sum(부분집합) > sum(그외 요소들)인 부분집합을 구하라. 여러개가 존재할 경우 가장 작은 사이즈, 그리고 같은 사이즈라면 합이 더 큰 것을 찾자.

### 접근

조건 덕분에 오름차순 정렬 후, 항상 그 다음 가장 큰 수만 선택해 가면서 선택한 값의 합 > 나머지 값의 합인 경우 바로 리턴하면 된다.