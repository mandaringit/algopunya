# [LEETCODE] Convert Binary Number in a Linked List to Integer

Singley Linked List에 있는 이진수를 십진수로 변환하기

### 접근

SLL을 순회할줄만 알변 2진수를 구하는거나 이를 10진수로 변환하는건 문제가 되지 않는다. 다만 SLL을 순회하면서 2진수를 얻는다면 이는 뒤에서부터가 아닌 앞에서 부터이기 때문에 단순히 수행하기엔 2번 반복 (전부 구하고, 변환)해야 한다.

SLL을 순회함과 동시에 바로 값을 구할 수 있는 방법이 있을까?

doublig 또는 shift + OR 연산을 활용하는 방법이다. 원리는 둘다 동일하다.

- doubling

  더블링 이라는 방법이다. 다음 노드로 갈 때마다 이전 값을 2배씩 하게 된다면 한번의 연산으로 끝날 수 있다.

  예를 들자면, 1000 이라면 구할 값은 8이다.
  SLL을 순회하면 1 -> 0 -> 0 -> 0 이 순서대로 만날텐데,
  이전 값 \* 2 + 현재 값을 계속해서 수행해주면 된다.

  ```text
  1 -> 0 * 2 + 1 = 1
  0 -> 1 * 2 + 0 = 2
  0 -> 2 * 2 + 0 = 4
  0 -> 4 * 2 + 0 = 8
  ```

- 비트연산 & shift

  1. 0부터 시작해서 `기존 값 << 1`로 시프트
  2. 새로운 값을 OR 연산으로 추가. (head.val이 1이면 1이 될거고 0 이면 0이 됨)

```text
1 -> 0 << 1 = 0 | 1 = 1
0 -> 1 << 1 = 2 | 0 = 2
0 -> 2 << 1 = 4 | 0 = 4
0 -> 4 << 1 = 8 | 0 = 8
```
