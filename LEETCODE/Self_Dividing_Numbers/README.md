# [LEETCODE] Self Dividing Numbers

상한과 하한이 주어질 때 그 안에서 가능한 self dividing number 모두 구하기

### 접근

순회하면서 self dividing number인지 확인하면 될것 같다.

다만 이 self dividing number인지 확인하는 과정을 잘 구현해야할것 같다.

문자열 변환 -> 정수로 변환하지 않고, 10으로 나눈 나머지(digit)로 확인했다.

문자열의 최대 길이가 M이라면 O(N \* M)만큼 걸린다.
