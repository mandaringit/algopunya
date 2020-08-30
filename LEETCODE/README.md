# [LEETCODE] 문제풀이

리트코드 정복하기

- 💪 : 기초적인 문제. 첫 틀을 잡는데 도움
- 🤔 : 고민했던 문제
- 👀 : 좀더 효율적인 방법은 없는지 찾아볼 문제

## 문제 리스트

#### A

- Add Binary : 이진수 더하기 (문자열 다루기 ?)

#### B

- 💪 BinarySearch : 이진탐색이란?

#### D

- 💪Duplicated Zeros : 기존 배열을 복사하지 않고 하나씩 밀어보기. 배열 조작 이해

#### F

- 🤔 Find Minimum in Rotated Sorted Array : 정렬된 배열이 특정 인덱스를 기준으로 뒤집혀있을때, 특정 수 찾기. 근데 그게 최솟값. 브루트포스 O(N) vs 이진탐색 O(logN)
- Find Numbers with Even Number of Digits : 숫자 -> 문자열 & 길이로 풀기
- Find Peak Element : Peak (산꼭대기) 같은 모양이 되는 인덱스 찾기. 브루트포스 O(N) vs 이진탐색 O(logN)
- Find Pivot Index : [0 ~ i] , [i ~ 끝] 두 배열의 전체 합이 같아지는 i 찾기. sum()은 O(N). 더 효율적인 방법은?
- First Bad Version : 정렬된 배열에서 특정 조건이 처음 나타나는 위치 찾기. 브루트포스 O(N) vs 이진탐색 O(logN)

#### G

- Guess Number Higher or Lower : 술게임에서 소주병 밑에 숫자 맞추는 업다운 게임임. 이진탐색 기초

#### I

- 👀Implement strStr() : 문자열 A 안에 B가 있는지 찾는 문제 (find() 함수 등의 내부 동작 원리, KMP 알고리즘 시도해보기)

#### L

- Largest Number At Least Twice of Others : 가장 큰 수를 찾고, 그 수가 다른 수들보다 2배 이상인지 아닌지 확인하기
- Longest Common Prefix : 단어들 모두가 공통으로 가지고 있는 접두사 (prefix) 중 가장 긴 접두사를 찾아라

#### M

- Max Consecutive Ones : 1이 연속적으로 나오는 길이들 중 가장 긴것 찾기

#### P

- Pascal Triangle : 파스칼 삼각형 만들기, 인덱스 다루기

#### S

- 🤔Search for a Range : 특정 수의 처음 - 시작 범위 구하기. 이진 탐색 응용
- Search in Rotated Sorted Array : 정렬된 배열이 특정 인덱스를 기준으로 뒤집혀있을때, 특정 수 찾기
- Sqrt(x) : 특정 수의 제곱근 찾기.
- Squares of Sorted Array : 제곱 & 정렬

### 🤯 아직 못풀었음. 쫌만 더 고민해보겠음

- Find K Closest Elements : 어떤 수가 주어졌을때, 그 수에 가까운 K개의 수 구하기
- Merge Sorted Array : 원본 배열에 절반을 채우는데, 정렬하면서 채우기
