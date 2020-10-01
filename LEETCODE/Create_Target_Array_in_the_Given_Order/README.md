# [LEETCODE] Create Target Array in the Given Order

값이 있는 nums 배열과 인덱스가 있는 index 배열이 주어질 때, index[i]에 nums[i]를 삽입한 배열을 리턴

### 접근

insert를 쓰면 쉽게 풀 문제이지만, 삽입은 O(N)의 시간이 걸린다. 그렇기 때문에 O(N^2)의 시간 복잡도를 갖게 된다. 제한사항에서 최대 길이가 100이기 때문에 문제는 없겠다.
