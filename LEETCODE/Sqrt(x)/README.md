# [LEETCODE] Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2

Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
the decimal part is truncated, 2 is returned.

### 제곱근 구하기

제곱근의 내림을 구하는건데 이걸 이진 탐색으로 해보는 문제다. 생각해보기에 일단 x의 제곱근이 될 수 있는 범위는 0 ~ x이다. 그러면 이걸 정렬된 배열로 생각하고 문제를 풀어본다.

1. mid의 제곱이 x라면 곧바로 리턴하면 된다.
2. mid의 제곱이 x보다 크다면, 이건 후보가 될 수 없다. r을 mid -1로 변경한다.
3. mid의 제곱이 x보다 작다면 이건 제곱근의 후보가 될 수 있다. 결과값을 저장하고 l을 mid + 1로 변경한다.

3번의 과정을 탐색을 계속하면서 result에 해당 수의 제곱근에 가까운 수로 가까워지기 때문에 마지막엔 결과를 알 수 있다.

다른사람들 풀이에선 그냥 0.5제곱 한 후 소숫점을 날리거나, `mid의 제곱 <= x < mid+1의 제곱` 으로 비교해서 결과를 도출해 내기도 했다.
