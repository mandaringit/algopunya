# [BOJ] 1920 수찾기

- [ ] PYTHON
- [x] JAVASCRIPT

#### 수를 찾자

간단한 방법은 for문 돌면서 해당 수가 있는지 판단하는 것. 그러나 10만개가 배열에 있고, 찾아야 하는 수가 10만개이기 때문에 최악의 경우 10만 \* 10만으로 매우 오래걸릴수 있다.

배열의 인덱스로 카운팅을 해볼까 하는것도 생각해 봤지만, 정수 범위가 굉장히 크므로 모두 만들기는 불가능.

최소한의 시간으로 찾는 방법을 선택해야한다.

#### 이진 탐색

logN의 시간이 걸리는 탐색을 통해 찾는다.

**왼쪽이 오른쪽보다 커지는 순간** 루프를 멈추도록 하여 절반씩 줄여 나간다.

#### [JS] sort

처음 정렬 시 `.sort()`만을 사용하면 틀림. compareFn을 넣어줘야함.
