# [LEETCODE] Product of Array Except Self

자기 자신을 제외한 나머지 수들의 곱으로 이뤄진 배열 구하기

### 접근

전체 곱을 구한 뒤 i번째 자리엔 i번째 요소로 나눈 값을 넣으면 되지 않을까? 하는 생각을 먼저 해봤다.

그러나 제약사항에 Please solve it without division and in O(n). 이라고 써져있어서 일단 보류.

다른 사람들의 풀이를 참고했다. 발상은 이러하다.

원본이 [1,2,3,4] 인 배열이라 한다면, 구하고자 하는 결과 result[i]는 i번째요소를 제외한 나머지 요소들의 곱이다. 예로 result[2] = original[0] \* original[1] \* original[3] 과 같다.

이걸 두번의 루프로 구현한다. 첫번째 루프로 original[0] \* original[1] 까지, 즉 i 번째 왼쪽까지 곱하고, 역으로 루프하는 두번째 루프로 \* original[3] 을 수행할 수 있다.

결과적으로 O(N)의 시간으로 마무리할 수 있다.

```python
nums = [1,2,3,4]

# 초기
result = [1, 1, 1, 1]

# 첫번째 루프로 얻는 결과값. 자기 자신을 제외, 왼쪽 값들의 곱들만 얻는다.
result = [1, 1*1, 1*1*2, 1*1*2*3]

# 두번째 루프로 얻는 결과값. 자기 자신 제외, 오른쪽 값들의 곱을 얻는다.
result = [1*(1*4*3*2), 1*1*(1*4*3), 1*1*2*(1*4), 1*1*2*3*(1)]

```

### Follow up:

Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
