# [LEETCODE] 문제풀이

리트코드 정복하기

🎉 100문제 달성 (2020.10.08)

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
- [x] Shuffle the Array : [x1,x2,...,xn,y1,y2,...,yn]과 같은 배열을 [x1,y1,x2,y2,...,xn,yn] 처럼 섞기
- [x] Number of Good Pairs : `i < j`이고, `nums[i]` == `nums[j]`인 i,j 쌍의 갯수 찾기
- [x] Jewels and Stones : 문자열 S에 문자열 J가 가진 character가 몇개인지 카운팅하기
- [x] Shuffle String : 문자열 s를 자신의 위체에 주어진 인덱스 위치로 변경하기
- [x] Maximum 69 Number : 6과 9로만 구성된 정수 num이 주어질 때 최대 하나(at most)의 digit만 변경 (6 -> 9, 9 ->6)해 만들 수 있는 가장 큰 수를 구하라. (그리디?)
- [x] Maximum Product of Two Elements in an Array : 가장 큰 두 수 찾아 곱하기
- [x] Number of Students Doing Homework at a Given Time : 특정 시간이 포함된 구간을 갖는 학생의 갯수 세기
- [x] Flipping an Image : binary matrix A를 flip & invert 하기
- [x] Count Negative Numbers in a Sorted Matrix : 정렬된 2차원 배열에서 음수 갯수 세기
- [x] Increasing Decreasing String : 문자열이 주어졌을때, 중복없는 알파벳의 오름차순 정렬 문자열 + 내림차순 정렬 문자열을 반복해 정렬한 문자열 반환
- [x] Generate a String With Characters That Have Odd Counts : n의 길이를 구성하는 알파벳이 홀수번만 나오도록 하는 문자열 만들기 (다양한 경우 존재)
- [x] Sort Array By Parity : 주어진 배열을 짝수가 모두 온 다음 홀수가 모두 오는 순서로 정렬하자. (순서 상관 X) (투포인터?)
- [x] Replace Elements with Greatest Element on Right Side : 자신을 자신의 오른쪽에 있는 요소들 중 가장 큰 수로 교체한 결과를 리턴
- [x] N-Repeated Element in Size 2N Array : 2N 길이의 배열 A에는 N+1개의 unique한 요소가 있고, 그 중 하나는 반드시 N번 등장한다. 이때 N번 등장하는 요소의 값을 리턴.
- [x] DI String Match : 0 ~ N까지 숫자를 I(증가), D(감소)조합에 맞춰 반환해라.
- [x] Make Two Arrays Equal by Reversing Sub-arrays : 빈 배열이 아닌 부분 배열을 골라 뒤집을 수 있을 때, 현재 배열을 목표 배열의 모양으로 만들 수 있는지 여부 확인
- [x] Can Make Arithmetic Progression From Sequence : 서로 인접한 두 수의 차이가 일정하게끔 정렬이 가능한지 여부 판단
- [x] Height Checker : 증가하는 모양으로 변경한 뒤 현재 배열과 자리가 다른 원소의 갯수는?
- [x] Lucky Numbers in a Matrix : 2차원 배열에서 row에서 가장 작고 column에서 가장 큰 수(lucky number)를 찾자.
- [x] Reverse Words in a String III : string의 각 단어를 뒤집자.
- [x] Sort Array By Parity II : 짝 /홀 순서로 정렬하기

# Stack & Queue

- [x] Design Circular Queue : 원형 큐 구현하기
- [x] Split a String in Balanced Strings : L과 R이 동일한 갯수만큼 들어간 string을 balanced string이라고 할 때, 문자열 s에서 balanced string의 갯수는?
- [x] Final Prices With a Special Discount in a Shop : i번째 아이템을 사면, i < j 이면서 prices[i] >= prices[j]를 만족하는 가장 작은 인덱스 j의 가격 만큼 할인이 가능하다. 각 아이템의 마지막 가격은? (monotonic stack)
- [x] Number of Recent Calls : 특정 시간 프레임 안의 요청의 갯수를 세는 클래스 만들기

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
- [x] Peak Index in a Mountain Array : Peak 값 찾기
- [x] The K Weakest Rows in a Matrix : 각 row 에서 1의 갯수가 작은(같다면 인덱스가 작은쪽이 우선) 순서대로 인덱스를 정렬한 뒤 k개만 리턴하기.

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
- [x] Range Sum of BST : BST의 특정 구간 안에 포함된 수 모두 더하기
- [x] Merge Two Binary Trees : 두개의 이진트리 합치기
- [x] Increasing Order Search Tree : BST를 in-order 순서로 재정렬하기
- [x] Sum of Root To Leaf Binary Numbers : 모든 값이 0 또는 1인 이진 트리에서 가장 루트를 MSB로 해서, 리프노드까지 값으로 만들어지는 이진수의 합을 구하라.

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

