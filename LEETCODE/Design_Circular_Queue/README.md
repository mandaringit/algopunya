# [LEETCODE] Design Circular Queue

원형큐 구현하기

### 접근

원형큐의 개념을 잘 숙지하고 가자. 기본적으로 큐와 동일한 구조다. 한정된 큐의 공간을 어떻게 잘 활용할까. 원형큐를 활용하는 것이다.

길이가 무한한 경우 딱히 상관은 없지만, 메모리 낭비를 방지하기위해 길이를 고정시키고, 큐에서 아래와 같은 부분만 신경좀 쓴다.

초기화는 front, rear = -1

- 어떤 경우에 비었다고 볼 수 있을까 ?

  front == rear인 경우이다.

- 어떤 경우에 가득 찼다고 봐야할까?

  (rear + 1) % 큐의 사이즈 == front인 경우이다.

이게 좀 복잡하다면 size 변수를 하나 둬 두고 이를 활용해도 괜찮아 보인다.
