# [LEETCODE] Cells with Odd Values in a Matrix

0으로 초기화된 n\*m 배열과 증가시킬 row, col의 인덱스 [ri, ci] 들이 포함된 배열이 주어지면 해당 row와 col을 1씩 증가시킨 2차원 배열에서 홀수 값들을 모두 더한 값을 리턴

### 접근

- bruteforce
  가장 간단한 방법으론 각 인덱스들을 순회, 해당 row, col도 순회하며 모두 1씩 증가시키는 방법이다.

  순회하는데 indices의 길이 L만큼 O(L) \* 각 순회당 n + m 만큼, 결과적으로 O(L(m+n) + m\*n) 만큼 걸린다. 썩 좋은 방법은 아닌 것 같다.

- bruteforce + 약간의 최적화 O(L + m\*n)

  위와 비슷하지만, 모든 행 & 열을 1씩 더하면서 카운트하지 말고 증가되는 row & col을 카운트한다. 그리고 맨 마지막에 한번 2차원 배열을 루프하면서 해당 i,j가 얼마나 나왔는지 카운트한걸 더하면 그게 값이 되므로 홀수 여부를 판단할 수 있다.

- row, col의 홀 & 짝 여부만을 판단, 수학적으로 구하기 O(L)
  값보단 홀 & 짝 여부를 판단한다. `^`는 XOR 연산자로, 1이면 0으로, 0이면 1로 변경한다. 토글한다고 생각하면 편하다.

  인덱스들로 모두 표기한 뒤에 이 값으로 답을 구한다.

  ```py
  row_count = sum(row) * m  # 홀수라고 판단되는 row의 원소 갯수들
  col_count = sum(col) * n  # 짝수라고 판단되는 col의 원소 갯수들
  # 겹친 경우, 홀 + 홀은 짝이므로 불가능한 경우다.
  overlaped = sum(row) * sum(col)
  # row, col이 겹친 원소 갯수를 위에서 두번 더했으므로 두번 빼줌(*2)
  ans = row_count + col_count - 2 * overlaped
  ```
