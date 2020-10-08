# [LEETCODE] Final Prices With a Special Discount in a Shop

i번째 아이템을 사면, i < j 이면서 prices[i] >= prices[j]를 만족하는 가장 작은 인덱스 j의 가격 만큼 할인이 가능하다. 각 아이템의 마지막 가격은?

### 접근

- bruteforce
  쉬운 방법은 자신의 옆에서부터 시작해 전부 돌아보는 방법이다. O(N^2) = 500 \* 500

- stack (monotinic)

  1. 할인이 안된 가격의 인덱스를 보관할 스택을 준비.
  2. 각 가격들을 루프한다.
  3. 해당 가격시점에 할인이 안된 것들을 가장 최근것부터 조건에 맞는지 확인해서 조건에 맞다면 pop, 지금 가격으로 할인 반복

  길어봐야 O(2N)= O(N)이겠다.
