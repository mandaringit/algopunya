# [LEETCODE] Convert Sorted Array to Binary Search Tree

정렬된 배열을 높이가 균형잡힌 BST로 변환하기

### 접근

BST로 변환하는건 쉽지만 균형잡힌 BST라. 어떻게 바꿔야 할까.

먼저 처음에 중심을 가운데로 잡아야 하는건 알겠다. 그리고 왼쪽 절반 오른쪽 절반을 순회하면서 삽입하면 되지 않을까? 이건 원소 갯수가 홀수개일 때만 가능하다. 짝수개라면 어느 한쪽이 높이가 1이더 커지기 마련이다.

그러면 중심을 가운데로 잡았던 것처럼, 왼쪽 절반과 오른쪽 절반도 동일하게 가운데 수를 잡아 진행하는 방식을 쓰면 좋을것 같다는 생각이 들었다. 마치 병합정렬처럼?

구현하기 단순한건 슬라이싱해서 전달하는 방법, 그리고 메모리나 시간쪽에서 시간을 덜 소비하는 인덱스를 전달하는 방법 두가지가 있을 것 같다.
