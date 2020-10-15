# [LEETCODE] Middle of the Linked List

Singly Linked List의 중간 구하기

### 접근

링크드 리스트는 길이를 모른다는 특징, 그리고 pointer로 가리키고 있다는 특징을 가진다.

- bruteforce O(N)
  모두 순회하여 길이를 알아낸 뒤 중간을 구한다.

- two-pointer O(N)
  하나는 한칸씩, 다른 하나는 두칸씩 진행해서 두칸씩 진행한 노드가 마지막에 닿게되면 한칸씩 진행했던 노드는 중간에 위치하게 된다. 절반만 루프해도 됨.