### 구현

- [x] Defanging an IP Address : 유효한 IP 주소(IPv4)가 주어질 때, 주소의 `.`을 `[.]`으로 교체하라.
- [x] Number of Steps to Reduce a Number to Zero : 정수가 주어질 때, 0이 되는데 걸리는 단계 수를 리턴해라. 짝수면 2로 나누고 아니면 1을 빼라.
- [x] Subtract the Product and Sum of Digits of an Integer : 정수의 digit 단위 곱 - digit 단위 합 구하기
- [x] Decompress Run-Length Encoded List : run-length encoding된 배열 nums가 주어질 때, 이를 decompressed 하기.
- [x] Create Target Array in the Given Order : 값이 있는 nums 배열과 인덱스가 있는 index 배열이 주어질 때, index[i]에 nums[i]를 삽입한 배열을 리턴
- [x] XOR Operation in an Array : nums 배열의 값을 모두 XOR 연산한 값 리턴하기
- [x] Sum of All Odd Length Subarrays : 홀수 길이의 모든 부분 배열의 합 구하기 (수학?)
- [x] Design Parking System : (간단한) 주차 시스템 구현하기
- [x] Count Good Triplets : 정수 배열 arr과 세 정수 a,b,c가 주어질 때, good triplets을 찾아라.
- [x] To Lower Case : 소문자로 변형하기
- [x] Minimum Time Visiting All Points : 좌표들이 주어질 때, 배열 순서대로 좌표들을 방문하는 최단시간 구하기
- [x] Matrix Diagonal Sum : 2차원 배열의 대각선 두개 안의 값들의 합 구하기
- [x] Remove Outermost Parentheses : 유효한 괄호 문자열이 주어질 때 가장 바깥쪽의 괄호들을 제거한 문자열 반환하기
- [x] Cells with Odd Values in a Matrix : 0으로 초기화된 n\*m 배열과 증가시킬 row, col의 인덱스 [ri, ci] 들이 포함된 배열이 주어지면 해당 row와 col을 1씩 증가시킨 2차원 배열에서 홀수 값들을 모두 더한 값을 리턴 (수학?)
- [x] Unique Morse Code Words : 모스부호로 변환한 단어의 unique한 모양의 갯수 구하기
- [x] Decrypt String from Alphabet to Integer Mapping : 문자열 해독하기 (숫자#, 숫자 구분)
- [x] Self Dividing Numbers : 상한과 하한이 주어질 때 그 안에서 가능한 self dividing number 모두 구하기
- [x] Robot Return to Origin : (0,0)에서 시작한 로봇이 주어진 방향으로 움직인 뒤 원래 자리에 있을지 여부 판단

### hashmap / hashset

- [x] Count Largest Group : 1 ~ n 까지 수들의 digit 합이 같은 것들끼리 그룹화 했을때, 가장 긴 그룹들의 갯수는?
- [x] Destination City : 다른곳으로 가는 길이 없는 도시 구하기
- [x] Unique Number of Occurrences : 값들의 발생 빈도가 unique한지 판단하기
- [x] Subdomain Visit Count : 모든 하위도메인의 방문 횟수 구하기

### bit

- [x] Convert Binary Number in a Linked List to Integer : Singley Linked List에 있는 이진수를 십진수로 변환하기
- [x] Hamming Distance : 두 수 x, y를 이진수로 표현했을 때 같은 자리에 서로 다른 비트는 몇개 있는지 구하라.

### math

- [x] Find N Unique Integers Sum up to Zero : 정수 n이 주어질 때, 합이 0이 되는 n개의 unique한 정수 배열을 찾아라. (모든 경우 가능)
- [x] Find Positive Integer Solution for a Given Equation : `f(x, y) < f(x + 1, y)`, `f(x, y) < f(x, y + 1)`를 만족하는 랜덤 함수가 주어질 때, `f(x,y) == z`를 만족하는 쌍을 모두 찾아라.

### Greedy

- [x] Minimum Subsequence in Non-Increasing Order : sum(부분집합) > sum(그외 요소들)인 부분집합을 구하라. 여러개가 존재할 경우 가장 작은 사이즈, 그리고 같은 사이즈라면 합이 더 큰 것을 찾자.
- [x] Delete Columns to Make Sorted : 세로로 (column) 묶은 쌍이 오름차순이 아닌것의 개수 카운팅

### ?

- [ ] Contain Duplicate III : 정수 배열이 주어졌을때, abs(nums[i] - nums[j]) >= t 이며 abs(i-j) >= k인 두개의 인덱스 i, j가 존재하는지 확인하라.
- [x] How Many Numbers Are Smaller Than the Current Number : 배열에서 현재 값 보다 작은건 몇개인지 알아내기
