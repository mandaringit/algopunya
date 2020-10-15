# [LEETCODE] Build an Array With Stack Operations

1 ~ n까지 수를 순회할때, target을 만들기 위해 수행할 Push & Pop 연산을 배열에 담아 리턴.

### 접근

타겟을 포인터로 하나 가리키면서 1 ~ n까지 순회해 간다. 순회하다 타겟과 같다면 Push 이후 타겟의 인덱스를 1증가 시킨다. 증가시킨 인덱스가 target의 길이와 같으면 멈춘다.
만약 같지 않다면 Push & Pop.
