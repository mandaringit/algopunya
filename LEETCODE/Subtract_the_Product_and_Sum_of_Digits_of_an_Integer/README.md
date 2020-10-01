# [LEETCODE] Subtract the Product and Sum of Digits of an Integer

정수의 digit 단위 곱 - digit 단위 합 구하기

### 접근

정수를 받았을때 digit을 구하는 방법은 string으로 변경 후 list화 하는 방법도 있긴 하지만, type casting하는데 시간이 걸리기도 하고, 바로 숫자로 쓸 수도 없으니 10으로 나눈 나머지를 활용하는게 용이하다.
