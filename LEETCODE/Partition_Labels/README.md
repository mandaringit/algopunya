# [LEETCODE] Partition Labels

각 알파벳이 '기껏해야' 하나의 파티션에만 나타나도록 분할하기

### 접근

말이 조금 헷갈리지만, 예시를 사용해보자면

`S = "ababcbacadefegdehijhklij"`일때, 파티션을 나누는 방법은 여러가지가 있다.

1. "ababcbacadefegdehijhklij"
2. "ababcbacadefegde", "hijhklij"
3. "ababcbaca", "defegde", "hijhklij"

파티션을 나누는건 좋은데, _서로의 파티션끼리 중복되는게 있으면 안된다._

### 완전탐색

S를 A / B 두 파트로 나눠서, 두 파트의 set()에 교집합 여부로 판단, 다시 B를 같은 방법으로 재귀적으로 수행하는 방법. 직관적이지만 aaabbbcccddd 이런식이라면 굉장히 오래걸린다.

### 투포인터

먼저, Map 형식으로 각 알파벳이 위치한 가장 큰 인덱스를 모은다.

```py
s = 'aabbcceec'
right_most = {'a':1, 'b':3, 'c':8, 'e':7}
```

이제 파티션의 범위를 잡을 left, right를 선언하고 문자열을 순회한다.

right는 어떤 알파벳이 등장하면 그 알파벳의 최대 인덱스까지 가야 하나의 파티션에 한번 등장한다는 조건이 만족되므로 이를 교체하면서 진행한다. 중간에 다른 알파벳이 나와도 그 알파벳의 최대 인덱스가 이전에 나온 알파벳보다 인덱스가 작다면 파티션의 범위는 줄어들지 않고, 만약 인덱스가 더 커지면 파티션의 범위는 더 늘어나게 된다.

```text
s = 'aabbcceec'
right_most = {'a':1, 'b':3, 'c':8, 'e':7}

  i   |  문자  | 파티션 범위 [left, right]
  0        a       [0,1] -> a의 최대 인덱스는 1이다. right = 1
  1        a       [0,1] -> i == right. 하나의 파티션 완료 -> 'aa'
  2        b       [2,3] -> b의 최대 인덱스는 3이다. right = 3
  3        b       [2,3] -> i == right. 하나의 파티션 완료 -> 'bb'
  4        c       [4,8] -> c의 최대 인덱스는 8이다. right = 8
  5        c       [4,8]
  6        e       [4,8] -> e의 최대 인덱스는 7이다. 기존보다 작으므로 변경 X
  7        e       [4,8]
  8        c       [4,8] -> i == right. 하나의 파티션 완료 -> 'cceec'
```

```py
left, right = 0, 0
for i, char in enumerate(s):

  # 파티션의 오른쪽 끝을 지금 등장한 알파벳의 최대 인덱스로 조절한다.
  right = max(right, right_most[char])

  # i가 right에 도달한 경우 하나의 파티션이 완성된 것이다.
  if i == right:
    # 1. 결과에 파티션 길이 추가하기
    # 2. 파티션의 왼쪽 끝을 조정
    left = i + 1
```
