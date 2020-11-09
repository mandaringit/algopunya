# [LEETCODE] Number of 1 Bits

1비트 갯수 구하기

### 접근

1. 내장함수로 이진수로 변환한 뒤, 1의 갯수를 세는 방법 (문자열)
2. n & n-1을 했을 때 값이 0이 될 때까지 카운트 + 하기. n
   n = XXXXXX1000, n - 1 is XXXXXX0111. n & (n - 1) will be XXXXXX0000 which is just remove the last significant 1
