# [LEETCODE] Find the Distance Value Between Two Arrays

arr1의 원소 중, arr2와의 차이의 절대값이 d보다 작은 경우가 "없는" arr1의 갯수 구하기

### 접근

문제의 설명이 쪼금 이상하지만, 이해하면 풀린다.

arr1의 원소를 돌면서, arr2와의 차이의 절대값을 구하고 이게 d보다 작거나 같은게 하나라도 있으면 패스, 아니면 카운트.

O(N^2)이지만 배열 길이가 500이므로 가능
