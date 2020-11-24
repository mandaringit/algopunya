# [LEETCODE] Remove Duplicates from Sorted Array

정렬된 배열에서 중복 제거하기 (in-place)

### 접근

추가적인 공간을 만들지 않고 중복을 제거한 배열을 얻기 위해선 어떻게 해야할까.

이 문제에선 중복이 안되게 일단 정렬을 하고 그 정렬된 배열의 길이를 리턴하라고 했다. 어쨌든 정렬은 해야한다.

그렇다면 중복된 수들을 뒤로 밀어내는 방법이 생각난다. 투포인터 접근을 생각해봤다.

- slow 포인터는 여기까지가 중복되지 않았다는, 중복을 제거한 배열의 마지막 인덱스를 가리킨다. 사실상 리턴값이다.
- fast 포인터는 전체 배열을 탐색해 나가기 위한 포인터이다.

1. fast가 slow보다 작거나 같으면 fast를 증가시킨다. (다음으로 넘어감)
2. fast가 slow보다 커질때, slow를 1증가시키고 그 자리에 가져온다. (swap)

여기선 이미 수들이 정렬되어 있기 때문에 가능한 방법이라고 할 수 있겠다. 즉, 간단히 말하면 순회하면서 중복되지 않은 수들만 하나씩 수집해서 앞쪽에 가져다 놓는 모습이라고 생각하면 된다.