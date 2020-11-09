# [LEETCODE] Intersection of Two Arrays II

두 배열의 교집합 찾기

### 접근

두 배열이 가지고 있는 동일한 원소들을 모두 찾아야 한다. (중복 포함)

1. `solution_counting.py` 한쪽을 key(값)-value(갯수) 쌍으로 모으고, 다른 한쪽을 이 Map에 비교해가며 작은쪽의 크기만큼으로 새로운 배열에 추가한다.

_Follow up:_

- What if the given array is already sorted? How would you optimize your algorithm?
  `solution_sort_twopointer.ts` 이미 정렬된 경우, 포인터를 가지고 양쪽을 순회한다. 두 값이 같다면 이를 결과에 추가하고 다음으로 이동, 또는 다르다면 비교해서 작은쪽의 포인터를 이동. 이런식으로 하면 O(N)으로 끝낼 수 있다.

- What if nums1's size is small compared to nums2's size? Which algorithm is better?

- What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
