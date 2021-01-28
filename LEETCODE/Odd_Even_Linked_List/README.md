# [LEETCODE] Odd Even Linked List

SLL이 주어졌을 때, 값이 아닌 "순서상" 홀수인 노드들을 그룹화 하고 그 뒤에 짝수 노드들이 따라오도록 변경하자.

- 시간 O(N)
- 공간 O(1)

### 접근

노드의 next & next.next를 적절하게 사용해서 짝수 홀수로 그룹화한 뒤 홀수 노드.next를 짝수노드 시작점과 잇는다는 생각을 했다.

```text
1 -> 2 -> 3 -> 4 -> 5 # 예시

# 1 초기 세팅
홀수 : 1 -> 2 -> 3 -> 4 -> 5 -> null
짝수 : 2 -> 3 -> 4 -> 5 -> null
헤드 : 3 -> 4 -> 5 -> null

# 2 중간 while 루프
홀수 : 1 -> 3 (헤드) -> 4 -> 5 -> null
짝수 : 2 -> 4 (헤드.next) -> 5 -> null
헤드 : 5 -> null

# 3 만약 헤드가 있는 경우.
홀수 : 1 -> 3 -> 5(헤드) -> null
짝수 : 2 -> 4 -> null (헤드.next)

# 4 홀수 -> 짝수 잇기
홀수 -> 짝수 : 1 -> 3 -> 5 -> 2 -> 4 -> null
```