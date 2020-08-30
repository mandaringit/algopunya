# [LEETCODE] Find Numbers with Even Number of Digits

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation:
12 contains 2 digits (even number of digits).
345 contains 3 digits (odd number of digits).
2 contains 1 digit (odd number of digits).
6 contains 1 digit (odd number of digits).
7896 contains 4 digits (even number of digits).
Therefore only 12 and 7896 contain an even number of digits.

#### 숫자의 갯수가 짝수인것의 갯수는?

- 12 -> 1과 2 두개로 짝수개,
- 122 -> 1,2,2 세개로 홀수개.

이 점만 주의해서 그냥 문자열로 생각하고 길이를 센다.
