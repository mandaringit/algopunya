# [LEETCODE] 문제풀이

리트코드 정복하기

- 💪 : 기초적인 문제. 첫 틀을 잡는데 도움
- 🤔 : 고민했던 문제
- 👀 : 좀더 효율적인 방법은 없는지 찾아볼 문제

## 문제 리스트

### Array & String

- [x] Squares of Sorted Array : 제곱 & 정렬
- [x] Find Numbers with Even Number of Digits : 숫자 -> 문자열 & 길이로 풀기
- [x] Find Pivot Index : [0 ~ i] , [i ~ 끝] 두 배열의 전체 합이 같아지는 i 찾기. sum()은 O(N). 더 효율적인 방법은?
- [x] Largest Number At Least Twice of Others : 가장 큰 수를 찾고, 그 수가 다른 수들보다 2배 이상인지 아닌지 확인하기
- [x] Plus One : 배열로 각 digit이 주어질때 , 1을 더한 수를 배열로 다시 리턴하기. 인덱스 다루기.
- [x] Diagonal Traverse : 2차원 배열 대각선 순회하기
- [x] Pascal Triangle : 파스칼 삼각형 만들기, 인덱스 다루기
- [x] Add Binary : 이진수 더하기 (문자열 다루기 ?)
- [x] 👀Implement strStr() : 문자열 A 안에 B가 있는지 찾는 문제 (find() 함수 등의 내부 동작 원리, KMP 알고리즘 시도해보기)
- [x] Longest Common Prefix : 단어들 모두가 공통으로 가지고 있는 접두사 (prefix) 중 가장 긴 접두사를 찾아라
- [x] Reverse String : 배열안에 문자들을 반대로 뒤집는다. 단 원본 배열 그대로, 공간 복잡도 O(1)을 유지해야한다. - 투포인터
- [x] Array Partition I : 2n 개의 정수 배열이 주어질때, 이 정수들을 n개의 짝으로 묶어야 하는데, 이 짝에서 작은 쪽의 합이 가장 큰 경우를 구하라 - 투포인터
- [x] Two Sum II : (정렬된 경우) 두 수의 합이 특정 수가 되는 경우, 두 수의 인덱스 찾기 - 투포인터
- [x] Max Consecutive Ones : 1이 연속적으로 나오는 길이들 중 가장 긴것 찾기 - 투포인터
- [x] 🤔Minimum Size Subarray Sum : 부분수열의 합이 S 이상인, "최소 길이" 부분수열 합을 구하는 문제. (O(N) & O(NlogN)) - 투포인터
- [x] 💪Duplicated Zeros : 기존 배열을 복사하지 않고 하나씩 밀어보기. 배열 조작 이해
- [x] Remove Element : 원본 배열에서 특정 값 지우기, - 투포인터(FastRunner, SlowRunner)
- [ ] Merge Sorted Array : 원본 배열에 절반을 채우는데, 정렬하면서 채우기
- [ ] Spiral Matrix : 나선형으로 2차원 배열 순회하기
- [x] Running Sum of 1d Array : nums가 주어질 때, `runningSum[i] = sum(nums[0]…nums[i])`로 정의되는 누적합 배열 구하기
- [x] Kids With the Greatest Number of Candies : i번째 아이가 여분의 캔디를 받았 을 때 다른 아이들보다 최대가 될 수 있을지 여부를 모두 담은 배열을 리턴하자.

# Stack & Queue

- [x] Design Circular Queue : 원형 큐 구현하기

### Binary Search

- [x] 💪BinarySearch : 이진탐색이란?
- [x] Sqrt(x) : 특정 수의 제곱근 찾기.
- [x] Guess Number Higher or Lower : 술게임에서 소주병 밑에 숫자 맞추는 업다운 게임임. 이진탐색 기초
- [x] Search in Rotated Sorted Array : 정렬된 배열이 특정 인덱스를 기준으로 뒤집혀있을때, 특정 수 찾기
- [x] First Bad Version : 정렬된 배열에서 특정 조건이 처음 나타나는 위치 찾기. 브루트포스 O(N) vs 이진탐색 O(logN)
- [x] Find Peak Element : Peak (산꼭대기) 같은 모양이 되는 인덱스 찾기. 브루트포스 O(N) vs 이진탐색 O(logN)
- [x] 🤔Find Minimum in Rotated Sorted Array : 정렬된 배열이 특정 인덱스를 기준으로 뒤집혀있을때, 특정 수 찾기. 근데 그게 최솟값. 브루트포스 O(N) vs 이진탐색 O(logN)
- [x] 🤔Search for a Range : 특정 수의 처음 - 시작 범위 구하기. 이진 탐색 응용
- [ ] Find K Closest Elements : 어떤 수가 주어졌을때, 그 수에 가까운 K개의 수 구하기

