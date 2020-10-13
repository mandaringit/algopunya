# [LEETCODE] Unique Number of Occurrences

값들의 발생 빈도가 unique한지 판단하기

### 접근

먼저 각 값들의 발생 빈도를 파악한다. map이 유용하므로 딕셔너리를 활용한다.

1. 등장한 유니크한 값의 길이가 얼마나 되는지 파악 = `dict.keys()`
2. 등장한 값들의 발생 빈도 `value` 들의 유니크한 값의 모음의 갯수 파악 = `set(dict.values())`
