# [LEETCODE] Majority Element

전체에서 과반(Majority)인 수 찾기

### 접근

- 정렬 -> 시간 O(NlogN) 공간 O(1)
  항상 절반 이상이 존재하기 때문에 정렬한 뒤 가운데 (N//2) 숫자는 뭘 해도 그 숫자가 나올 수 밖에 없다.

- ⭐️ [Boyer–Moore majority vote algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm) -> 시간 O(N) 공간 O(1)
  일련의 요소들중 과반을 차지하는 수를 찾는 알고리즘이다.

과반 요소라면 카운팅하고, 요소가 아니라면 카운팅을 감소시킨다. 만약 카운팅이 0이되면 현재 수로 과반수를 교체한다.

정렬로 풀때 생각한 방법처럼 만약 100개가 있을 때, 과반인 수를 카운팅하면 51개를 카운팅한다. 다른 다른 수를 만나서 카운터가 0이 되더라도 다시 과반인 수로 되돌아 올 수 있다.

- 순회 & 카운팅 -> 시간 O(N) 공간 O(N)