### Binary Tree & Binary Search Tree

- [x] 💪Binary Tree Inorder Traversal : 배열로 주어진 이진 트리를 Inorder - Traversal, 중위순회 하기. (재귀 & 순회)
- [x] 💪Binary Tree Level Order Traversal : 이진트리가 주어졌을때, Level Order - Traversal, 레벨 순회 하기
- [x] 💪Binary Tree Postorder Traversal : 이진 트리가 주어졌을때, Postorder - Traversal, 후위순회 하기. (재귀 & 순회)
- [x] 💪Binary Tree Preorder Traversal : 배열로 주어진 이진 트리를 PreOrder - Traversal, 전위순회 하기. (재귀 & 순회)
- [x] Maximum Depth of Binary Tree : 이진 트리의 최대 깊이 찾기
- [x] 🤔Validate Binary Search Tree : 올바른 Binary Search Tree 인지 판단하기 (D&C)
- [x] Binary Search Tree Iterator : 이진 탐색 트리 BST 이터레이터를 직접 구현해보는 문제
- [x] 💪Search in a Binary Search Tree : 이진 탐색 트리에서 검색 연산 구현하기
- [x] 💪Insert into a Binary Search Tree : 이진 탐색 트리 BST 에 요소 삽입하기
- [x] 💪Delete Node in a BST : 이진 탐색 트리 BST에서 요소 삭제하기
- [x] 🤔Kth Largest Element in a Stream : 요소에서 K번째로 큰 숫자 찾기 (heapq)
- [x] Lowest Common Ancestor of a Binary Search Tree : 이진 탐색 트리 BST에서 노드 두개가 주어질때, 두 노드가 가지는 가장 낮은 공통 조상(Lowest Common Ancestor)을 찾아라.

### N-ary Tree / Trie

- [x] 💪N-ary Tree Preorder Traversal : n-ary 트리가 주어질 때, preorder 하기
- [x] 💪N-ary Tree Postorder Traversal : n-ary 트리가 주어졌을 때, postorder 하기
- [x] 💪N-ary Tree Level Order Traversal : n-ary 트리 레벨 순회 하기
- [x] Maximum Depth of N-ary Tree : N-ary 트리의 최대 깊이 찾기
- [x] 💪Implement Trie(Prefix Tree) : Trie 구현하기
- [x] Map Sum Pairs : 독특한 insert와 sum 메서드를 가진 MapSum 클래스 완성하기. (Trie)
- [x] Replace Words : 주어진 문장의 특정 단어에 dictionary에 있는 root가 존재한다면 해당 단어를 successor를 제외한 root로 변경하여 다시 구성한 문장을 구하는 함수를 구현하라.
- [x] Add and Search Word - Data structure design : Trie에서 insert 및 와일드카드('.')가 포함된 search를 갖는 WordDictionary 구현하기

### Recursion

- [ ] 🤔Swap Node In Pairs : 링크드 리스트가 주어졌을 때, 인접한 두개의 노드의 헤드를 서로 바꾸기.
- [ ] 🤔Reverse Linked List : 링크드 리스트 뒤집기
- [x] Pascal's Triangle II : 파스칼의 삼각형 2. O(K) 공간만 사용
- [x] Fibonacci Number : N번째 피보나치 수 구하기.
- [x] 🤔Climbing Stairs : 1걸음 또는 2걸음만 걸을 수 있을 때, n개의 계단에 오르는 경우의 수는?
- [x] Pow(x,n) : x의 n승 구하기
- [x] Sort an Array : 배열 정렬하기 (Merge Sort)
- [x] 🤔Search a 2D Matrix : 각 row 별, col 별로 오름차순 정렬된 2차원 배열에서 효율적으로 숫자 찾기 - D&C로 풀어볼것
- [x] 🤔N-Queens II : N이 주어질 때 가능한 N-Queens 경우의 수를 찾아라.
- [x] 🤔Sudoku Solver : 스도쿠 풀기 (백트래킹)
- [x] Same Tree : 같은 이진 트리인지 확인하기
- [x] Generate Parentheses : n개의 `()`를 사용할 수 있을 때, 가능한 괄호 조합을 모두 찾기.

### ?

- [ ] Contain Duplicate III : 정수 배열이 주어졌을때, abs(nums[i] - nums[j]) >= t 이며 abs(i-j) >= k인 두개의 인덱스 i, j가 존재하는지 확인하라.
- [x] Count Largest Group : 1 ~ n 까지 수들의 digit 합이 같은 것들끼리 그룹화 했을때, 가장 긴 그룹들의 갯수는? (해시?)
